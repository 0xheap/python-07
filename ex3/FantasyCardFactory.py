"""FantasyCardFactory - Concrete factory (ex3)."""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed creatures, spells, and artifacts."""

    def __init__(self) -> None:
        self._supported_types = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a fantasy creature: dragon or goblin."""
        creatures: dict[str, CreatureCard] = {
            "dragon": CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
            "goblin": CreatureCard("Goblin Warrior", 2, "Common", 5, 1),
        }
        names = list(creatures.keys())

        if isinstance(name_or_power, int):
            if name_or_power >= 5:
                return creatures["dragon"]
            return creatures["goblin"]

        if name_or_power is None:
            return creatures[random.choice(names)]

        return creatures.get(str(name_or_power), creatures["goblin"])

    def create_spell(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create an elemental spell (Fireball or Lightning Bolt)."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key == "fireball":
                return SpellCard("Fireball", 4, "Rare", "damage")
            if key == "lightning_bolt" or key == "lightning bolt":
                return SpellCard("Lightning Bolt", 3, "Common", "damage")

        if isinstance(name_or_power, int) and name_or_power >= 4:
            return SpellCard("Fireball", 4, "Rare", "damage")

        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a magical artifact (e.g. Mana Ring)."""
        # USE the parameter to satisfy flake8!
        artifact_name = "Mana Ring"
        if isinstance(name_or_power, str) and name_or_power:
            artifact_name = name_or_power.replace("_", " ").title()

        return ArtifactCard(
            artifact_name,
            2,
            "Rare",
            durability=3,
            effect="Permanent: +1 mana per turn",
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Create a small themed deck with the requested size.

        Mix creatures, spells, and artifacts using this factory.
        """
        cards: list[Card] = []
        creators = [
            self.create_creature,
            self.create_spell,
            self.create_artifact,
        ]

        for i in range(size):
            creator = creators[i % len(creators)]
            cards.append(creator(None))

        return {
            "cards": cards,
            "size": size,
        }

    def get_supported_types(self) -> dict[str, Any]:
        return self._supported_types.copy()
