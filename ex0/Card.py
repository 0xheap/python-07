"""Abstract base class for all DataDeck cards."""

from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    """Universal card blueprint. All card types must inherit and implement play()."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Execute playing this card. Subclasses must implement."""
        ...

    def get_card_info(self) -> dict[str, Any]:
        """Return common card fields."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """True if this card can be played with the given mana."""
        return available_mana >= self.cost
