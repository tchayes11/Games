#create the game of war

import random

print("Welcome")

def generate_deck(suits = 4, typeCards =13):
    cards = []
    for suite in range(suits):
        for typeCard in range(1,typeCards + 1):
            cards.append(typeCard)
        random.suffle(cards)
        return cards


def play_card(deck):
    a_cards = deck[:len(deck)/2]
    b_cards= deck[len(deck)/2:]
    a_stash =[]
    b_stash =[]

    num = 1
    while a_cards and b_cards:
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        if a_card == b_card:
            a_stash.extend([a_card]+ a_cards[-3:])
            a_cards = a_cards[:-3]
            a_cards.append(a_stash.pop())






