"""Concrete creature card implementation."""

from typing import Any

from ex0.Card import Card, CardType


class CreatureCard(Card):
    """Creature card with attack and health. Validates positive integers."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Describe playing this creature."""
        available_mana = game_state.get('mana', 0)
        if not self.is_playable(available_mana):
            return {
                'error': 'Not enough mana to play this card.',
                'playable': False
            }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def get_card_info(self) -> dict[str, Any]:
        """Base card info plus creature type, attack, and health."""
        info = super().get_card_info()
        info["type"] = CardType.CREATURE.value
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target: Any) -> dict[str, Any]:
        """Resolve this creature attacking a target."""
        return {
            "attacker": self.name,
            "target": str(target),
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
