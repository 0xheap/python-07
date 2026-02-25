"""Spell card — instant magic effects (one-time use)."""

from typing import Any

from ex0.Card import Card


class SpellCard(Card):
    """Spell with effect_type (damage, heal, buff, debuff). Consumed when played."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
            """Describe playing this spell (one-time use)."""
            available_mana = game_state.get('mana', 0)
            
            if not self.is_playable(available_mana):
                return {
                    'error': 'Not enough mana to play this card.',
                    'playable': False
                }
                
            effect_msg = self._effect_description()
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": effect_msg,
            }
    def _effect_description(self) -> str:
        """Build effect string from effect_type and card name/cost."""
        if self.effect_type == "damage":
            return f"Deal {self.cost} damage to target"
        if self.effect_type == "heal":
            return f"Heal {self.cost} to target"
        if self.effect_type == "buff":
            return f"Buff target +{self.cost}"
        if self.effect_type == "debuff":
            return f"Debuff target -{self.cost}"
        return f"Spell: {self.effect_type}"

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        """Resolve the spell on the given targets."""
        return {
            "spell": self.name,
            "targets": targets,
            "effect_type": self.effect_type,
            "resolved": True,
        }
