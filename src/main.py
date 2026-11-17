import time

from rich.live import Live

from data.constants import Constants

from ui.cli import get_telemetry_table

from src.data.telemetry_data import SystemTelemetry, telemetry_update

if __name__ == "__main__":
    telemetry_data: SystemTelemetry = SystemTelemetry()
    telemetry_data = telemetry_update(telemetry_data)

    with Live(get_telemetry_table(telemetry_data, width=75), refresh_per_second=Constants.Telemetry.UI_REFRESH_FREQUENCY) as live:
        while True:
            telemetry_data = telemetry_update(telemetry_data)
            time.sleep(Constants.Telemetry.UPDATE_FREQUENCY)
            live.update(get_telemetry_table(telemetry_data, width=52))