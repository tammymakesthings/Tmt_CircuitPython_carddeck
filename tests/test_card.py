#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#
#
#
#
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
        the_card = Card(rank="Q", suit="H")
        assert the_card.rank == "Q"
        assert the_card.suit == "H"

    def test_can_create_joker(self):
        the_card = Card(rank="*")
        assert the_card.rank == "*"
        assert the_card.suit is None
        assert the_card.is_joker

    def test_can_create_multiple_jokers(self):
        joker_one = Card(rank="*", suit="R")
        joker_two = Card(rank="*", suit="B")
        joker_three = Card(rank="P", suit="P", is_joker=True)

        assert joker_one.is_joker
        assert joker_two.is_joker
        assert joker_three.is_joker
        assert joker_one != joker_two
        assert joker_three != joker_two
        assert joker_three != joker_one

    def test_multi_joker_int_val(self):
        joker_one = Card(rank="*", suit="R")
        joker_two = Card(rank="*", suit="B")
        assert int(joker_one) != int(joker_two)

    def test_can_get_rank_order(self):
        assert Card(rank="7", suit="D").rank_value == 5
        assert Card(rank="J", suit="D").rank_value == 9
        assert Card(rank="A", suit="D").rank_value == 12
        assert Card(rank="*").rank_value == 13

    def test_can_get_suit_order(self):
        assert Card(rank="7", suit="C").suit_value == 0
        assert Card(rank="7", suit="D").suit_value == 1
        assert Card(rank="7", suit="H").suit_value == 2
        assert Card(rank="7", suit="S").suit_value == 3
        assert Card(rank="*").suit_value == 4

    def test_can_get_int_value(self):
        assert int(Card(2, "C")) == 1
        assert int(Card("A", "C")) == 13
        assert int(Card(2, "D")) == 14
        assert int(Card("A", "D")) == 26
        assert int(Card(2, "H")) == 27
        assert int(Card("A", "H")) == 39
        assert int(Card(2, "S")) == 40
        assert int(Card("A", "S")) == 52
        assert int(Card("*")) == 53
        assert int(Card(rank=2, suit="F", is_joker=True)) == 162

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
        assert Card("A", "S") > Card(2, "S")
        assert Card("A", "S") > Card("A", "D")
        assert Card("*") > Card("A", "S")

    def test_card_less_than(self):
        assert Card(2, "S") < Card(3, "S")
        assert Card("A", "D") < Card("A", "S")

    def test_dunder_str(self):
        assert str(Card("A", "D")) == "AD"
        assert str(Card(5, "S")) == "5S"
        assert str(Card("*")) == "*"
        assert str(Card("*", "R")) == "*R"
        assert str(Card(2, "*")) == "*2"
        assert str(Card(rank="5", suit="P", is_joker="*")) == "*5P"

    def test_dunder_repr(self):
        assert repr(Card("A", "D")) == "AD"
        assert repr(Card(5, "S")) == "5S"
        assert repr(Card("*")) == "*"

    def test_dunder_hash(self):
        assert hash(Card("A", "D")) == 69697
        assert hash(Card(5, "S")) == 85045
        assert hash(Card("*")) == 42
        assert hash(Card(rank="*", suit="R")) == 84010
        assert hash(Card(rank=3, suit="*")) == 43059
        assert hash(Card(rank=10, suit="F", is_joker=True)) == 71777

    def test_can_sign_text(self):
        the_card = Card("A", "S")
        the_card.sign(text_signature="Tammy")
        the_signature = the_card.signature
        assert the_signature.type == "text"
        assert the_signature.data == "Tammy"

    def test_can_sign_graphic(self):
        the_card = Card("A", "S")
        the_card.sign(graphic_signature="Tammy")
        the_signature = the_card.signature
        assert the_signature.type == "graphic"
        assert the_signature.data == "Tammy"

    def test_cant_multisign_card(self):
        the_card = Card("A", "S")
        with pytest.raises(AttributeError):
            the_card.sign()
        with pytest.raises(AttributeError):
            the_card.sign(text_signature="Tammy", graphic_signature="Tammy")

    def test_cant_sign_more_than_once(self):
        the_card = Card("A", "S")
        the_card.sign(text_signature="Tammy")
        with pytest.raises(AttributeError):
            the_card.sign(text_signature="Also Tammy")

    def test_can_override_rank_order(self):
        pass

    def test_can_override_suit_order(self):
        pass
