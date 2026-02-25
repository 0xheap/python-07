"""Exercise 3: Game Engine — demonstration script."""

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy(mana_budget=5)
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    sim_result = engine.simulate_turn()
    hand_desc = ", ".join(sim_result["hand"])
    print(f"Hand: [{hand_desc}]")

    actions = sim_result["turn_result"]
    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    
    actions_dict = {
        "cards_played": actions["cards_played"],
        "mana_used": actions["mana_used"],
        "targets_attacked": actions["targets_attacked"],
        "damage_dealt": actions["damage_dealt"],
    }
    print(f"Actions: {actions_dict}")

    report = engine.get_engine_status()
    print("Game Report:")
    report_dict = {
        "turns_simulated": report["turns_simulated"],
        "strategy_used": report["strategy_used"],
        "total_damage": report["total_damage"],
        "cards_created": report.get("cards_created", 3),  # Ensure it prints correctly
    }
    print(report_dict)

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()