import platform
import socket
import time

from datetime import timedelta

from rich.live import Live
from rich.table import Table

from data.constants import Constants

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

def get_telemetry_table(telemetry_info: SystemTelemetry, width: int) -> Table:
    table: Table = Table(width=width, show_lines=True).grid(padding=(0, 2), expand=False)
    table.title = "TELEMETRY DATA"
    table.add_column(justify="left", style="")
    table.add_column(justify="right")

    table.add_row(
        "CPU Usage:",
        f"{telemetry_info.cpu_usage_percentage:.2f}%"
    )

    table.add_row(
        "RAM Usage:",
        f"{telemetry_info.ram_usage_percentage:.2f}%"
    )

    table.add_row(
        "Disk Usage:",
        f"{telemetry_info.disk_usage_percentage:.2f}%"
    )

    table.add_row(
        "System Uptime:",
        str(telemetry_info.system_uptime)
    )

    table.add_row(
        "Hostname:",
        telemetry_info.system_host_name
    )

    table.add_row(
        "Operating System:",
        telemetry_info.system_os
    )

    table.add_row(
        "CPU Cores:",
        str(telemetry_info.num_cpu_cores)
    )

    table.add_row(
        "Total RAM:",
        f"{telemetry_info.total_ram:,} bytes"
    )

    table.add_row(
        "Disk Capacity:",
        f"{telemetry_info.disk_capacity:,} bytes"
    )

    return table

if __name__ == "__main__":
    telemetry_data: SystemTelemetry = SystemTelemetry()
    telemetry_data = telemetry_update(telemetry_data)

    with Live(get_telemetry_table(telemetry_data, width=75), refresh_per_second=Constants.Telemetry.UI_REFRESH_FREQUENCY) as live:
        while True:
            telemetry_data = telemetry_update(telemetry_data)
            time.sleep(Constants.Telemetry.UPDATE_FREQUENCY)
            live.update(get_telemetry_table(telemetry_data, width=52))