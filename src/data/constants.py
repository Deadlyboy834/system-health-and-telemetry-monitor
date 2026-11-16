from typing import Final

class Constants:
    class Telemetry:
        UPDATE_FREQUENCY: Final[float | int] = 1    # seconds
    class ResourceUsageLevels:
        NORMAL: Final[str] = "NORMAL"
        WARNING: Final[str] = "WARNING"
        CRITICAL: Final[str] = "CRITICAL"