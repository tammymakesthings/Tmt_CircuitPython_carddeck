#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#
#
# SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

from collections import namedtuple


try:
    from typing import List, Optional, Union, Sequence  # noqa
except ImportError:
    pass

from tmt_carddeck.constants import DEFAULT_RANK_ORDER, DEFAULT_SUIT_ORDER


CardSignatureType = namedtuple("CardSignatureType", "type data")


class Card:
    """
    Class to represent a playing card.
    """

    def __init__(
            self,
            rank: Optional[Union[int, str, None]] = None,
            suit: Optional[str] = None,
            **kwargs
    ) -> None:
        """
        Create a new Card.

        Parameters:
            rank - The value of the card. Non-int values are upper-cased and
                only the first letter is saved. Jokers have a value of '*'.
            suit - The suit of the card. The value is upper-cased and only the
                first letter is saved. Jokers have a suit of '*'.
            rank_order - If provided, override the rank ordering of cards. If
                not provided, DEFAULT_RANK_ORDER is used instead.
            suit_order - If provided, override the suit ordering of cards. If
                not provided, DEFAULT_SUIT_ORDER is used instead.
            is_joker - If provided and a truthy value, this card is a joker.

        Returns:
            The newly created card.

        Raises:
            AttributeError is raised if any of these conditions are true:
                - The rank and suit are both None
        """

        self._value_order: List[str] = []
        self._rank_order = list(kwargs.get("rank_order", DEFAULT_RANK_ORDER))
        self._suit_order = list(kwargs.get("suit_order", DEFAULT_SUIT_ORDER))
        self._is_joker: bool = kwargs.get("is_joker", False)

        self._build_value_order_list()
        self._signature: Optional[CardSignatureType] = None
        self._rank: Optional[Union[int, str, None]] = None
        self._suit: Optional[str] = None

        if rank == "*" or suit == "*":
            self._rank = rank
            self._suit = suit
            self._is_joker = True
        else:
            if rank and str(rank) not in self._rank_order and self.is_joker is False:
                raise ValueError("rank not in rank_order list")
            if suit and str(suit) not in self._suit_order and self.is_joker is False:
                raise ValueError("suit not in suit_order list")

            if isinstance(rank, int):
                self._rank = str(rank)
            elif rank is not None:
                self._rank = str(rank).strip().upper()

            if suit is not None:
                self._suit = str(suit).strip().upper()

    def _build_value_order_list(self) -> None:
        """Update the value order list from the rank order and suit order."""
        self._value_order = [""]

        for suit_iterator in self._suit_order:
            if suit_iterator != "*":
                for rank_iterator in self._rank_order:
                    card_name: str = ""  # noqa

                    if rank_iterator == "*" or suit_iterator == "*":
                        card_name = "*"
                    else:
                        card_name = f"{rank_iterator}{suit_iterator}"
                    if card_name not in self._value_order:
                        self._value_order.append(card_name)

        if "*" not in self._value_order:
            self._value_order.append("*")

    @property
    def rank(self) -> Optional[str]:
        """Retrieves the card's rank."""
        return self._rank

    @property
    def suit(self) -> Optional[str]:
        """Retrieves the card's suit."""
        return self._suit

    @property
    def rank_order(self) -> List[str]:
        """Retrieves the card's rank order."""
        return list(self._rank_order)

    @property
    def suit_order(self) -> List[str]:
        """Returns the card's suit order."""
        return list(self._suit_order)

    @property
    def value_order(self) -> List[str]:
        """Returns the card's value order."""
        return list(self._value_order)

    @value_order.setter
    def value_order(self,
                    new_order: Sequence) -> None:
        """Overrides the card's value order."""
        self._value_order = list(new_order)

    @property
    def is_joker(self) -> bool:
        """Returns True if the card is a joker."""
        return self._is_joker

    @property
    def rank_value(self) -> int:
        """Retrieves the numeric rank value of the card."""
        if self.is_joker:
            if (self.rank is None or self.rank == "*") and (
                    self.suit is None or self.suit == "*"
            ):
                return len(self._rank_order)
            return self._int_value_from_string(str(self.rank))
        return self._rank_order.index(self.rank)

    @property
    def suit_value(self) -> int:
        """Retrieves the numeric suit value of the card."""
        if self.is_joker:
            if (self.rank is None or self.rank == "*") and (
                    self.suit is None or self.suit == "*"
            ):
                return len(self._suit_order)
            return self._int_value_from_string(str(self.suit))
        return self._suit_order.index(self.suit)

    def __int__(self) -> int:
        """Retrieves the numeric value of the card."""
        if self.is_joker:
            if str(self) in self._value_order:
                return self._value_order.index(str(self))
            if str(self) == "*":
                return len(self._value_order) - 1
            return self._int_value_from_string(str(self))

        if str(self) in self._value_order:
            return self._value_order.index(str(self))

        raise AttributeError("card value is unknown")

    def __eq__(self, other) -> bool:
        """Compares two cards (==)"""
        return self.suit == other.suit and self.rank == other.rank

    def __gt__(self, other) -> bool:
        """Compares two cards (>)"""
        return int(self) > int(other)

    def __lt__(self, other) -> bool:
        """Compares two cards (<)"""
        return int(self) < int(other)

    def __str__(self) -> str:
        """Returns the string value of a card."""
        if self.is_joker:
            joker_str = "*"
            if self.rank is not None and self.rank != "*":
                joker_str = joker_str + str(self.rank)
            if self.suit is not None and self.suit != "*":
                joker_str = joker_str + str(self.suit)
            return joker_str
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        """Returns a string representation of a card."""
        return str(self)

    def __hash__(self):
        hash_code = 0
        if self.suit is not None:
            hash_code += self._int_value_from_string(str(self.suit)) * 1024
        if self.rank is not None:
            hash_code += self._int_value_from_string(str(self.rank))

        return hash_code

    # pylint: disable=no-self-use
    def _int_value_from_string(self,
                               str_value: str) -> int:
        """Convert a string to an integer value."""
        int_val = 0
        for val_char in str_value:
            int_val += ord(val_char)
        return int_val

    def sign(
            self,
            text_signature: Optional[str] = None,
            graphic_signature: Optional[str] = None,
    ) -> None:
        """Allows a signature to be added to a card."""
        # Check that we have one kind of signature but not both
        if not text_signature and not graphic_signature:
            raise AttributeError("card must have a text or graphic signature")
        if text_signature and graphic_signature:
            raise AttributeError("card cannot have both text and graphic signatures")
        if self._signature is not None:
            raise AttributeError("card is already signed")

        if text_signature:
            self._signature = CardSignatureType(type="text", data=text_signature)
        elif graphic_signature:
            self._signature = CardSignatureType(type="graphic", data=graphic_signature)

    @property
    def signature(self) -> Optional[CardSignatureType]:
        """Retrieve the signature from the card."""
        return self._signature
