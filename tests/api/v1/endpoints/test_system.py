import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import datetime

# Adjust import based on the new location relative to the project root
from app.main import app
from app.models.system import SystemInfoResponse, MemoryInfo, DiskInfo

# Use TestClient against the main app
client = TestClient(app)

@pytest.fixture
def mock_system_info_data():
    """Provides mock data that get_system_info would return."""
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

def test_read_system_info_endpoint(mock_system_info_data):
    """Tests the /api/v1/system_info endpoint with mocked data."""
    # Patch the get_system_info function within the system endpoint module
    with patch('app.api.v1.endpoints.system.get_system_info', return_value=mock_system_info_data) as mock_get:
        response = client.get("/api/v1/system_info")

        assert response.status_code == 200
        mock_get.assert_called_once() # Ensure our mock was called

        # Validate response body against the Pydantic model
        response_data = response.json()

        # Pydantic v2+ serializes datetime to ISO 8601 string including timezone
        # Ensure comparison uses the same timezone awareness if needed
        # The mock data now includes timezone info
        expected_data = mock_system_info_data.model_dump(mode='json')

        # Compare timestamps carefully - convert response string to offset-aware datetime
        response_time = datetime.datetime.fromisoformat(response_data['current_time'])
        expected_time = datetime.datetime.fromisoformat(expected_data['current_time'])
        assert response_time == expected_time

        # Compare the rest of the data, excluding the time which we already checked
        response_data_no_time = {k: v for k, v in response_data.items() if k != 'current_time'}
        expected_data_no_time = {k: v for k, v in expected_data.items() if k != 'current_time'}
        assert response_data_no_time == expected_data_no_time

        # Check specific fields for clarity
        assert response_data["os_info"] == "Linux 5.15.0-generic (Mocked Version)"
        assert response_data["memory"]["total"] == "15.50GB"
        assert response_data["disk"]["percent_used"] == 45.4
        assert response_data["uptime"] == "1 days, 02:30:05" 