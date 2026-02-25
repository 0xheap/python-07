"""TournamentCard - Enhanced card class (ex4)."""

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A powerful card implementing multiple interfaces for tournaments."""

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        rating: int = 1200
    ) -> None:
        """Initialize all components from the base classes."""
        # Note: Card __init__ handles name, cost, rarity
        super().__init__(name, cost, rarity)
        self.id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0

    # From Card
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the card."""
        return {"action": "play", "card": self.name}

    # From Combatable
    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target."""
        return {"attacker": self.name, "target": str(target)}

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Defend from damage."""
        return {"defender": self.name, "damage_taken": incoming_damage}

    def get_combat_stats(self) -> dict[str, Any]:
        """Returns dummy combat stats."""
        return {"attack": 0, "health": 0}

    # From Rankable
    def calculate_rating(self) -> int:
        """Return the current tournament rating."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Add to total wins."""
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Add to total losses."""
        self.losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        """Return ranking details."""
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    # Class specific method
    def get_tournament_stats(self) -> dict[str, Any]:
        """Return general tournament statistics."""
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
        }
