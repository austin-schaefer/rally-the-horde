import random

# Create the deck
deck=[]
for _ in range(17):
    deck.append("Land")
for _ in range(23):
    deck.append("Spell")
random.shuffle(deck)

# Print the deck
print(deck)