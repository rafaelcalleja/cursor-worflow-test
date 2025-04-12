import platform
import psutil
import datetime
import os

from app.models.system import SystemInfoResponse, MemoryInfo, DiskInfo


def _get_size(bytes_val, suffix="B"):
    """Scale bytes to its proper format e.g: 1253656 => '1.20MB'"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_val < factor:
            return f"{bytes_val:.2f}{unit}{suffix}"
        bytes_val /= factor
    return f"{bytes_val:.2f}P{suffix}" # Should suffice

def get_system_info() -> SystemInfoResponse:
    """Gathers various system information accessible by the current user."""
    try:
        uname = platform.uname()
        os_info = f"{uname.system} {uname.release} ({uname.version})"
    except Exception:
        os_info = "N/A"

    try:
        cpu_freq = psutil.cpu_freq()
        cpu_info = f"{platform.processor()} ({psutil.cpu_count(logical=True)} Cores @ {cpu_freq.max:.2f}Mhz)"
    except Exception:
        try: # Fallback if freq fails
             cpu_info = f"{platform.processor()} ({psutil.cpu_count(logical=True)} Cores)"
        except Exception:
            cpu_info = "N/A"

    try:
        svmem = psutil.virtual_memory()
        memory = MemoryInfo(
            total=_get_size(svmem.total),
            available=_get_size(svmem.available),
            percent_used=svmem.percent
        )
    except Exception:
        memory = MemoryInfo(total="N/A", available="N/A", percent_used=0.0)

    try:
        partitions = psutil.disk_partitions()
        root_partition = None
        for p in partitions:
             # Attempt to find the root partition mount point
             # This heuristic might need adjustment depending on the system
            if p.mountpoint == '/' and 'rw' in p.opts.lower():
                root_partition = p
                break

        if root_partition:
            partition_usage = psutil.disk_usage(root_partition.mountpoint)
            disk = DiskInfo(
                total=_get_size(partition_usage.total),
                used=_get_size(partition_usage.used),
                free=_get_size(partition_usage.free),
                percent_used=partition_usage.percent
            )
        else:
             disk = DiskInfo(total="N/A", used="N/A", free="N/A", percent_used=0.0)

    except Exception:
        disk = DiskInfo(total="N/A", used="N/A", free="N/A", percent_used=0.0)

    try:
        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
        now = datetime.datetime.now()
        uptime_delta = now - boot_time
        # Format uptime nicely (e.g., "X days, HH:MM:SS")
        total_seconds = int(uptime_delta.total_seconds())
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"
    except Exception:
        uptime_str = "N/A"

    current_time = datetime.datetime.now()

    return SystemInfoResponse(
        current_time=current_time,
        os_info=os_info,
        cpu_info=cpu_info,
        memory=memory,
        disk=disk,
        uptime=uptime_str
    ) 