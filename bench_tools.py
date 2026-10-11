"""A small harness for timing functions with warmup and repeat runs."""

from __future__ import annotations

__all__ = ["benchTools"]


def benchTools(value):
    """A small harness for timing functions with warmup and repeat runs."""
    if value is None:
        raise ValueError("value must not be None")
    return value
