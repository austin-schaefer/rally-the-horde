import random
output_file = open("output.csv", "a")

test_for_rally_the_horde = False

# Function for counting
def count(iteratble):
    return sum(1 for _ in iterable)

# Create the deck (with Rally the Horde)
deck = []
for _ in range(17):
    deck.append("Land")
if test_for_rally_the_horde == True:
    for _ in range(22):
        deck.append("Spell")
    deck.append("Rally the Horde")
if test_for_rally_the_horde == False:
    for _ in range(23):
        deck.append("Spell")
random.shuffle(deck)

# Draw cards into "hand" until it has 7 lands
hand=[]
lands = 0
while lands < 7:
    hand.append(deck[0])
    if deck[0] == "Land":
        lands += 1
    deck.pop(0)

# If Rally the Horde isn't in our hand, draw until it is
if test_for_rally_the_horde == True:
    while "Rally the Horde" not in hand:
        hand.append(deck[0])
        deck.pop(0)

# Debugging output
#print("Initial hand:", hand)
#print("Initial deck:", deck)
#print("\n")

# variables for rally the horde functions
warriors = 0
end_the_rally = False
decked_ourselves = False

# Tests top card of deck to see if it's a spell
def rally_test():
    global warriors
    if deck[0] == "Spell":
        warriors += 1
    deck.pop(0)

# Cast Rally the Horde
while end_the_rally == False:
    # If there are less than 3 cards at the start, we decked ourselves
    if len(deck) <= 3:
        while len(deck) > 0:
            rally_test()
        decked_ourselves = True
        end_the_rally = True
    # Run an iteration
    if len(deck) > 3:
        rally_test()
        rally_test()
        if deck[0] == "Land":
            end_the_rally = True
        rally_test()
    # Print some debug stuff
    #print("Current deck:", deck)
    #print("  Warrior count:", warriors)
    #print("  Cards left in deck:", len(deck))

#print("Final warrior count:", warriors)
#print("Final deck count:", len(deck))
#print("Did we deck ourselves:", decked_ourselves)
# print(warriors, len(deck), decked_ourselves, sep=",")

# Output results
results = ''.join([str(warriors),",", str(len(deck)),",", str(decked_ourselves)])
print(results)
output_file.write(results)