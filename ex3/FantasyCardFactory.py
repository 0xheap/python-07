# FantasyCardFactory - Concrete factory (ex3)
from ex3.CardFactory import CardFactory, Card
from ex0.CreatureCard import CreatureCard
import random

class FantasyCardFactory(CardFactory):
    def __init__(self):
        ...

    def create_creature(self,
                        name_or_power: str | int | None = None
                        ) -> Card:
        creature = {
            'dragon': CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
            'goblin': CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        }
        Cards = ["dragon", "goblin"]
        if isinstance(name_or_power, int) or name_or_power is None:
            if name_or_power == 5:
                return creature['dragon']
            elif name_or_power == 2:
                return creature['goblin']
            else:
                return creature[random.choice[Cards]]
        return creature[name_or_power]

    def create_spell(self,
                     name_or_power: str | int | None = None
                     ) -> Card:
        ...

    def create_artifact(self,
                            name_or_power: str | int | None = None
                            ) -> Card:
        ...

    def create_themed_deck(self, size: int) -> dict:
        ...

    def get_supported_types(self) -> dict:
        ...
