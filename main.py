import random

# Function for counting
def count(iteratble):
    return sum(1 for _ in iterable)

# Create the deck
deck=[]
for _ in range(17):
    deck.append("L")
for _ in range(23):
    deck.append("S")
random.shuffle(deck)

# Variable for tracking which card we're on
current_card = 0

# Draw cards into "hand" until it has 7 lands
hand=[]
lands = 0
while lands < 7:
    hand.append(deck[current_card])
    if deck[current_card] == "L":
        lands += 1
    deck.pop(current_card)
    current_card += 1

# Debugging output
print("Initial hand:", hand)
print("Initial deck:", deck)
print("\n")

# Cast Rally the Horde
end_the_rally = False
warriors = 0
while len(deck) >= 3:
    while end_the_rally == False:
        # Test if first card is spell
        if deck[0] == "S":
            warriors += 1
        deck.pop(0)
        # Test if second card is spell
        if deck[0] == "S":
            warriors += 1
        deck.pop(0)
        if deck[0] == "S":
            warriors += 1
        if deck[0] == "L":
            end_the_rally = True
        deck.pop(0)
        print("Current deck:", deck)
        print("  End the rally:", end_the_rally)
        print("  Warrior count:", warriors)
        print("  Cards left in deck:", len(deck))

print(warriors)