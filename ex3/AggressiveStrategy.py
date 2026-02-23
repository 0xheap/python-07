# AggressiveStrategy - Concrete strategy (ex3)
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def __init__(self):
        ...
    
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...
    
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        ...