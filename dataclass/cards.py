from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():    
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

# setting order=True allows to make comparisons between cards
@dataclass(order=True)
class PlayingCard:
    """
    init=False means that sort_index should not be included in the __init__() method
    (and also, sort_index is omitted from the PlayingCard repr)
    """
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    """
    This method permits we initialize the sort_index after 
    the calling of the __init__() method. So, we can set up values 
    for rank and suit first, and then fill the sort_index based 
    on their values
    """
    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)

    def __str__(self):
        return f'{self.suit} {self.rank}'

    def __repr__(self):
        return f'{self.suit} {self.rank}'

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        # !s in string formatting means that we want to use the str() representation from each PlayingCard
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'