# DataDeck — Implementation Guideline

This document defines **what each method must do** so you can implement without guessing. Use it as the single source of truth for behavior and return shapes. Subject gives signatures; this gives the contract.

---

## General rules (all exercises)

- **Python 3.10+**, **type hints** on all functions/methods, **flake8** compliant.
- **Authorized imports:** `abc`, `typing`, `random`, `enum`, `datetime`, stdlib only. No file I/O, no `eval`/`exec`.
- **Exceptions:** Handle invalid inputs gracefully (e.g. raise `ValueError` with a clear message, or return a safe default where it makes sense). Don’t crash.
- **Run from repo root:** `python3 -m ex0.main`, `python3 -m ex1.main`, etc.
- **Imports:** Use absolute imports only: `from ex0.Card import Card`, never `from ..ex0.Card import Card`.

---

## Exercise 0 — Card Foundation (`ex0/`)

### `Card` (abstract base class in `Card.py`)

- **Inherit from:** `ABC` (from `abc`).
- **Abstract method:** `play(self, game_state: dict) -> dict` — subclasses must implement it.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `__init__(self, name: str, cost: int, rarity: str)` | Store `name`, `cost`, `rarity` as instance attributes. No validation required at this level (concrete classes can add their own). | — |
| `play(self, game_state: dict) -> dict` | **Abstract.** No implementation in `Card`; only the signature. Concrete classes return a dict describing the play. | Subclasses return a dict (see `CreatureCard.play`). |
| `get_card_info(self) -> dict` | **Concrete.** Return a dict with at least the common card fields. | `{"name": str, "cost": int, "rarity": str}`. Subclasses extend it (e.g. `"type"`, `"attack"`, `"health"`). |
| `is_playable(self, available_mana: int) -> bool` | **Concrete.** True if the card can be played with the given mana. | `True` if `available_mana >= self.cost`, else `False`. |

**Note:** `game_state` can be any dict (e.g. `{"mana": 6}`). You are not required to read specific keys; the point is the **interface**. Concrete classes can use it to build their return dict.

---

### `CreatureCard` (concrete in `CreatureCard.py`)

- **Inherit from:** `Card`.
- **Extra attributes:** `attack`, `health` (both `int`).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `__init__(self, name, cost, rarity, attack, health)` | Call `super().__init__(name, cost, rarity)`. Store `attack` and `health`. | **Validation:** Raise `ValueError` if `attack` or `health` are not positive integers. |
| `play(self, game_state: dict) -> dict` | Describe playing this creature. | `{"card_played": self.name, "mana_used": self.cost, "effect": "Creature summoned to battlefield"}`. |
| `get_card_info(self) -> dict` | Same as base plus creature-specific fields. | Extend parent: add `"type": "Creature"`, `"attack": self.attack`, `"health": self.health`. |
| `attack_target(self, target) -> dict` | Resolve this creature attacking a target. `target` can be a string (e.g. creature name) or any object; use it for display. | `{"attacker": self.name, "target": str(target), "damage_dealt": self.attack, "combat_resolved": True}`. |

**Expected output (excerpt):**  
`get_card_info()` → `{'name': 'Fire Dragon', 'cost': 5, 'rarity': 'Legendary', 'type': 'Creature', 'attack': 7, 'health': 5}`  
`play(...)` → `{'card_played': 'Fire Dragon', 'mana_used': 5, 'effect': 'Creature summoned to battlefield'}`  
`attack_target("Goblin Warrior")` → `{'attacker': 'Fire Dragon', 'target': 'Goblin Warrior', 'damage_dealt': 7, 'combat_resolved': True}`

---

## Exercise 1 — Deck Builder (`ex1/`)

- **Import:** `from ex0.Card import Card`.

### `SpellCard` (`SpellCard.py`)

- **Inherit from:** `Card`.
- **Extra attribute:** `effect_type` (e.g. `"damage"`, `"heal"`, `"buff"`, `"debuff"`).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `__init__(self, name, cost, rarity, effect_type: str)` | Store attributes; call `super().__init__(name, cost, rarity)`. | — |
| `play(self, game_state: dict) -> dict` | Describe playing the spell (one-time use). | `{"card_played": self.name, "mana_used": self.cost, "effect": "<description>"}`. Description can depend on `effect_type` (e.g. damage → "Deal N damage to target"). |
| `resolve_effect(self, targets: list) -> dict` | Resolve the spell on the given targets. | Return a dict, e.g. `{"spell": self.name, "targets": targets, "effect_type": self.effect_type, "resolved": True}`. Keep it simple. |

