def classify(cpu: float | int, ram: float | int, disk: float | int) -> int:
    from math import floor
    import src.utils.math_models as m

    cpu_gain: float | int
    ram_gain: float | int
    disk_gain: float | int
    raw_status_sum: float | int

    # TODO: Use values from config.py instead of magic numbers
    def normalize_cpu() -> float | int:
        return m.exponential(cpu, a=350, k=3) / 100

    def normalize_ram() -> float | int:
        return m.exponential(ram, a=400, k=3) / 100

    def normalize_disk() -> float | int:
        return m.exponential(disk, a=500, k=3.5) / 100

    cpu_gain = normalize_cpu()
    ram_gain = normalize_ram()
    disk_gain = normalize_disk()
    raw_status_sum = floor(cpu_gain + ram_gain + disk_gain)

    return 3 if raw_status_sum >= 6 else 2 if raw_status_sum >= 3 else 1