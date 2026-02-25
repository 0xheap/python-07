"""TournamentPlatform - Platform management system (ex4)."""

from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament cards, matches, and leaderboards."""

    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a new card into the tournament platform."""
        self.cards[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        """Simulate match between two cards. First card always wins."""
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)
        if not card1 or not card2:
            return {}

        winner = card1
        loser = card2

        # Winner gains a simple 16 points; loser drops 16 points.
        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list[TournamentCard]:
        """Return cards sorted by rating, highest first."""
        return sorted(
            self.cards.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True
        )

    def generate_tournament_report(self) -> dict[str, Any]:
        """Return an overview report of the tournament."""
        count = len(self.cards)
        avg_rating = sum(
            c.calculate_rating() for c in self.cards.values()
        ) // count if count > 0 else 0
        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
