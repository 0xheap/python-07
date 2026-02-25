# DataDeck Project - Evaluation Guidelines

This document serves as a guide for evaluating the DataDeck project (Module 07). It outlines the core objectives, key areas to check, and specific questions or criteria to assess the student's understanding and implementation of Advanced Object-Oriented Programming concepts in Python.

## Core Objectives
This module focuses on:
- **Abstract Base Classes (ABCs)** and Interfaces.
- **Multiple Inheritance** and Method Resolution Order (MRO).
- **Polymorphism** and Duck Typing.
- **Design Patterns** (Strategy, Abstract Factory).
- **Clean Code Practices** (Type hinting, `flake8` compliance, Docstrings).

## Preliminary Checks
Before exploring the code, ensure the following basic requirements are met:
1.  **No External Libraries:** The project must rely solely on Python's standard libraries (`abc`, `typing`, `enum`, `random`, etc.).
2.  **`flake8` Compliance:** Run `flake8 ex0/ ex1/ ex2/ ex3/ ex4/`. There should be zero errors or warnings.
3.  **Execution:** Run `python3 -m exX.main` (where X is 0-4) from the repository root. All scripts must execute without errors and produce expected output demonstrating the concepts.
4.  **Type Hinting:** Look for strict and correct type hinting (`-> None`, `-> dict[str, Any]`, etc.) across all files.

---

## Exercise 0: Card Foundation (ABCs and Enums)
**Goal:** Establish the foundational abstract class and basic card types.

### What to Look For:
- **`Card` Class:**
    - Must inherit from `abc.ABC`.
    - Must define at least one `@abstractmethod` (e.g., `play()`).
    - Should encapsulate common properties (name, cost, rarity).
- **`CardType` Enum:**
    - Usage of `enum.Enum` for defining card types (Creature, Spell, Artifact).
- **`CreatureCard` Class:**
    - Must inherit from `Card` and implement the `play()` method correctly.
    - Should demonstrate overriding or adding specific attributes (like `attack`, `health`).

### Questions for the Student:
- Why do we use Abstract Base Classes (`ABC`) instead of a normal parent class?
- What happens if you try to instantiate the `Card` class directly?
- How does the `CardType` enum improve code safety compared to using plain strings?

---

## Exercise 1: Deck Builder (Polymorphism)
**Goal:** Demonstrate polymorphism by treating different card types uniformly.

### What to Look For:
- **`SpellCard` and `ArtifactCard`:** Correctly inherit from `Card` and implement `play()`.
- **`Deck` Class:**
    - Contains a list of `Card` objects (type hinted as `list[Card]`).
    - `add_card()` and `draw()` methods work seamlessly regardless of whether a Creature, Spell, or Artifact is passed.
    - Uses `isinstance()` correctly in `get_deck_stats()` if calculating specific type totals.

### Questions for the Student:
- Explain what polymorphism is in the context of your `Deck` class.
- Why does the `Deck` class not need to know the specific subclass (Creature, Spell) when calling a card's `play()` method?

---

## Exercise 2: Ability System (Multiple Inheritance & Interfaces)
**Goal:** Implement multiple inheritance using abstract interfaces.

### What to Look For:
- **Interfaces (`Combatable`, `Magical`):**
    - These should be ABCs acting purely as interfaces (only defining abstract methods, no concrete state or logic).
- **`EliteCard` Class:**
    - Must inherit from `Card`, `Combatable`, and `Magical`.
    - Must provide concrete implementations for all required abstract methods from all parent interfaces.

### Questions for the Student:
- How does Python handle Method Resolution Order (MRO)? You can ask them to run or show `EliteCard.__mro__`.
- What are the risks of multiple inheritance (e.g., the Diamond Problem) and how does Python's `super()` resolve it?
- Why is it beneficial to separate `Combatable` and `Magical` into distinct interfaces rather than cramming them into the base `Card` class?

---

## Exercise 3: Game Engine (Design Patterns)
**Goal:** Apply the Abstract Factory and Strategy patterns.

### What to Look For:
- **Abstract Factory (`CardFactory` -> `FantasyCardFactory`):**
    - Identifiable factory methods that return instances of `Card` subclasses based on input.
    - Abstract parent factory and a concrete implementation.
- **Strategy Pattern (`GameStrategy` -> `AggressiveStrategy`):**
    - An abstract strategy interface with an `execute_turn()` method.
    - At least one concrete strategy implemented.
- **`GameEngine` Class:**
    - Takes instances of the Factory and Strategy via composition (e.g., injected into `__init__` or a setter method).
    - Delegates turn logic to the strategy and card creation to the factory.

### Questions for the Student:
- Explain the Strategy Pattern. How would adding a `DefensiveStrategy` impact the `GameEngine` code? (Answer: It shouldn't impact the engine logic at all).
- Explain the Abstract Factory Pattern. Why is it used here instead of directly instantiating cards in the engine?
- Describe the difference between Composition (used in `GameEngine`) and Inheritance.

---

## Exercise 4: Tournament Platform (Integration)
**Goal:** Combine all learned concepts into a final system.

### What to Look For:
- **`TournamentCard` Class:**
    - Implements multiple interfaces (`Card`, `Combatable`, `Rankable`).
    - Uses `super().__init__(...)` appropriately.
- **`TournamentPlatform` Class:**
    - Manages collections of `TournamentCard` objects.
    - Correctly simulates matches and updates ranks/stats.
    - Functional `get_leaderboard()` returning sorted data without errors.
- **Overall Cohesion:**
    - Clean structure, good separation of concerns, and robust encapsulation (using `_` for private attributes where suitable).

### Questions for the Student:
- How did the use of interfaces make creating the `TournamentCard` easier?
- Walk me through the `main.py` script for Exercise 4. Explain how the platform interacts with the cards.

---

## Final Review
Give the student appropriate feedback on code readability, proper use of docstrings, handling of edge cases, and overall architectural design.
