import random

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣

deck =[]
for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
    for rank in range(2,11):
        deck.append((str(rank), suit))
    for rank in ('J', 'Q', 'K', 'A'):
        deck.append((str(rank), suit))

print(deck)
random.shuffle(deck)
print(deck)
