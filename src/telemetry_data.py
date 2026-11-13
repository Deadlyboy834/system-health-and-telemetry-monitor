from dataclasses import dataclass, field
from datetime import timedelta

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