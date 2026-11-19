import platform
import socket
import time
from dataclasses import dataclass, field, astuple
from datetime import timedelta
from typing import Any
from src.config import Telemetry
from src.utils.file_io import update_logs

import psutil
from psutil._ntuples import svmem

@dataclass
class SystemTelemetry:
    cpu_usage_percentage: float | int = field(init=False)
    ram_usage_percentage: float | int = field(init=False)
    disk_usage_percentage: float | int = field(init=False)
    system_uptime: timedelta = field(init=False)
    system_host_name: str = field(init=False)
    system_os: str = field(init=False)
    num_cpu_cores: int = field(init=False)
    total_ram: float | int = field(init=False)
    disk_capacity: float | int = field(init=False)

def get_updated_telemetry(telemetry_data: SystemTelemetry) -> SystemTelemetry:
    def get_disk_usage_info() -> tuple[float | int, int]:
        total_bytes: int = 0
        used_bytes: int = 0

        for partition in psutil.disk_partitions():
            if partition.fstype:
                usage = psutil.disk_usage(partition.mountpoint)
                total_bytes += usage.total
                used_bytes += usage.used

        return (used_bytes / total_bytes) * 100, total_bytes
    def get_system_uptime() -> timedelta:
        boot_timestamp: float | int = psutil.boot_time()
        uptime_seconds: float | int = time.time() - boot_timestamp

        return timedelta(seconds=int(uptime_seconds))

    virtual_memory: svmem = psutil.virtual_memory()
    disk_usage_info: tuple[float | int, int] = get_disk_usage_info()

    telemetry_data.cpu_usage_percentage = psutil.cpu_percent()
    telemetry_data.ram_usage_percentage = virtual_memory.percent
    telemetry_data.disk_usage_percentage = disk_usage_info[0]
    telemetry_data.system_uptime = get_system_uptime()
    telemetry_data.system_host_name = socket.gethostname()
    telemetry_data.system_os = platform.system()
    telemetry_data.num_cpu_cores = psutil.cpu_count() or -1
    telemetry_data.total_ram = virtual_memory.total
    telemetry_data.disk_capacity = disk_usage_info[1]

    return telemetry_data

def log_telemetry(telemetry_data: SystemTelemetry) -> None:
    values: list[Any] = [entry for entry in astuple(telemetry_data)]
    headers: list[str] = Telemetry.HEADERS
    new_log_entry: dict[str, Any] = {}

    for index in range(len(values)):
        new_log_entry[headers[index]] = values[index]

    update_logs(new_log_entry, headers=headers)