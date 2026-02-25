"""Exercise 1: Deck Builder — demonstration script."""

from ex0.CreatureCard import CreatureCard

from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")
    game_states = {'mana': 10}
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    artifact = ArtifactCard(
        "Mana Crystal",
        2,
        "Rare",
        3,
        "Permanent: +1 mana per turn"
    )
    deck.add_card(artifact)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        card_type = "Creature" if isinstance(card, CreatureCard) else (
            "Spell" if isinstance(card, SpellCard) else "Artifact"
        )
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play(game_states)}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
