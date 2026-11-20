from rich.table import Table

from src.telemetry.system_telemetry_manager import SystemTelemetry

def get_telemetry_table(telemetry_info: SystemTelemetry, width: int) -> Table:
    table: Table = Table(width=width, show_lines=True).grid(padding=(0, 2), expand=False)
    table.title = "TELEMETRY DATA"
    table.add_column(justify="left", style="")
    table.add_column(justify="right")

    # TODO: get the keys from the config.py headers instead of hard-code
    keys: list[str] = [
        "CPU Usage:",
        "RAM Usage:",
        "Disk Usage:",
        "System Uptime:",
        "Hostname:",
        "Operating System:",
        "CPU Cores:",
        "Total RAM:",
        "Disk Capacity:",
        "Status Number: ",
        "System Status: "
    ]

    values: list[str] = [
        f"{telemetry_info.cpu_usage_percentage:.2f}%",
        f"{telemetry_info.ram_usage_percentage:.2f}%",
        f"{telemetry_info.disk_usage_percentage:.2f}%",
        str(telemetry_info.system_uptime),
        telemetry_info.system_host_name,
        telemetry_info.system_os,
        str(telemetry_info.num_cpu_cores),
        f"{telemetry_info.total_ram:,} bytes",
        f"{telemetry_info.disk_capacity:,} bytes",
        f"{telemetry_info.status_number: .2f}",
        f"{telemetry_info.system_status}"
    ]

    for index in range(len(keys)):
        table.add_row(keys[index], values[index])

    return table