**Expected (excerpt):**  
`play(...)` → `{'card_played': 'Lightning Bolt', 'mana_used': 3, 'effect': 'Deal 3 damage to target'}`

---

### `ArtifactCard` (`ArtifactCard.py`)

- **Inherit from:** `Card`.
- **Extra attributes:** `durability` (int), `effect` (str, e.g. permanent ability description).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `__init__(self, name, cost, rarity, durability: int, effect: str)` | Store attributes; call `super().__init__(name, cost, rarity)`. | — |
| `play(self, game_state: dict) -> dict` | Describe playing the artifact (permanent). | `{"card_played": self.name, "mana_used": self.cost, "effect": self.effect}` (e.g. `"Permanent: +1 mana per turn"`). |
| `activate_ability(self) -> dict` | Activate the artifact’s ongoing ability. | e.g. `{"artifact": self.name, "effect": self.effect, "durability_remaining": self.durability}`. Keep logic simple. |

**Expected (excerpt):**  
`play(...)` → `{'card_played': 'Mana Crystal', 'mana_used': 2, 'effect': 'Permanent: +1 mana per turn'}`

---

### `Deck` (`Deck.py`)

- **Holds:** A list (or similar) of `Card` instances. Use the **concrete type** of each card to count creatures/spells/artifacts (e.g. `CreatureCard`, `SpellCard`, `ArtifactCard` from your imports).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `add_card(self, card: Card) -> None` | Add the card to the deck. | No return. |
| `remove_card(self, card_name: str) -> bool` | Remove **one** card whose `name` equals `card_name`. | `True` if a card was removed, `False` if no such card. |
| `shuffle(self) -> None` | Shuffle the deck in place (e.g. `random.shuffle`). | No return. |
| `draw_card(self) -> Card` | Remove and return the **top** card. | The card. If deck is empty: raise a clear exception (e.g. `ValueError("Deck is empty")`) or document that behavior. |
| `get_deck_stats(self) -> dict` | Compute counts and average cost. | `{"total_cards": int, "creatures": int, "spells": int, "artifacts": int, "avg_cost": float}`. Count by type (isinstance). `avg_cost` = total cost of all cards / total_cards; 0 if no cards. |

**Expected (excerpt):**  
`get_deck_stats()` → `{'total_cards': 3, 'creatures': 1, 'spells': 1, 'artifacts': 1, 'avg_cost': 4.0}`

---

## Exercise 2 — Ability System (`ex2/`)

- **Imports:** `from ex0.Card import Card` in `EliteCard.py`.

### `Combatable` (abstract interface in `Combatable.py`)

- **Inherit from:** `ABC`.
- **Abstract methods:** `attack`, `defend`, `get_combat_stats`.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `attack(self, target) -> dict` | Abstract. No implementation. | — |
| `defend(self, incoming_damage: int) -> dict` | Abstract. No implementation. | — |
| `get_combat_stats(self) -> dict` | Abstract. No implementation. | — |

---

### `Magical` (abstract interface in `Magical.py`)

- **Inherit from:** `ABC`.
- **Abstract methods:** `cast_spell`, `channel_mana`, `get_magic_stats`.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `cast_spell(self, spell_name: str, targets: list) -> dict` | Abstract. No implementation. | — |
| `channel_mana(self, amount: int) -> dict` | Abstract. No implementation. | — |
| `get_magic_stats(self) -> dict` | Abstract. No implementation. | — |

---

### `EliteCard` (`EliteCard.py`)

