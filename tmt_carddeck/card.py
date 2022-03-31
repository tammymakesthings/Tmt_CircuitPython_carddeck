# SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
# SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

try:
    from typing import List, Optional, Union
except ImportError:
    pass


class Card:
    """
    Class to represent a playing card.
    """

    DEFAULT_RANK_ORDER: List[str] = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
        "*",
    ]

    DEFAULT_SUIT_ORDER: List[str] = ["C", "D", "H", "S", "*"]

    def __init__(
        self,
        rank: Optional[Union[int, str]] = None,
        suit: Optional[str] = None,
        **kwargs
    ) -> None:
        """
        Create a new Card.

        Parameters:
            rank - The value of the card. Non-int values are uppercased and
                only the first letter is saved. Jokers have a value of '*'.
            suit - The suit of the card. The value is uppercased and only the
                first letter is saved. Jokers have a suit of '*'.
            rank_order - If provided, override the rank ordering of cards. If
                not provided, DEFAULT_RANK_ORDER is used instead.
            suit_order - If provided, override the suit ordering of cards. If
                not provided, DEFAULT_SUIT_ORDER is used instead.

        Returns:
            The newly created card.

        Raises:
            AttributeError is raised if any of these conditions are true:
                - The rank and suit are both None
        """

        # REFACTOR: Check that rank and suit exist in the rank order and suit
        # order arrays.

        self._rank_order = list(kwargs.get("rank_order", Card.DEFAULT_RANK_ORDER))
        self._suit_order = list(kwargs.get("suit_order", Card.DEFAULT_SUIT_ORDER))

        if rank is None and suit is None:
            raise AttributeError("blank cards are not allowed")

        if rank == "*" or suit == "*":
            self._rank = "*"
            self._suit = "*"
        else:
            if isinstance(rank, int):
                self._rank = str(rank)
            else:
                self._rank = str(rank).strip().upper()[0]

            self._suit = str(suit).strip().upper()[0]

    @property
    def rank(self) -> str:
        """Retrieves the card's rank."""
        return self._rank

    @property
    def suit(self) -> str:
        """Retrieves the card's suit."""
        return self._suit

    def rank_value(self) -> int:
        """Retrieves the numeric rank value of the card.

        Note that rank values of 0 and 1 are undefined by default so that the
        integer value of a card's rank matches the number on the card.
        """
        # REFACTOR Don't make assumptions about the length/offset of rank
        # order
        return self._rank_order.index(self.rank) + 2

    def suit_value(self) -> int:
        """Retrieves the numeric suit value of the card."""
        return self._suit_order.index(self.suit)

    def __int__(self) -> int:
        """Retrieves the numeric value of the card.

        Note that this is deliberately not designed to be the index of the card
        within the deck. Rather, it's designed to just produce a unique number
        such that cards can be compared to one another.
        """

        # REFACTOR: We shouldn't make assumptions about the number of suits
        # and the number of ranks.

        return (self.suit_value() * 15) + self.rank_value()

    # TODO
    # - Make cards comparable
    # - Make cards sequenceable
    # - Make cards hashable
    # - Add suitable string conversion methods (__str__ and __repr__)