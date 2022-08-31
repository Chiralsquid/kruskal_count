"""Generic jokerless playing cards implementation, with classes for deck and card. Uses Enums for Suit and Rank."""

import random
from dataclasses import dataclass
from enum import Enum


class Suit(Enum):
    """Enum for the suits of a playing card."""
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3

    def __str__(self):
        return self.name.capitalize()


class Rank(Enum):
    """Enum for the ranks of a playing card."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self):
        return self.name.capitalize()


@dataclass
class PlayingCard:
    suit: Suit
    rank: Rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._cards = []
        self.add_standard_deck()

    def number_of_cards(self):
        """Return the number of cards in the deck."""
        return len(self._cards)

    def __str__(self):
        return f"Deck of {self.number_of_cards()} cards"

    @property
    def cards(self):
        """Return the list of cards in the deck."""
        return self._cards

    def deal_card(self):
        """Deal a card from the deck and return it."""
        return self._cards.pop()

    def add_standard_deck(self, copies: int = 1):
        """Add one or multiple copies of a standard deck of 52 cards to the deck."""
        for _ in range(copies):
            for suit in Suit:
                for rank in Rank:
                    self._cards.append(PlayingCard(suit, rank))
        return self

    def add_card(self, card: PlayingCard):
        """Add a card to the deck."""
        self._cards.append(card)

    def shuffle(self):
        """Shuffle the deck in place."""
        random.shuffle(self._cards)
        return self

    def remove_standard_deck(self):
        pass

    def clear(self):
        """Clear the deck of all cards."""
        self._cards.clear()

    def merge(self, other):
        """Merge the deck with another deck."""
        self._cards.extend(other.cards)
        other.clear()


if __name__ == "__main__":
    test1 = PlayingCard(Suit.HEARTS, Rank.ACE)
    test2 = PlayingCard(Suit.HEARTS, Rank.JACK)
    print(test1)
    print(test1.rank == Rank.ACE)




