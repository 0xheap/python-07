"""Exercise 0: Card Foundation — demonstration script."""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    print(f"Play result: {dragon.play({'mana': available_mana})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
