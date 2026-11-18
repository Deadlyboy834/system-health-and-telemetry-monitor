import time

from rich.live import Live
from src.constants import Telemetry
from ui.cli import get_telemetry_table
from src.telemetry.system_telemetry_manager import SystemTelemetry, get_updated_telemetry
from src.utils.paths import initialize_logs

if __name__ == "__main__":
    initialize_logs()
    telemetry_data: SystemTelemetry = SystemTelemetry()
    telemetry_data = get_updated_telemetry(telemetry_data)

    with Live(get_telemetry_table(telemetry_data, width=75), refresh_per_second=Telemetry.UI_REFRESH_FREQUENCY) as live:
        while True:
            telemetry_data = get_updated_telemetry(telemetry_data)
            time.sleep(Telemetry.UPDATE_FREQUENCY)
            live.update(get_telemetry_table(telemetry_data, width=52))