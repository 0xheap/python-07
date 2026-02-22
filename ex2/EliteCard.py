"""Elite card: Card + Combatable + Magical (multiple inheritance)."""

from typing import Any

from ex0.Card import Card

from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Card with combat and magic. Implements all abstract methods."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
        base_mana: int = 0,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self._attack = attack
        self._defense = defense
        self._mana = base_mana

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Describe playing this elite card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card summoned with combat and magic",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """Resolve combat attack."""
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self._attack,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Resolve defense: block up to defense, take the rest."""
        blocked = min(self._defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """Return combat stats."""
        return {
            "attack": self._attack,
            "defense": self._defense,
        }

    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict[str, Any]:
        """Resolve casting a spell (reports mana_used; logic is simple)."""
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Add mana. Return channeled amount and new total."""
        self._mana += amount
        return {
            "channeled": amount,
            "total_mana": self._mana,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        """Return current mana."""
        return {"mana": self._mana}
