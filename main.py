from cards import Deck, Rank
from random import seed


seed(29)  # randomly selected integer. This forces the shuffled deck to be the same every run.
deck = Deck()
deck.add_standard_deck(5)
deck.shuffle()

print(deck.cards)


# def kruskal_count_recursive(deck: Deck, starting_card_position: int = 0) -> PlayingCard:
#     """Start from the starting_card_position, run the kruskal count procedure and return the final card.
#     Does not alter the deck. Recursive.
#     """
#     current_card = deck.cards[starting_card_position]
#     if current_card.rank is not (Rank.JACK or Rank.QUEEN or Rank.KING):
#         try:
#             return kruskal_count(deck, starting_card_position + current_card.rank.value)
#         except IndexError:
#             return current_card
#     else:
#         try:
#             return kruskal_count(deck, starting_card_position + 5)
#         except IndexError:
#             return current_card


def kruskal_count(deck: Deck, starting_card_position: int = 0) -> list:
    """Start from the starting_card_position, run the kruskal count procedure and return the list of cards up to the
    final. Does not alter the deck. Iterative.
    """
    current_card = deck.cards[starting_card_position]
    history = [current_card]
    card_position = starting_card_position
    while True:
        try:
            if current_card.rank is not (Rank.JACK or Rank.QUEEN or Rank.KING):
                card_position += current_card.rank.value
                current_card = deck.cards[card_position]
                history.append(current_card)
            else:
                card_position += 5
                current_card = deck.cards[card_position]
                history.append(current_card)
        except IndexError:
            break
    return history


print(kruskal_count(deck, 5)[-1])
