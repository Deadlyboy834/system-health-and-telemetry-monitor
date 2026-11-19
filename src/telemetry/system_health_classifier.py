def classify(cpu: float | int, ram: float | int, disk: float | int):
    import src.utils.math_models as m

    cpu_gain: float | int
    ram_gain: float | int
    disk_gain: float | int

    def normalize_cpu() -> float | int:
        return m.rational(cpu, y=100, z=100)

    def normalize_ram() -> float | int:
        return m.rational(ram, y=100, z=100)

    def normalize_disk() -> float | int:
        return m.rational(disk, y=100, z=100)

    cpu_gain = normalize_cpu()
    ram_gain = normalize_ram()
    disk_gain = normalize_disk()

    return cpu_gain + ram_gain + disk_gain