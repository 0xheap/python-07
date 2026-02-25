import re

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losses = 0
        self.rating = 1000

    # --- From Card Interface ---
    def play(self, game_state: dict) -> dict:
        return {}
    # --- From Combatable Interface ---
    def attack(self, target) -> dict:
        return {}
        
    def defend(self, incoming_damage: int) -> dict:
        return {}
    
    def get_combat_stats(self) -> dict:
        return {}

    # --- From Rankable Interface ---
    def calculate_rating(self) -> int:
        if self.wins + self.losses == 0:
            return 1000
        win_ratio = self.wins / (self.wins + self.losses)
        return int(1000 + (win_ratio * 100))  # Simple rating calculation
        
    def update_wins(self, wins: int) -> None:
        self.wins += wins
        
    def update_losses(self, losses: int) -> None:
        self.losses += losses
        
    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }


    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "win_ratio": self.wins / (self.wins + self.losses) if (self.wins + self.losses) > 0 else 0
        }