#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#
#
#
# SPDX-License-Identifier: MIT

"""CircuitPython Card Deck Library"""

import pytest  # pylint:disable=unused-import

from tmt_carddeck.card import Card
from tmt_carddeck.deck import Deck


@pytest.fixture
def starter_deck() -> Deck:
    """Return a starter deck for testing."""
    the_cards = []
    for rank in range(2, 6):
        the_cards.append(Card(rank=rank, suit="S"))
    return Deck(initial_cards=the_cards)
