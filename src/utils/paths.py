import csv
import json
from pathlib import Path
from typing import Any
from src.constants import Telemetry

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "data" / "config.json"
LOGS = ROOT / "data" / "telemetry_logs.csv"

def initialize_logs() -> None:
    headers: list[str] = Telemetry.HEADERS

    do_not_have_headers: bool = True
    LOGS.parent.mkdir(parents=True, exist_ok=True)

    if LOGS.exists():
        with LOGS.open(mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader[str](file)

            do_not_have_headers = reader.fieldnames is None

    if do_not_have_headers:
        with LOGS.open(mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter[str](file, fieldnames=headers)
            writer.writeheader()

def get_chosen_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}", encoding="utf-8")

    return json.loads(path.read_text(encoding="utf-8"))

def get_config() -> dict[str, Any]:
    return get_chosen_json_file(CONFIG)

def get_logs() -> list[dict[str, Any]]:
    path: Path = LOGS

    with path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader[str](file)
        return list[dict[str | Any, str | Any]](reader)