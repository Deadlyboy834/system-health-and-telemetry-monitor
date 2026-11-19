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
    USAGE_LEVELS_DICT: Final[dict[str, str]] = CONFIG_DICT["resource_usage_levels"]

    NORMAL: Final[str] = USAGE_LEVELS_DICT["normal"]
    WARNING: Final[str] = USAGE_LEVELS_DICT["warning"]
    CRITICAL: Final[str] = USAGE_LEVELS_DICT["critical"]

class WarningThresholds:
    WARNING_THRESHOLDS_DICT: Final[dict[str, list[int]]] = CONFIG_DICT["warning_thresholds"]

    NORMAL: Final[tuple[int]] = tuple(WARNING_THRESHOLDS_DICT["normal"])
    WARNING: Final[tuple[int]] = tuple(WARNING_THRESHOLDS_DICT["warning"])
    CRITICAL: Final[tuple[int]] = tuple(WARNING_THRESHOLDS_DICT["critical"])