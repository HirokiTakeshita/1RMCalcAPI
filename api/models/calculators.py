"""Define a 1RM calculator model."""
from typing import Generator

from api import utils


class OneRepMaxCalculator:
    """The 1RM calculator model."""

    @staticmethod
    def get_one_rep_max_from_weight_and_reps(weight: float, reps: int) -> int:
        """Return the 1RM calculated from weight and reps.

        Reference:
            Brzycki, M. (1993). Strength testing—Predicting a one-rep max
            from reps-to-fatigue. Journal of Physical Education,
            Recreation and Dance, 64(1), 88–90.
            https://doi.org/10.1080/07303084.1993.10606684

        Args:
            weight (float):
            reps (int):

        Returns:
            int: one_rep_max
        """
        return utils.get_round_off_value(weight / (1.0278 - 0.0278 * reps))

    @staticmethod
    def get_weights_from_each_percentage_of_1rm(
        one_rep_max: int,
    ) -> Generator[dict[str, int], None, None]:
        """Returns each weight (95% -> 20% of 1RM: 5% intervals).

        Args:
            one_rep_max (int):

        Yields:
            dict[str, int]: {"percentage": x, "weight": y}
        """
        for percentage in reversed(range(20, 100, 5)):
            weight = utils.get_round_off_value(one_rep_max * percentage / 100)
            yield {"percentage": percentage, "weight": weight}
