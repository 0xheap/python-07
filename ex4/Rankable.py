"""Rankable - Simple ranking interface (ex4)."""

from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    """Interface for ranking and recording tournament stats."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Return the current rating."""
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins."""
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses."""
        ...

    @abstractmethod
    def get_rank_info(self) -> dict[str, Any]:
        """Return ranking information as a dictionary."""
        ...
