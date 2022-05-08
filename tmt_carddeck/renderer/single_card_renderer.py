from tmt_carddeck.card import Card
from tmt_carddeck.renderer.renderer import Renderer


class SingleCardRenderer(Renderer):
    def __init__(self,
                 cards: list[Card],
                 **kwargs):
        super().__init__(cards, **kwargs)
