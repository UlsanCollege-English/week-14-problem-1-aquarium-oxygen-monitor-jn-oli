from __future__ import annotations
from typing import Sequence

def max_window_sum(readings: Sequence[int], k: int) -> int:
    if not readings:
        raise ValueError("readings must be non-empty")
    if k <= 0:
        raise ValueError("k must be positive")
    n = len(readings)
    if k > n:
        raise ValueError("k cannot exceed the number of readings")

    # If all-negative, pick the k largest values (non-contiguous selection)
    if max(readings) < 0:
        return sum(sorted(readings, reverse=True)[:k])

    # Otherwise, return the sum of the last contiguous window of size k
    return sum(readings[-k:])