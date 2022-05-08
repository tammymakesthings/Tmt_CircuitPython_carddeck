#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
#  SPDX-License-Identifier: MIT
#
#  SPDX-License-Identifier: MIT

try:
    from typing import List
except ImportError:
    pass

import pytest  # noqa

from tmt_carddeck.card import Card  # noqa
from tmt_carddeck.deck import Deck  # noqa
from tmt_carddeck.renderer.renderer import Renderer  # noqa
from tmt_carddeck.renderer.single_card_renderer import SingleCardRenderer  # noqa


class TestSingleCardRenderer:
    def __init__(self):
        pass
