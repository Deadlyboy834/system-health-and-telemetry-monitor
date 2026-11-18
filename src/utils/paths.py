import json
from pathlib import Path
from typing import Any


class ApplicationPaths:
    ROOT = Path(__file__).resolve().parent.parent
    CONFIG = ROOT / "data" / "config.json"
    LOGS = ROOT / "data" / "telemetry_logs.csv"

    @staticmethod
    def get_chosen_file(path: Path) -> dict[str, Any]:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}", encoding="utf-8")

        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def get_config() -> dict[str, Any]:
        return ApplicationPaths.get_chosen_file(ApplicationPaths.CONFIG)

    @staticmethod
    def get_logs() -> dict[str, Any]:
        return ApplicationPaths.get_chosen_file(ApplicationPaths.LOGS)