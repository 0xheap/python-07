"""AggressiveStrategy - Concrete strategy (ex3)."""

from typing import Any

from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    """Simple aggressive strategy: play cheap damage-focused cards first."""

    def __init__(self, mana_budget: int = 10) -> None:
        self._mana_budget = mana_budget

    def execute_turn(self, hand: list[Card], battlefield: list[Any]) -> dict[str, Any]:
        """
        Play low-cost cards from hand until mana budget is used.

        - Prefer cheaper cards first (board presence).
        - Treat creatures and damage spells as sources of damage.
        """
        sorted_hand = sorted(hand, key=self._card_cost)

        mana_used = 0
        cards_played: list[str] = []
        damage_dealt = 0

        for card in sorted_hand:
            if mana_used + card.cost > self._mana_budget:
                continue
            mana_used += card.cost
            cards_played.append(card.name)

            if isinstance(card, CreatureCard):
                damage_dealt += card.attack
            elif isinstance(card, SpellCard):
                damage_dealt += card.cost

        targets_attacked = ["Enemy Player"] if damage_dealt > 0 else []

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    @staticmethod
    def _card_cost(card: Card) -> int:
        """Helper used as sort key; no lambdas per constraints."""
        return card.cost

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Prioritize enemy player if present, otherwise keep original order.
        """
        if "Enemy Player" in available_targets:
            return ["Enemy Player"] + [t for t in available_targets if t != "Enemy Player"]
        return available_targets
