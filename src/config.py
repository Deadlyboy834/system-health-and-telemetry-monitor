from typing import Final, Any
from src.utils.file_io import get_config

CONFIG_DICT: dict[str, Any] = get_config()

class Telemetry:
    TELEMETRY_DICT: Final[dict[str, Any]] = CONFIG_DICT["telemetry"]

    UPDATE_FREQUENCY: Final[float | int] = TELEMETRY_DICT["update_frequency"]        # seconds
    UI_REFRESH_FREQUENCY: Final[float | int] = TELEMETRY_DICT["ui_refresh_frequency"]   # refreshes per second
    HEADERS: Final[dict[str, str]] = TELEMETRY_DICT["headers"]
    SYSTEM_HEADERS: Final[list[str]] = list[str](HEADERS.keys())
    USER_HEADERS: Final[list[str]] = list[str](HEADERS.values())

class ResourceUsageLevels:
    NORMAL: Final[str] = "NORMAL"
    WARNING: Final[str] = "WARNING"
    CRITICAL: Final[str] = "CRITICAL"