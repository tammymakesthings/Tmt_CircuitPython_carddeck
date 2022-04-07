# SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
# SPDX-License-Identifier: MIT


"""CircuitPython Card Deck Library
"""


import pytest  # pylint:disable=unused-import
from tmt_carddeck.card import Card

# pylint:disable=no-self-use,missing-function-docstring


class TestCard:
    """Unit tests for the Card class"""

    def test_can_initialize(self):
        the_card = Card(rank="queen", suit="hearts")
        assert the_card.rank == "Q"
        assert the_card.suit == "H"

    def test_initialize_with_no_values(self):
        with pytest.raises(AttributeError):
            _ = Card(rank=None, suit=None)

    def test_can_create_joker(self):
        the_card = Card(rank="*")
        assert the_card.rank == "*"
        assert the_card.suit == "*"

    def test_can_get_rank_order(self):
        assert Card(rank=7, suit="D").rank_value() == 7
        assert Card(rank="J", suit="D").rank_value() == 11
        assert Card(rank="A", suit="D").rank_value() == 14
        assert Card(rank="*").rank_value() == 15

    def test_can_get_suit_order(self):
        assert Card(rank="7", suit="C").suit_value() == 0
        assert Card(rank="7", suit="D").suit_value() == 1
        assert Card(rank="7", suit="H").suit_value() == 2
        assert Card(rank="7", suit="S").suit_value() == 3
        assert Card(rank="*").suit_value() == 4

    def test_can_get_int_value(self):
        assert int(Card(2, "C")) == 2
        assert int(Card("A", "C")) == 14
        assert int(Card(2, "D")) == 17
        assert int(Card("A", "D")) == 29
        assert int(Card(2, "H")) == 32
        assert int(Card("A", "H")) == 44
        assert int(Card(2, "S")) == 47
        assert int(Card("A", "S")) == 59
        assert int(Card("*")) == 75

    def test_card_equality(self):
        card_one = Card(3, "C")
        card_two = Card(3, "C")
        card_three = Card(3, "S")
        card_four = Card(7, "C")
        assert card_one == card_two
        assert card_one != card_three
        assert card_one != card_four
        assert Card("*") == Card("*")

    def test_card_greater_than(self):
        assert Card('A', 'S') > Card(2, 'S')
        assert Card('A', 'S') > Card('A', 'D')
        assert Card('*') > Card('A', 'S')

    def test_card_less_than(self):
        assert Card(2, 'S') < Card(3, 'S')
        assert Card('A', 'D') < Card('A', 'S')

    def test_dunder_str(self):
        assert str(Card('A', 'D')) == 'AD'
        assert str(Card(5, 'S')) == '5S'
        assert str(Card('*')) == '*'

    def test_dunder_repr(self):
        assert repr(Card('A', 'D')) == 'AD'
        assert repr(Card(5, 'S')) == '5S'
        assert repr(Card('*')) == '*'

    def test_can_sign_text(self):
        the_card = Card('A', 'S')
        the_card.sign(text_signature='Tammy')
        the_signature = the_card.signature
        assert the_signature.type == 'text'
        assert the_signature.data == 'Tammy'

    def test_can_sign_graphic(self):
        the_card = Card('A', 'S')
        the_card.sign(graphic_signature='Tammy')
        the_signature = the_card.signature
        assert the_signature.type == 'graphic'
        assert the_signature.data == 'Tammy'

    def test_have_exactly_one_signature_type(self):
        the_card = Card('A', 'S')
        with pytest.raises(AttributeError):
            the_card.sign()
        with pytest.raises(AttributeError):
            the_card.sign(text_signature='Tammy', graphic_signature='Tammy')

    def test_cant_sign_more_than_once(self):
        the_card = Card('A', 'S')
        the_card.sign(text_signature='Tammy')
        with pytest.raises(AttributeError):
            the_card.sign(text_signature='Also Tammy')

    def test_can_override_rank_order(self):
        pass

    def test_can_override_suit_order(self):
        pass
