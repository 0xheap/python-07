# DataDeck — Concepts You Need Today

This README focuses on the **theory you actually need** to understand and defend this project. It is organized by concept, not by file.

---

## 1. Abstract Base Classes (ABC) and Interfaces

- **What problem they solve**: You want many different classes (Creature, Spell, Artifact, EliteCard, TournamentCard, etc.) to **share the same API** (same methods) while each one has its **own implementation**.
- **In Python**:
  - Use `from abc import ABC, abstractmethod`.
  - A class that inherits from `ABC` and has one or more `@abstractmethod`s is an **abstract base class**.
  - You **cannot instantiate** an abstract class until all abstract methods are implemented in a subclass.

**In this project:**

- `Card` is an **abstract base class**:
  - Defines the universal contract for all cards: `play`, `get_card_info`, `is_playable`.
  - You never use a raw `Card`; you use `CreatureCard`, `SpellCard`, `ArtifactCard`, `EliteCard`, `TournamentCard`, etc.
- `Combatable`, `Magical`, `Rankable`, `GameStrategy`, `CardFactory` are all **abstract interfaces**:
  - They define sets of methods that a class must implement (`attack`, `defend`, `cast_spell`, `calculate_rating`, `execute_turn`, `create_creature`, etc.).
  - They **do not** contain concrete behavior by themselves.

**Key idea to explain**:  
“Abstract classes and interfaces define **what** must exist (`play`, `attack`, `execute_turn`), while concrete classes decide **how** it works.”

---

## 2. Polymorphism

- **Definition**: Same method name, **different implementations**, chosen at **runtime** depending on the object’s concrete type.
- In practice, you write code against the **abstract type** (`Card`, `GameStrategy`, `CardFactory`), and Python chooses the correct method implementation for the **actual object**.

**In this project:**

- `Deck` stores a list of `Card` objects. It does **not care** if a card is `CreatureCard`, `SpellCard`, or `ArtifactCard`.
  - `draw_card()` returns `Card`.
  - `play()` is called on whatever card you drew; the correct `play` implementation runs.
- `GameEngine` holds a `GameStrategy` and a `CardFactory`:
  - You can swap `AggressiveStrategy` for another strategy without touching `GameEngine`.
  - You can swap `FantasyCardFactory` for another factory without touching `GameEngine`.

**Phrase for defense**:  
“Polymorphism lets my engine and deck **treat all cards the same** via the `Card` interface, while each card type can still behave differently when played.”

---

## 3. Multiple Inheritance as Interface Composition

- **Multiple inheritance** = a class inherits from **more than one base class**.
- Dangerous if misused, but here it is used only for **interfaces/ABCs**, which is a common and safe pattern.

**In this project:**

- `EliteCard(Card, Combatable, Magical)`:
  - Is a `Card` (can be played, has `get_card_info`, `is_playable`).
  - Is `Combatable` (has `attack`, `defend`, `get_combat_stats`).
  - Is `Magical` (has `cast_spell`, `channel_mana`, `get_magic_stats`).
- `TournamentCard(Card, Combatable, Rankable)`:
  - Is a `Card`, is `Combatable`, and is `Rankable` (has rating, wins, losses).

**Why it’s powerful here:**

- You can mix **orthogonal capabilities**:
  - Combat abilities (`Combatable`)
  - Magic abilities (`Magical`)
  - Ranking abilities (`Rankable`)
- Each interface is small and focused; you combine them like **Lego pieces**.

**What to say**:  
“Multiple inheritance here is used to **compose capabilities** (combat, magic, ranking) rather than to share state. Each interface stays small and clear.”

---

## 4. Strategy Pattern (Exercise 3)

- **Intent**: Encapsulate **“how to play a turn”** into a separate object, so you can switch strategies without touching the game engine.
- **Structure**:
  - `GameStrategy` (abstract):
    - `execute_turn(self, hand, battlefield) -> dict`
    - `get_strategy_name(self) -> str`
    - `prioritize_targets(self, available_targets) -> list`
  - `AggressiveStrategy` (concrete):
    - Implements `execute_turn` with an **aggressive** plan:
      - Sort/choose low-cost cards.
      - Favor creatures/damage spells.
      - Focus on dealing damage to `"Enemy Player"`.

