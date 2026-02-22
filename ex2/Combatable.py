"""Abstract combat interface."""

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """Interface for combat: attack, defend, combat stats."""

    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target. Returns result dict."""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Defend against damage. Returns result dict."""
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        """Return combat-related stats."""
        ...
