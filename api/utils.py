"""Define helper functions."""
from decimal import Decimal, ROUND_HALF_UP


def get_round_off_value(num: float) -> int:
    """Receive a float value and return a rounded-off value.

    Args:
        num (float):

    Returns:
        int: rounded_off_value
    """
    return int(Decimal(num).quantize(0, ROUND_HALF_UP))