**Why it matters**:

- `GameEngine` calls `strategy.execute_turn(...)` but does not know the details.
- You could easily add a `DefensiveStrategy` in the future without changing `GameEngine`.

**Short explanation**:  
“The Strategy pattern lets me plug in different **‘brains’** for the game (aggressive, defensive, etc.) without rewriting the engine.”

---

## 5. Abstract Factory Pattern (Exercise 3)

- **Intent**: Provide an interface to create **families of related objects** without specifying their concrete classes.
- **Structure**:
  - `CardFactory` (abstract):
    - `create_creature(...) -> Card`
    - `create_spell(...) -> Card`
    - `create_artifact(...) -> Card`
    - `create_themed_deck(size: int) -> dict`
    - `get_supported_types() -> dict`
  - `FantasyCardFactory` (concrete):
    - Actually creates **Dragons, Goblins, Fireballs, Lightning Bolts, Mana Crystals**, etc.

**Why it matters**:

- `GameEngine` asks the factory for cards but never touches `CreatureCard`, `SpellCard`, `ArtifactCard` directly.
- If you create a new factory (e.g. `SciFiCardFactory`), the engine code stays the same.

**Phrase to use**:  
“The Abstract Factory lets the engine create theme‑specific cards through a **single interface**, making it easy to switch whole card families.”

---

## 6. Combining Strategy + Abstract Factory

In Exercise 3, you are **supposed** to show these two patterns working together:

- `GameEngine` holds:
  - A `CardFactory` → **what cards exist**.
  - A `GameStrategy` → **how we use those cards**.
- Flow:
  1. Engine uses the factory to build a **hand** and possibly a **deck**.
  2. Engine passes that hand to the strategy’s `execute_turn`.
  3. Strategy decides which cards to play and how to attack.
  4. Engine aggregates results into a report.

**Key takeaway**:  
“Abstract Factory controls **what cards are created**, Strategy controls **how they are used**. The engine wires both together.”

---

## 7. Tournament & Ranking Concepts (Exercise 4)

Even if not fully coded yet, you should know the intent:

- `Rankable` interface:
  - `calculate_rating() -> int`
  - `update_wins(wins: int)`, `update_losses(losses: int)`
  - `get_rank_info() -> dict`
- `TournamentCard` combines:
  - `Card` + `Combatable` + `Rankable`
  - Tracks **wins, losses, rating**.
- `TournamentPlatform`:
  - `register_card(card) -> id`
  - `create_match(card1_id, card2_id) -> dict` (updates ratings)
  - `get_leaderboard() -> list`
  - `generate_tournament_report() -> dict`

**Conceptual idea**:

- You’re layering **meta‑information** (rating, record) on top of the card system.
- Multiple inheritance again: the same object is both a game unit **and** a ranked competitor.

---

## 8. Practical Python Concepts You’re Using

- **Type hints**: `list[Card]`, `dict[str, Any]`, `name_or_power: str | int | None`.
  - They make contracts clearer and help tools (linters, IDE) catch mistakes.
- **In‑memory design**: No file I/O; everything is kept in Python objects (lists, dicts, classes).
- **No lambdas / simple functions**: Where lambdas are forbidden, you can always replace them with a small named function or `@staticmethod` used as a key.

---

## 9. How to Explain This Project in a Few Sentences

You can summarize your work like this:

> “I built a modular trading card engine using Python’s abstract base classes and interfaces.  
> All card types share a common `Card` interface, and extra behaviors like combat, magic, and ranking are composed via multiple inheritance (`Combatable`, `Magical`, `Rankable`).  
> On the engine side, I used the **Strategy pattern** to encapsulate different turn‑playing behaviors (`GameStrategy`) and the **Abstract Factory pattern** to generate themed cards (`CardFactory`).  
> Together, these patterns make it easy to add new card families and strategies without changing the engine or deck code.”

If you can comfortably explain everything in this README, you’re conceptually ready for the exercises you worked on today.

