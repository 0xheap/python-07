"""Exercise 2: Ability System — demonstration script."""

from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    card = EliteCard(
        "Arcane Warrior", 4, "Legendary", attack=5, defense=3, base_mana=4
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    print(f"Play result: {card.play({'mana': 10})}")

    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
    print(
        "How do multiple interfaces enable flexible card design? What are"
        "\nthe advantages of separating combat and magic concerns?"
    )


if __name__ == "__main__":
    main()
