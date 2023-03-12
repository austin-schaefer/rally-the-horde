import random

# Function for counting
def count(iteratble):
    return sum(1 for _ in iterable)

# Create the deck
deck = []
for _ in range(17):
    deck.append("L")
for _ in range(23):
    deck.append("S")
random.shuffle(deck)

# Draw cards into "hand" until it has 7 lands
hand=[]
lands = 0
while lands < 7:
    hand.append(deck[0])
    if deck[0] == "L":
        lands += 1
    deck.pop(0)

# Debugging output
print("Initial hand:", hand)
print("Initial deck:", deck)
print("\n")

# Tests top card of deck to see if it's a spell
warriors = 0
end_the_rally = False
decked_ourselves = False
def rally_test():
    global warriors
    if deck[0] == "S":
        warriors += 1
    deck.pop(0)

# Cast Rally the Horde
while end_the_rally == False:
    # Test if first card is spell
    rally_test()
    rally_test()
    if deck[0] == "L":
        end_the_rally = True
    rally_test()
    print("Current deck:", deck)
    print("  Warrior count:", warriors)
    print("  Cards left in deck:", len(deck))
    if len(deck) <= 3:
        decked_ourselves = True
        end_the_rally = True

print("Final warrior count:", warriors)
print("Final deck count:", len(deck))
print("Did we deck ourselves:", decked_ourselves)