from dataclasses import dataclass
from datetime import timedelta

@dataclass
class SystemTelemetry:
    cpu_usage_percentage: float | int
    ram_usage_percentage: float | int
    disk_usage_percentage: float | int
    system_uptime: timedelta
    system_host_name: str
    system_os: str
    num_cpu_cores: int
    total_ram: float | int
    disk_capacity: float | int