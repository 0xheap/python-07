"""Artifact card — permanent game modifiers."""

from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    """Permanent with durability and an effect. Stays in play until destroyed."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Describe playing this artifact (permanent)."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> dict[str, Any]:
        """Activate the artifact's ongoing ability."""
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
        }
