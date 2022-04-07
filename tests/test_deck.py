# SPDX-FileCopyrightText: 2022 Tammy Cravit <tammy@tammymakesthings.com>
#
# SPDX-License-Identifier: MIT

import pytest # noqa
from tmt_carddeck.card import Card
from tmt_carddeck.deck import Deck

class TestDeck:
    """
    """

    def test_can_initialize_deck(self, starter_deck):
        assert isinstance(starter_deck, Deck)
        assert len(starter_deck) > 0
        assert [isinstance(the_card, Card) for the_card in starter_deck.cards]

    def test_can_pick_cards(self, starter_deck):
        for _ in range(len(starter_deck) - 1):
            assert isinstance(starter_deck.pick(), Card)

    def test_deck_resets_on_empty(self, starter_deck):
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
        picked_card = starter_deck.pick()
        assert isinstance(picked_card, Card)

    def test_deck_raises_exception_on_non_reset(self, starter_deck):
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
        with pytest.raises(ValueError):
            _ = starter_deck.pick(reset_if_empty=False)

    def test_dunder_len(self, starter_deck):
        assert len(starter_deck) > 0
        for _ in range(len(starter_deck)):
            starter_deck.pick()
        assert len(starter_deck) == 0
