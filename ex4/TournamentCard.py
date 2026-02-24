# TournamentCard - Card + Combatable + Rankable (ex4)
from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Deploys the tournament card to the board.
        """
        # We check if it is playable using the inherited method from Card
        available_mana = game_state.get('mana', 0)
        
        if not self.is_playable(available_mana):
            return {
                'error': 'Not enough mana to play this card.',
                'playable': False
            }
        return {
                    'card_played': self.name,  
                    'mana_used': self.cost,    
                    'effect': 'Tournament card deployed to the battlefield',
                    'current_rating': self.calculate_rating()
                }