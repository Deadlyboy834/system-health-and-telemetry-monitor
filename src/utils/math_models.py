import math


def exponential(x: float | int, a: float | int, k: float | int):
    return a * (math.exp(k * x / 100) - 1) / (math.exp(k) - 1)