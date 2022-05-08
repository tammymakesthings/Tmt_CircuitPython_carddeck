#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
#  SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

try:
    from typing import List, Optional
except ImportError:
    pass

import displayio

from tmt_carddeck.card import Card
from tmt_carddeck.renderer.renderer import Renderer


class SingleCardRenderer(Renderer):
    """
    The SingleCardRenderer displays a single card on the display.
    """

    def __init__(self, cards: List[Card], **kwargs):
        self.x = 0
        super().__init__(cards, **kwargs)  # noqa

    def render(
        self,
        draw_on: displayio.Group,
        the_card: Card,
        x_position: int,
        y_position: int,
        width_in_tiles: int,
        height_in_tiles: int,
        orientation: Optional[int] = None,
        **kwargs
    ) -> None:
        pass