- **Inherit from:** `Card`, `Combatable`, `Magical` (multiple inheritance). Implement **all** abstract methods from all three.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `__init__` | Store what’s needed for Card + combat + magic (e.g. name, cost, rarity, attack, defense, mana, spell names). | Call `Card.__init__(name, cost, rarity)` and set your extra attributes. |
| `play(self, game_state: dict) -> dict` | Same idea as other cards: describe playing this card. | e.g. `{"card_played": self.name, "mana_used": self.cost, "effect": "..."}`. |
| `attack(self, target) -> dict` | Resolve combat attack. | `{"attacker": self.name, "target": str(target), "damage": <int>, "combat_type": "melee"}`. |
| `defend(self, incoming_damage: int) -> dict` | Resolve defense (e.g. block part of damage). | `{"defender": self.name, "damage_taken": int, "damage_blocked": int, "still_alive": bool}`. Simple rule: e.g. block 3, take rest; or take all. |
| `get_combat_stats(self) -> dict` | Return combat-related stats. | e.g. `{"attack": int, "defense": int}` or similar. |
| `cast_spell(self, spell_name: str, targets: list) -> dict` | Resolve casting a spell. | `{"caster": self.name, "spell": spell_name, "targets": targets, "mana_used": int}`. |
| `channel_mana(self, amount: int) -> dict` | Channel mana (increase available mana). | `{"channeled": amount, "total_mana": int}` (e.g. track a mana attribute and add `amount`). |
| `get_magic_stats(self) -> dict` | Return magic-related stats. | e.g. `{"mana": int}` or similar. |

**Expected (excerpt):**  
Attack: `{'attacker': 'Arcane Warrior', 'target': 'Enemy', 'damage': 5, 'combat_type': 'melee'}`  
Defend: `{'defender': 'Arcane Warrior', 'damage_taken': 2, 'damage_blocked': 3, 'still_alive': True}`  
Cast: `{'caster': 'Arcane Warrior', 'spell': 'Fireball', 'targets': ['Enemy1', 'Enemy2'], 'mana_used': 4}`  
Channel: `{'channeled': 3, 'total_mana': 7}`

---

## Exercise 3 — Game Engine (`ex3/`)

- **Imports:** Use `ex0.Card`, `ex1.SpellCard`, `ex1.ArtifactCard`, `ex1.Deck`, etc., as needed.

### `GameStrategy` (abstract in `GameStrategy.py`)

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `execute_turn(self, hand: list, battlefield: list) -> dict` | Abstract. No implementation. | — |
| `get_strategy_name(self) -> str` | Abstract. No implementation. | — |
| `prioritize_targets(self, available_targets: list) -> list` | Abstract. No implementation. | — |

---

### `CardFactory` (abstract in `CardFactory.py`)

- **Signature:** `name_or_power` can be `str | int | None = None` (for flexibility: name string, power level int, or None for default).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `create_creature(self, name_or_power: str \| int \| None = None) -> Card` | Abstract. No implementation. | — |
| `create_spell(self, name_or_power: str \| int \| None = None) -> Card` | Abstract. No implementation. | — |
| `create_artifact(self, name_or_power: str \| int \| None = None) -> Card` | Abstract. No implementation. | — |
| `create_themed_deck(self, size: int) -> dict` | Abstract. No implementation. | — |
| `get_supported_types(self) -> dict` | Abstract. No implementation. | — |

---

### `AggressiveStrategy` (concrete in `AggressiveStrategy.py`)

- **Inherit from:** `GameStrategy`.
- **Idea:** Prefer attacking, low-cost creatures first, target enemies.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `execute_turn(self, hand, battlefield) -> dict` | Simulate one turn: choose which cards to play from `hand`, which targets to attack. Keep logic simple (e.g. play low-cost first, then “attack” first available target). | e.g. `{"strategy": "AggressiveStrategy", "cards_played": [names], "mana_used": int, "targets_attacked": [names], "damage_dealt": int}`. Match subject expected format. |
| `get_strategy_name(self) -> str` | Return the strategy name. | `"AggressiveStrategy"`. |
| `prioritize_targets(self, available_targets: list) -> list` | Return a reordered list (e.g. enemy player first, then creatures). | Same elements, different order; simple rule is enough. |

**Expected (excerpt):**  
`execute_turn` → `'Strategy': 'AggressiveStrategy'`, `'Actions': {'cards_played': ['Goblin Warrior', 'Lightning Bolt'], 'mana_used': 5, 'targets_attacked': ['Enemy Player'], 'damage_dealt': 8}`

---

### `FantasyCardFactory` (concrete in `FantasyCardFactory.py`)

