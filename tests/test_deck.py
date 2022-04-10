# SPDX-FileCopyrightText: 2022 Tammy Cravit <tammy@tammymakesthings.com>
#
# SPDX-License-Identifier: MIT

"""
CircuitPython  Card Deck Library
"""

import pytest  # noqa

from tmt_carddeck.card import Card  # pytest:disable=unused-import
from tmt_carddeck.deck import (Deck, DeckEmpty)  # noqa pylint:disable=unused-import


class TestDeck:
    # Disable Pylint "method could be a function" errors
    #
    # pylint:disable=R0201

    """Unit tests for the Deck class.
    """

    def test_can_initialize_deck(self, starter_deck) -> None:
        """
        Check that we can initialize a Deck object.

        Args:
            starter_deck (): the starter_deck pytest fixture
        """
        assert isinstance(starter_deck, Deck)
        assert len(starter_deck) > 0
        assert [isinstance(the_card, Card) for the_card in starter_deck.cards]

    # Test picking cards - with and without deck reset.
    def test_pick_cards(self, starter_deck) -> None:
        """
        Check that we can pick cards from the Deck.

        Args:
            starter_deck (): the starter_deck pytest fixture
        """
        for _ in range(len(starter_deck) - 1):
            assert isinstance(starter_deck.pick(), Card)

    def test_reset_on_empty(self, starter_deck) -> None:
        """
        Check that the Deck resets if it's empty.

        Args:
            starter_deck (): the starter_deck pytest fixture
        """
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
        picked_card = starter_deck.pick()
        assert isinstance(picked_card, Card)

    def test_raise_exception_no_reset(self, starter_deck) -> None:
        """
        Check that when the deck is empty and reset_if_empty is false,
        a DeckEmptyError is raised.

        Args:
            starter_deck (): the starter_deck pytest fixture
        """
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
        with pytest.raises(DeckEmpty):
            _ = starter_deck.pick(reset_if_empty=False)

    # Test sequence methods®
    def test_dunder_len(self, starter_deck) -> None:
        """
        Check that `len(deck)` works.

        Args:
            starter_deck (): the starter_deck pytest fixture
        """
        assert len(starter_deck) > 0
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
