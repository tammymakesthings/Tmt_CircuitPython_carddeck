# SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
# SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

from collections import namedtuple   # noqa
from tmt_carddeck.card import Card   # noqa

try:
    from typing import List, Optional, Union, Tuple  # noqa
except ImportError:
    pass

class Deck:
    """
    """
    def __init__(self, initial_cards: Optional[List[Card]] = None) -> None:
        self._initial_cards = list(initial_cards)
        self._cards = []
        self.reset_deck()

    def reset_deck(self) -> None:
        self._cards = list(self._initial_cards)

    @property
    def cards(self) -> Optional[List[Card]]:
        return self._cards

    def pick(self,
             pick_location: Optional[int] = 0,
             reset_if_empty: Optional[bool] = True) -> Card:
        if len(self._cards) == 0:
            if reset_if_empty:
                self.reset_deck()
            else:
                raise ValueError('no cards in deck')
        return self._cards.pop(pick_location)

    def __len__(self):
        return len(self._cards)
