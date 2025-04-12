import pytest
from unittest.mock import patch, MagicMock
import datetime

# Adjust import based on the new location relative to the project root
from app.models.system import SystemInfoResponse, MemoryInfo, DiskInfo

@pytest.fixture
def mock_system_info_data_fixture(): # Renamed fixture to avoid conflicts if run together
    """Provides mock data expected from get_system_info."""
    # Use the same fixed datetime for consistency
    fixed_time = datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    return SystemInfoResponse(
        current_time=fixed_time,
        os_info="Linux 5.15.0-generic (Mocked Version)",
        cpu_info="Mock Processor (8 Cores @ 3000.00Mhz)",
        memory=MemoryInfo(total="15.50GB", available="7.80GB", percent_used=49.7),
        disk=DiskInfo(total="99.50GB", used="45.20GB", free="54.30GB", percent_used=45.4),
        uptime="1 days, 02:30:05"
    )

# Example test for the utility function (requires more mocking)
@patch('app.core.system_utils.platform')
@patch('app.core.system_utils.psutil')
@patch('app.core.system_utils.datetime')
def test_get_system_info_utility(mock_dt, mock_psutil, mock_platform, mock_system_info_data_fixture):
    """Tests the get_system_info utility function with extensive mocking."""
    # Import locally to ensure patches are applied
    from app.core.system_utils import get_system_info

    # --- Mock platform --- 
    mock_uname = MagicMock()
    mock_uname.system = "Linux"
    mock_uname.release = "5.15.0-generic"
    mock_uname.version = "Mocked Version"
    mock_platform.uname.return_value = mock_uname
    mock_platform.processor.return_value = "Mock Processor"

    # --- Mock psutil --- 
    mock_cpu_freq = MagicMock()
    mock_cpu_freq.max = 3000.00
    mock_psutil.cpu_freq.return_value = mock_cpu_freq
    mock_psutil.cpu_count.return_value = 8

    mock_vmem = MagicMock()
    mock_vmem.total = 15.5 * 1024**3 # 15.5 GB in bytes
    mock_vmem.available = 7.8 * 1024**3 # 7.8 GB in bytes
    mock_vmem.percent = 49.7
    mock_psutil.virtual_memory.return_value = mock_vmem

    mock_disk_part = MagicMock()
    mock_disk_part.mountpoint = '/'
    mock_disk_part.opts = 'rw' # Ensure this matches the logic in get_system_info
    mock_psutil.disk_partitions.return_value = [mock_disk_part]

    mock_disk_usage = MagicMock()
    mock_disk_usage.total = 99.5 * 1024**3
    mock_disk_usage.used = 45.2 * 1024**3
    mock_disk_usage.free = 54.3 * 1024**3
    mock_disk_usage.percent = 45.4
    mock_psutil.disk_usage.return_value = mock_disk_usage

    # Calculate expected boot timestamp based on fixed_time and expected uptime string
    expected_uptime_delta = datetime.timedelta(days=1, hours=2, minutes=30, seconds=5)
    mock_boot_timestamp = (mock_system_info_data_fixture.current_time - expected_uptime_delta).timestamp()
    mock_psutil.boot_time.return_value = mock_boot_timestamp

    # --- Mock datetime --- 
    # Mock datetime.now() to return the fixed time from the fixture
    mock_now = mock_system_info_data_fixture.current_time
    mock_dt.datetime.now.return_value = mock_now
    # Ensure fromtimestamp returns timezone-aware datetime if needed, though psutil.boot_time is typically naive UTC
    # We will compare the final string representation for uptime
    mock_dt.datetime.fromtimestamp.side_effect = lambda ts: datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
    mock_dt.timezone = datetime.timezone # Provide timezone object if needed

    # --- Call the function --- 
    result = get_system_info()

    # --- Assertions --- 
    # Compare results against the fixture data
    assert result.os_info == mock_system_info_data_fixture.os_info
    assert result.cpu_info == mock_system_info_data_fixture.cpu_info
    assert result.memory.total == mock_system_info_data_fixture.memory.total
    assert result.memory.available == mock_system_info_data_fixture.memory.available
    assert result.memory.percent_used == mock_system_info_data_fixture.memory.percent_used
    assert result.disk.total == mock_system_info_data_fixture.disk.total
    assert result.disk.used == mock_system_info_data_fixture.disk.used
    assert result.disk.free == mock_system_info_data_fixture.disk.free
    assert result.disk.percent_used == mock_system_info_data_fixture.disk.percent_used
    assert result.uptime == mock_system_info_data_fixture.uptime
    assert result.current_time == mock_now # Check against the mocked now time 