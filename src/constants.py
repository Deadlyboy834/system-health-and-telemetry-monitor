from typing import Final

class Constants:
    class Telemetry:
        UPDATE_FREQUENCY: Final[float | int] = 1    # seconds
    class ResourceUsageLevels:
        NORMAL: Final[str] = "NORMAL"
        WARNING: Final[str] = "WARNING"
        CRITICAL: Final[str] = "CRITICAL"

        class Thresholds:
            NORMAL: Final[tuple[int, int]] = (0, 100)
            WARNING: Final[tuple[int, int]] = (100, 200)
            CRITICAL: Final[tuple[int, int]] = (200, 300)

