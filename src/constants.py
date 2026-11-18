from typing import Final, Any
from src.utils.paths import ApplicationPaths

class Constants:
    CONFIG_DICT: dict[str, Any] = ApplicationPaths.get_config()
    LOGS_DICT: dict[str, Any] = ApplicationPaths.get_logs()

class Telemetry:
    UPDATE_FREQUENCY: Final[float | int] = Constants.CONFIG_DICT["update_frequency"]        # seconds
    UI_REFRESH_FREQUENCY: Final[float | int] = Constants.LOGS_DICT["ui_refresh_frequency"]   # refreshes per second
class ResourceUsageLevels:
    NORMAL: Final[str] = "NORMAL"
    WARNING: Final[str] = "WARNING"
    CRITICAL: Final[str] = "CRITICAL"