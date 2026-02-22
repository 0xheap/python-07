"""Abstract magic interface."""

from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """Interface for magic: cast spell, channel mana, magic stats."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict[str, Any]:
        """Cast a spell on targets. Returns result dict."""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Channel mana. Returns result dict."""
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        """Return magic-related stats."""
        ...
