# FantasyCardFactory - Concrete factory (ex3)
from ex3.CardFactory import CardFactory, Card
import random

class FantasyCardFactory(CardFactory):
    def __init__(self):
        ...

    def create_creature(self,
                        name_or_power: str | int | None = None
                        ) -> Card:
        creature = {
            'dragon': {
                'name': 'Fire Dragon',
                'cost': 5, 'rarity': 'Legendary',
                'type': 'Creature', 'attack': 7, 'health': 5
                },
            'goblin': {}
        }
        Cards = ["dragon", "goblin"]
        choice =  random.choice(Cards)
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
