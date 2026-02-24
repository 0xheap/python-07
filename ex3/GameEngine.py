"""GameEngine - Game orchestrator (ex3)."""

from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Configure a factory and strategy, then simulate turns."""

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns_simulated = 0
        self._total_damage = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """Set the card factory and strategy used by the engine."""
        self._factory = factory
        self._strategy = strategy
        self._turns_simulated = 0
        self._total_damage = 0

    def simulate_turn(self) -> dict[str, Any]:
        """Create a hand using the factory and execute a single aggressive turn."""
        if self._factory is None or self._strategy is None:
            raise ValueError("Engine is not configured with factory and strategy")

        hand = [
            self._factory.create_creature("dragon"),
            self._factory.create_creature("goblin"),
            self._factory.create_spell("lightning_bolt"),
        ]
        battlefield: list[Any] = []

        result = self._strategy.execute_turn(hand, battlefield)

        self._turns_simulated += 1
        damage = int(result.get("damage_dealt", 0))
        self._total_damage += damage

        return {
            "hand": [f"{c.name} ({c.cost})" for c in hand],
            "turn_result": result,
        }

    def get_engine_status(self) -> dict[str, Any]:
        """Return a simple engine status report."""
        strategy_name = self._strategy.get_strategy_name() if self._strategy else None
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
        }