- **Inherit from:** `CardFactory`.
- **Creates:** Fantasy-themed creatures (e.g. Dragon, Goblin), elemental spells (Fire, Ice, Lightning), magical artifacts (Ring, Staff, Crystal). Use `name_or_power` to pick variant or power level; if `None`, use defaults.

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `create_creature(self, name_or_power=None) -> Card` | Return a `CreatureCard` (or compatible) with fantasy name/stats. | e.g. if `name_or_power` is `"dragon"` or `None` → Fire Dragon; `"goblin"` → Goblin Warrior. |
| `create_spell(self, name_or_power=None) -> Card` | Return a `SpellCard` (e.g. Lightning Bolt, Fireball). | — |
| `create_artifact(self, name_or_power=None) -> Card` | Return an `ArtifactCard` (e.g. Mana Ring). | — |
| `create_themed_deck(self, size: int) -> dict` | Build a deck of `size` cards (mix of creatures, spells, artifacts) and return a structure describing it. | e.g. `{"deck": list of Card, "size": size}` or `{"cards": [...], "total": size}`. So that the engine can use it. |
| `get_supported_types(self) -> dict` | Return which themes/types this factory supports. | e.g. `{"creatures": ["dragon", "goblin"], "spells": ["fireball"], "artifacts": ["mana_ring"]}`. |

**Expected (excerpt):**  
`get_supported_types()` → `{'creatures': ['dragon', 'goblin'], 'spells': ['fireball'], 'artifacts': ['mana_ring']}`

---

### `GameEngine` (`GameEngine.py`)

