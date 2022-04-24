#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#
#

# SPDX-FileCopyrightText: 2022 Tammy Cravit <tammy@tammymakesthings.com>
#
# SPDX-License-Identifier: MIT

"""
CircuitPython  Card Deck Library
"""
# Disable Pylint "method could be a function" errors
#
# pylint:disable=R0201, invalid-name

import pytest  # noqa

from tmt_carddeck.card import Card  # pytest:disable=unused-import
from tmt_carddeck.constants import (
    DEFAULT_RANK_ORDER,
    DEFAULT_SUIT_ORDER,
)
from tmt_carddeck.deck import (
    Deck,
    DeckEmpty,
    standard_deck,
)  # noqa pylint:disable=unused-import


class TestDeck:
    """Unit tests for the Deck class."""

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

    def test_can_get_std_deck(self) -> None:
        """

        Returns:

        """
        the_deck = standard_deck()
        assert isinstance(the_deck, Deck)
        assert len(the_deck) == 54

        for suit in DEFAULT_SUIT_ORDER:
            for rank in DEFAULT_RANK_ORDER:
                assert Card(rank=rank, suit=suit) in the_deck
        assert Card(None, None) in the_deck
        assert Card("*", "*") in the_deck

    def test_std_deck_optional_args(self) -> None:
        """

        Returns:

        """

        joker_card = Card("*", "*")
        blank_card = Card(None, None)

        deck_without_joker = standard_deck(include_joker=False)
        deck_without_blank = standard_deck(include_blank=False)
        only_playable_cards = standard_deck(include_blank=False, include_joker=False)

        assert isinstance(deck_without_blank, Deck)
        assert len(deck_without_blank) == 53
        assert blank_card not in deck_without_blank

        assert isinstance(deck_without_joker, Deck)
        assert len(deck_without_joker) == 53
        assert joker_card not in deck_without_joker

        assert isinstance(only_playable_cards, Deck)
        assert len(only_playable_cards) == 52
        assert blank_card not in only_playable_cards
        assert joker_card not in only_playable_cards
