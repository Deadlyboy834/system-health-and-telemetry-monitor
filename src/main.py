import os
import platform
import socket
import time
from datetime import timedelta

import psutil
from psutil._ntuples import svmem

from telemetry_data import SystemTelemetry

def telemetry_update(telemetry_info: SystemTelemetry) -> SystemTelemetry:
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

    telemetry_info.cpu_usage_percentage = psutil.cpu_percent()
    telemetry_info.ram_usage_percentage = virtual_memory.percent
    telemetry_info.disk_usage_percentage = disk_usage_info[0]
    telemetry_info.system_uptime = get_system_uptime()
    telemetry_info.system_host_name = socket.gethostname()
    telemetry_info.system_os = platform.system()
    telemetry_info.num_cpu_cores = psutil.cpu_count() or -1
    telemetry_info.total_ram = virtual_memory.total
    telemetry_info.disk_capacity = disk_usage_info[1]

    return telemetry_info

if __name__ == "__main__":
    telemetry_data: SystemTelemetry = SystemTelemetry()

    while True:
        telemetry_data = telemetry_update(telemetry_data)

        print(telemetry_data)

        os.system("cls")