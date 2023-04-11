# define Cards
import random


def card_group(groups: int, jokes: int):
    # cards = [c for ]
    cards = []
    for c in ['A', 'B', 'C', 'D']:
        for n in range(1, 14):
            cards.append('{}{}'.format(c, str(n)))
    cards *= groups
    for j in range(jokes):
        cards.append('joke')
    return cards


cards = card_group(2, 2)


def send_cards(players: int, num: int):
    players_cards = []
    random.shuffle(cards)
    for i in range(players):
        players_cards.append(sorted(random.sample(cards, num)))
    return players_cards
