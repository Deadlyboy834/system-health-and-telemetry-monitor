import math

def rational(x: float | int, y: float | int, z: float | int) -> float | int:
    return z * x / (y - x)

def power(p: float | int, x: float | int, y: float | int, z: float | int) -> float | int:
    return y * (x / z) ** p

def exponential(x: float | int, a: float | int, b: float | int, c: float | int, k: float | int):
    return a * (math.e ** (k * x) - c) / (math.e ** (b * k) - c)