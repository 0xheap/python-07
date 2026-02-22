"""Deck management — add, remove, shuffle, draw, stats."""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard

from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    """Holds cards. Counts creatures, spells, artifacts for stats."""

    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove one card with the given name. Return True if removed."""
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Remove and return the top card. Raises if deck is empty."""
        if not self._cards:
            raise ValueError("Deck is empty")
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        """Return total_cards, creatures, spells, artifacts, avg_cost."""
        total = len(self._cards)
        creatures = sum(1 for c in self._cards if isinstance(c, CreatureCard))
        spells = sum(1 for c in self._cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self._cards if isinstance(c, ArtifactCard))
        total_cost = sum(c.cost for c in self._cards)
        avg_cost = total_cost / total if total else 0.0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1),
        }
