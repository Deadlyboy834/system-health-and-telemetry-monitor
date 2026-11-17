from typing import Final

class Constants:
    class Telemetry:
        UPDATE_FREQUENCY: Final[float | int] = 1        # seconds
        UI_REFRESH_FREQUENCY: Final[float | int] = 10   # refreshes per second
    class ResourceUsageLevels:
        NORMAL: Final[str] = "NORMAL"
        WARNING: Final[str] = "WARNING"
        CRITICAL: Final[str] = "CRITICAL"