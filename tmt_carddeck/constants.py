try:
    from typing import List
except ImportError:
    pass


DEFAULT_RANK_ORDER: List[str] = [
        "2", "3", "4", "5", "6", "7", "8",
        "9", "10", "J", "Q", "K", "A",
]

DEFAULT_SUIT_ORDER: List[str] = [
        "C", "D", "H", "S",
]
