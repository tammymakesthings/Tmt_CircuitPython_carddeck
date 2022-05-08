#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
#  SPDX-License-Identifier: MIT

"""
tmt_carddeck: CircuitPython Card Deck library.
"""

try:
    from typing import Dict, Tuple, Optional, Any, Union
except ImportError:
    pass

import adafruit_imageload  # type: ignore
import displayio  # type: ignore # noqa
from adafruit_displayio_layout.layouts.grid_layout import GridLayout  # type: ignore # noqa

from tmt_carddeck.card import Card  # noqa
from tmt_carddeck.constants import FACE_DOWN, FACE_UP  # noqa
from tmt_carddeck.deck import Deck  # nopq


SymbolTileMap = Union[Dict[str, Tuple[int, int]], None]

DEFAULT_SYMBOL_MAP: SymbolTileMap = {
        'A': (0, 0), '2': (0, 1), '3': (0, 2), '4': (0, 3), '5': (0, 4),
        '6': (0, 5), '7': (0, 6), '8': (0, 7), '9': (0, 8), '10': (0, 9),
        'J': (1, 0), 'Q': (1, 1), 'K': (1, 2),
        'D': (1, 3), 'C': (1, 4), 'H': (1, 5), 'S': (1, 6),
}


class Renderer:
    """
    Default card renderer base class.
    """

    def __init__(self,
                 cards: list[Card],
                 **kwargs):
        self.asset_path: str = kwargs.get("asset_path", "/assets")
        self.face_up_background: str = kwargs.get("face_up_background",
                                                  'card_front_sprites_24x24.bmp')
        self.face_down_background: str = kwargs.get("face_down_background",
                                                    'card_back_sprites_24x24.bmp')
        self.symbol_image: str = kwargs.get("symbol_image",
                                            'card_symbols_24x24.bmp')
        self.background_tile_size: int = kwargs.get("background_tile_size",
                                                    24)
        self.symbol_tile_size: int = kwargs.get("symbol_tile_size", 16)
        self.row_offset_black: int = kwargs.get("row_offset_black", 0)
        self.row_offset_red: int = kwargs.get("row_offset_red", 2)
        self.symbol_tile_mapping: SymbolTileMap = kwargs.get("symbol_tile_map",
                                                             DEFAULT_SYMBOL_MAP)
        self.cards: Deck = Deck(cards)

        self.face_up_bmp: Optional[displayio.Bitmap] = None
        self.face_down_bmp: Optional[displayio.Bitmap] = None
        self.symbol_bmp: Optional[displayio.Bitmap] = None

        self.face_up_palette: Optional[displayio.Palette] = None
        self.face_down_palette: Optional[displayio.Palette] = None
        self.symbol_palette: Optional[displayio.Palette] = None

        self.face_up_tilegrid: Optional[displayio.TileGrid] = None
        self.face_down_tilegrid: Optional[displayio.TileGrid] = None
        self.symbol_tilegrid: Optional[displayio.TileGrid] = None

    def load_assets(self) -> None:
        """

        Returns:

        """

        self.face_up_bmp, self.face_up_palette, self.face_up_tilegrid = \
            self.load_bitmap_from_disk(self.face_up_background, 3, 3, \
                                       self.background_tile_size)
        self.face_dpwm_bmp, self.face_down_palette, self.face_down_tilegrid = \
            self.load_bitmap_from_disk(self.face_down_background, 3, 3, \
                                       self.background_tile_size)
        self.symbol_bmp, self.symbol_palette, self.symbol_tilegrid = \
            self.load_bitmap_from_disk(self.symbol_image, 10, 4, \
                                       self.symbol_tile_size)

    def load_bitmap_from_disk(self,
                              bitmap_name: str,
                              x_tiles: int,
                              y_tiles: int,
                              tile_size: int) -> Tuple[displayio.Bitmap,
                                                       displayio.Palette,
                                                       displayio.TileGrid]:
        """

        Args:
            bitmap_name ():
            x_tiles ():
            y_tiles ():
            tile_size ():

        Returns:

        """
        bitmap_path = f"/{self.asset_path}/{bitmap_name}"
        sprite_sheet, palette = adafruit_imageload.load(bitmap_path,
                                                        bitmap=displayio.Bitmap,
                                                        palette=displayio.Palette)
        sprite = displayio.TileGrid(bitmap=sprite_sheet,
                                    pixel_shader=palette,
                                    width=x_tiles,
                                    height=y_tiles,
                                    tile_width=tile_size,
                                    tile_height=tile_size)
        return sprite_sheet, palette, sprite

    def render(self,
               draw_on: displayio.Group,
               the_card: Card,
               x_position: int,
               y_position: int,
               width_in_tiles: int,
               height_in_tiles: int,
               orientation: Optional[int] = None,
               **kwargs) -> None:
        """

        Args:
            draw_on ():
            the_card ():
            x_position ():
            y_position ():
            width_in_tiles ():
            height_in_tiles ():
            orientation ():
            **kwargs ():

        Returns:

        """

        raise NotImplementedError('Renderer base class is virtual')
