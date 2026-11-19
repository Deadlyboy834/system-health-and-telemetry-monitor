import csv
import json
from pathlib import Path
from typing import Any, Collection

from src.utils.paths import CONFIG, LOGS

def _get_chosen_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}", encoding="utf-8")

    return json.loads(path.read_text(encoding="utf-8"))

def get_config() -> dict[str, Any]:
    return _get_chosen_json_file(CONFIG)

def update_config(new_config: dict[str, Any]) -> None:
    with CONFIG.open(mode="w", encoding="utf-8") as file:
        json.dump(new_config, file, indent=4)

def get_logs() -> list[dict[str, Any]]:
    path: Path = LOGS

    with path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader[str](file)
        return list[dict[str | Any, str | Any]](reader)

def initialize_headers(headers: Collection[str]) -> None:
    with LOGS.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter[str](file, fieldnames=headers)
        writer.writeheader()

def update_logs(data: dict[str, Any], headers: Collection[str]) -> None:
    with LOGS.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter[str](file, fieldnames=headers).writerow(data)