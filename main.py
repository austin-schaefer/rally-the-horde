import random

# settings
output_file = open("output.csv", "a")
test_for_rally_the_horde = True
completed_iterations = 0
target_iterations = 10000

# Add headers to CSV
output_file.write("warriors,deck_count,did_we_deck_ourselves\n")

# Function for counting
def count(iteratble):
    return sum(1 for _ in iterable)

# the logic
while completed_iterations < target_iterations:
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

    # Output results
    results = ''.join([str(warriors),",", str(len(deck)),",", str(decked_ourselves),"\n"])
    output_file.write(results)
    
    completed_iterations += 1