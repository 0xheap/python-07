"""AggressiveStrategy - Concrete strategy (ex3)."""

from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Simple aggressive strategy: play cheap damage-focused cards first."""

    def __init__(self, mana_budget: int = 10) -> None:
        self._mana_budget = mana_budget

    def execute_turn(
        self, hand: list[Card], battlefield: list[Any]
    ) -> dict[str, Any]:
        """
        Play low-cost cards from hand until mana budget is used.
        """
        sorted_hand = sorted(hand, key=self._card_cost)

        mana_used = 0
        cards_played: list[str] = []
        damage_dealt = 0

        prioritized = self.prioritize_targets(battlefield)
        primary_target = prioritized[0] if prioritized else "Enemy Player"

        for card in sorted_hand:
            if mana_used + card.cost > self._mana_budget:
                continue

            mana_used += card.cost
            cards_played.append(card.name)

            if isinstance(card, CreatureCard):
                damage_dealt += card.attack
            elif isinstance(card, SpellCard):
                damage_dealt += card.cost

        targets_attacked = [primary_target] if damage_dealt > 0 else []

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    @staticmethod
    def _card_cost(card: Card) -> int:
        """Helper used as sort key."""
        return card.cost

    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Prioritize the enemy player if present, otherwise keep original order.
        """
        if "Enemy Player" in available_targets:
            other_targets = [
                t for t in available_targets if t != "Enemy Player"
            ]
            return ["Enemy Player"] + other_targets
        return available_targets
