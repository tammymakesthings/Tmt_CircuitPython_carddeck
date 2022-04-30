#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#
#
#
#
# SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

from tmt_carddeck.card import Card  # noqa
from tmt_carddeck.constants import DEFAULT_RANK_ORDER, DEFAULT_SUIT_ORDER


try:
    from typing import List, Optional  # noqa
except ImportError:
    pass


class DeckEmpty(RuntimeWarning):
    """Raised when the deck is empty and reset_if_empty is false."""


class Deck:
    """
    Represents a deck of cards.
    """

    def __init__(self, initial_cards: Optional[List[Card]] = None) -> None:
        """
        Initialize a new Deck

        Args:
            initial_cards (Optional[list[Card]]): The initial list of cards.
        """
        self._initial_cards: Optional[List[Card]] = (
            list(initial_cards) if initial_cards else []
        )
        self._cards: Optional[List[Card]] = []
        self.reset_deck()

    def reset_deck(self) -> None:
        """
        Reset the deck to the initial cards.
        Returns:

        """
        self._cards = list(self._initial_cards)  # type: ignore

    @property
    def cards(self) -> Optional[List[Card]]:
        """
        Retrieve a reference to the deck's cards. We return a reference so
        the caller can modify the deck if desired.

        Returns:
        A reference to the deck's current contents.
        """
        return self._cards if self._cards else None

    def pick(self, **kwargs):
        """
        Pick a card from the deck.
        Args:
            kwargs: The argument dictionary:
                pick_location (int): The pick location within the stack of cards.
                reset_if_empty (bool): True to reset the deck to its initial
                    state if it's empty.

        Returns:
            The selected card.

        Raises:
            `DeckEmpty` is raised if the deck is empty and reset_if_empty
            is False.
        """
        reset_if_empty: bool = kwargs.get("reset_if_empty", True)
        pick_location: int = kwargs.get("pick_location", 0)

        if len(self._cards) == 0:
            if reset_if_empty:
                self.reset_deck()
            else:
                raise DeckEmpty("no cards in deck")
        return self._cards.pop(pick_location)

    def __len__(self):
        """
        Get the number of cards in the deck.
        """
        return len(list(self._cards)) if self._cards else 0

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value


def standard_deck(
    include_blank: Optional[bool] = True, include_joker: Optional[bool] = True
) -> Deck:
    """Build and return a standard card deck."""
    the_deck: List[Card] = []

    if include_blank:
        the_deck.append(Card(None, None))

    for suit in DEFAULT_SUIT_ORDER:
        for rank in DEFAULT_RANK_ORDER:
            the_deck.append(Card(rank, suit))

    if include_joker:
        the_deck.append(Card("*", "*"))

    return Deck(initial_cards=the_deck)
