"""Exercise 4: Tournament Platform — demonstration script."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 1150)

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print("Ice Wizard (ID: wizard_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("Creating tournament match...")
    match_res = platform.create_match("dragon_001", "wizard_001")

    # We output the dict directly, though we enforce order to match expected
    ordered_match_res = {
        "winner": match_res["winner"],
        "loser": match_res["loser"],
        "winner_rating": match_res["winner_rating"],
        "loser_rating": match_res["loser_rating"]
    }
    print(f"Match result: {ordered_match_res}")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, c in enumerate(leaderboard, start=1):
        rating_info = f"{c.calculate_rating()} ({c.wins}-{c.losses})"
        print(f"{i}. {c.name} - Rating: {rating_info}")

    print("Platform Report:")
    rep = platform.generate_tournament_report()
    ordered_rep = {
        "total_cards": rep["total_cards"],
        "matches_played": rep["matches_played"],
        "avg_rating": rep["avg_rating"],
        "platform_status": rep["platform_status"]
    }
    print(ordered_rep)

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
