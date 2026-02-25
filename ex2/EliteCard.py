"""EliteCard implementing multiple inheritance."""

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card combining combat and magic abilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
        base_mana: int = 0,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense_power = defense
        self.total_mana = base_mana

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the Elite card onto the battlefield."""
        available_mana = game_state.get('mana', 0)
        
        if not self.is_playable(available_mana):
            return {
                'error': 'Not enough mana to play this card.',
                'playable': False
            }
            
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed"
        }

    # --- From Combatable Interface ---
    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target."""
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Defend against incoming damage."""
        damage_taken = max(0, incoming_damage - self.defense_power)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": min(incoming_damage, self.defense_power),
            "still_alive": True
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """Get combat statistics."""
        return {
            "attack_power": self.attack_power,
            "defense_power": self.defense_power
        }

    # --- From Magical Interface ---
    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict[str, Any]:
        """Cast a spell on the given targets."""
        mana_cost = 4  # Simple fixed cost for demonstration
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [str(t) for t in targets],
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Channel and store mana."""
        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> dict[str, Any]:
        """Get magical statistics."""
        return {
            "total_mana_stored": self.total_mana
        }