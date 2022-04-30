"""
tmt_carddeck: CircuitPython Card Deck library.
"""

#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
#  SPDX-License-Identifier: MIT

from micropython import const  # type: ignore


try:
    from typing import List  # noqa
except ImportError:
    pass

DEFAULT_RANK_ORDER: List[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
]

DEFAULT_SUIT_ORDER: List[str] = [
    "C",
    "D",
    "H",
    "S",
]

ROTATION_0: int = const(0)
ROTATION_90: int = const(90)
ROTATION_180: int = const(180)
ROTATION_270: int = const(270)

FACE_UP: bool = True
FACE_DOWN: int = False