- **Holds:** Current factory, strategy, and optional state (e.g. turn count, total damage).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None` | Store `factory` and `strategy`. Reset any turn/state if needed. | None. |
| `simulate_turn(self) -> dict` | Create a hand (e.g. via factory), run `strategy.execute_turn(hand, battlefield)`, aggregate result. | e.g. `{"turns_simulated": 1, "strategy_used": strategy.get_strategy_name(), "total_damage": int, "cards_created": int}` or similar. Match subject expected output. |
| `get_engine_status(self) -> dict` | Return current engine state. | e.g. same keys as above; or `{"factory": factory class name, "strategy": strategy name, ...}`. |

**Expected (excerpt):**  
Report: `{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy', 'total_damage': 8, 'cards_created': 3}`

---

## Exercise 4 — Tournament Platform (`ex4/`)

- **Imports:** `from ex0.Card import Card`, `from ex2.Combatable import Combatable`, etc.

### `Rankable` (abstract in `Rankable.py`)

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `calculate_rating(self) -> int` | Abstract. No implementation. | — |
| `update_wins(self, wins: int) -> None` | Abstract. No implementation. | — |
| `update_losses(self, losses: int) -> None` | Abstract. No implementation. | — |
| `get_rank_info(self) -> dict` | Abstract. No implementation. | — |

---

### `TournamentCard` (`TournamentCard.py`)

- **Inherit from:** `Card`, `Combatable`, `Rankable`. Implements all their abstract methods.
- **Extra:** Track wins, losses, and a rating (e.g. start 1200; simple Elo-like or fixed +/- on win/loss).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `play(self, game_state: dict) -> dict` | Same idea as other cards. | Dict with card_played, mana_used, effect. |
| `attack(self, target) -> dict` | Same as Combatable (e.g. damage dict). | — |
| `calculate_rating(self) -> int` | Return current rating. | int (e.g. 1200 + wins*16 - losses*16). |
| `update_wins(self, wins: int) -> None` | Add wins to internal counter. | None. |
| `update_losses(self, losses: int) -> None` | Add losses to internal counter. | None. |
| `get_rank_info(self) -> dict` | Return rating and record. | e.g. `{"rating": int, "wins": int, "losses": int}`. |
| `get_tournament_stats(self) -> dict` | Combine card + rank info. | e.g. card info + wins, losses, rating. |

**Expected (excerpt):**  
Rating 1200, record 0-0; after win: winner 1216, loser 1134 (or similar).

---

### `TournamentPlatform` (`TournamentPlatform.py`)

- **Stores:** Registered cards by ID (e.g. `card_id -> TournamentCard`), match history.
- **ID:** Returned by `register_card` (e.g. `"dragon_001"`, `"wizard_001"` — you can generate from name + counter).

| Method | What it must do | Return / behavior |
|--------|------------------|-------------------|
| `register_card(self, card: TournamentCard) -> str` | Register the card and assign a unique ID. Return that ID. | e.g. `"dragon_001"`. |
| `create_match(self, card1_id: str, card2_id: str) -> dict` | Simulate a match between two registered cards (e.g. compare attack or random). Update winner’s wins and loser’s losses; update ratings (simple formula). | `{"winner": winner_id, "loser": loser_id, "winner_rating": int, "loser_rating": int}`. |
| `get_leaderboard(self) -> list` | Return list of entries sorted by rating (highest first). | e.g. `[{"rank": 1, "name": card.name, "rating": int, "wins": int, "losses": int}, ...]`. |
| `generate_tournament_report(self) -> dict` | Summary of platform state. | `{"total_cards": int, "matches_played": int, "avg_rating": float, "platform_status": "active"}`. |

**Expected (excerpt):**  
Match: `{'winner': 'dragon_001', 'loser': 'wizard_001', 'winner_rating': 1216, 'loser_rating': 1134}`  
Leaderboard: `1. Fire Dragon - Rating: 1216 (1-0)`, etc.  
Report: `{'total_cards': 2, 'matches_played': 1, 'avg_rating': 1175, 'platform_status': 'active'}`

---

## Implementation order (avoid getting stuck)

1. **ex0:** Card (ABC) → CreatureCard. Run `python3 -m ex0.main` and match the expected output.
2. **ex1:** SpellCard, ArtifactCard, Deck. Import Card from ex0. Test with a small deck and draw/shuffle/stats.
3. **ex2:** Combatable, Magical (interfaces) → EliteCard. Implement every abstract method; test with ex2.main.
4. **ex3:** GameStrategy, CardFactory (abstract) → AggressiveStrategy, FantasyCardFactory → GameEngine. Wire engine to factory and strategy; one `simulate_turn` should be enough to match the sample.
5. **ex4:** Rankable → TournamentCard (Card + Combatable + Rankable) → TournamentPlatform. Simple win/loss and rating update; then leaderboard and report.

---

## Quick reference: return dict shapes

| Context | Keys to include (typical) |
|--------|----------------------------|
| `Card.get_card_info()` | `name`, `cost`, `rarity` (+ type-specific) |
| `Card.play()` | `card_played`, `mana_used`, `effect` |
| `CreatureCard.attack_target()` | `attacker`, `target`, `damage_dealt`, `combat_resolved` |
| `Deck.get_deck_stats()` | `total_cards`, `creatures`, `spells`, `artifacts`, `avg_cost` |
| `EliteCard.attack` | `attacker`, `target`, `damage`, `combat_type` |
| `EliteCard.defend` | `defender`, `damage_taken`, `damage_blocked`, `still_alive` |
| `EliteCard.cast_spell` | `caster`, `spell`, `targets`, `mana_used` |
| `EliteCard.channel_mana` | `channeled`, `total_mana` |
| `create_match` | `winner`, `loser`, `winner_rating`, `loser_rating` |
| `generate_tournament_report` | `total_cards`, `matches_played`, `avg_rating`, `platform_status` |

If a method is not in this table, use the subject’s expected output for that exercise as the target shape. Keep logic simple; the focus is on abstract patterns and consistent interfaces, not deep game balance.


cards informations :

        self._creatures = [
            {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4, "rarity": "Rare", "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon", "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5, "health": 8},
            {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon", "attack": 5, "health": 2},
            {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2, "health": 6},
            {"name": "Forest Sprite", "cost": 1, "rarity": "Common", "attack": 1, "health": 1},
        ]
        
        self._spells = [
            {"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"},
            {"name": "Healing Potion", "cost": 2, "rarity": "Common", "effect_type": "heal"},
            {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Shield Spell", "cost": 1, "rarity": "Common", "effect_type": "buff"},
            {"name": "Meteor", "cost": 8, "rarity": "Legendary", "effect_type": "damage"},
            {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"},
            {"name": "Divine Light", "cost": 5, "rarity": "Rare", "effect_type": "heal"},
            {"name": "Magic Missile", "cost": 1, "rarity": "Common", "effect_type": "damage"},
        ]
        
        self._artifacts = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common", "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon", "durability": 3, "effect": "Permanent: +2 attack to equipped creature"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare", "durability": 4, "effect": "Permanent: Draw an extra card each turn"},
            {"name": "Shield of Defense", "cost": 5, "rarity": "Rare", "durability": 6, "effect": "Permanent: +3 health to all friendly creatures"},
            {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary", "durability": 8, "effect": "Permanent: +1 cost reduction to all cards"},
            {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon", "durability": 2, "effect": "Permanent: Cards cost 1 less mana"},
            {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon", "durability": 3, "effect": "Permanent: Creatures have stealth"},
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary", "durability": 7, "effect": "Permanent: +1 spell damage"},
        ]
