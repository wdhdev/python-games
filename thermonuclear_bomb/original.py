import random, sys, time

def type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10 / 2500)
    print()

# Define rooms
rooms = [
    "bathroom",
    "bedroom",
    "playroom",
    "kitchen",
    "basement",
    "garage",
    "attic",
    "living room",
    "office",
    "garden",
    "laundry",
    "backyard",
    "games room",
    "library",
    "study"
]

ingredients = [
    "uranium-235",
    "neutron reflector",
    "high explosive charge",
    "deuterium",
    "lead",
    "lithium-6"
]

if len(rooms) < len(ingredients):
    type("There are not enough rooms for all of the ingredients. Add more rooms or remove some ingredients.")
    exit()

rooms_already_been_to = []
ingredients_fetched = []

# Randomly assign ingredients to rooms
room_ingredient_mapping = {}
remaining_ingredients = ingredients[:]
random.shuffle(rooms)

for room in rooms:
    if remaining_ingredients:
        ingredient = remaining_ingredients.pop()
        room_ingredient_mapping[room] = ingredient

# Shuffle again so the rooms are actually random
random.shuffle(rooms)

type("Welcome to the make-a-thermonuclear-bomb game!")
type("In this game, you make a thermonuclear bomb and can blow up the United States!")

# Get input function
def get_input(prompt, valid_options=None, validation_fn=None, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(f"{prompt} ")

        # Convert to lowercase
        user_input = user_input.lower()

        if valid_options and user_input in valid_options:
            return user_input
        elif validation_fn and validation_fn(user_input):
            return user_input
        elif not valid_options and not validation_fn:
            return user_input
        else:
            type(error_message)

type(f"\nYou need to find all {len(ingredients)} ingredients:")
type(("- ", "\n- ".join(ingredients)))
type(f"\nThere are {len(rooms)} rooms:")
type(("- ", "\n- ".join(rooms)))
print()

# Continue searching for ingredients if the user hasn't found them all
while len(ingredients_fetched) < len(ingredients):
    # Get remaining rooms
    remaining_rooms = [room for room in rooms if room not in rooms_already_been_to]

    # If it isn't the first run, print the rooms the user hasn't been to yet
    if len(remaining_rooms) != len(rooms):
        type(f"\nRooms you haven't been to yet: {", ".join(remaining_rooms)}\n")

    current_room = get_input("Which room do you want to go to?", remaining_rooms)

    if current_room in rooms_already_been_to:
        type(f"You've already been to the {current_room} and found {room_ingredient_mapping[current_room]} there.")
    else:
        # Check if the room contains an ingredient
        if current_room in room_ingredient_mapping:
            ingredient_found = room_ingredient_mapping[current_room]
            type(f"You found {ingredient_found} in the {current_room}!")
            ingredients_fetched.append(ingredient_found)
        else:
            type(f"There's nothing useful in the {current_room}.")

        # Add the room the user has already been to, to the array
        rooms_already_been_to.append(current_room)

    # Get remaining ingredients
    remaining_ingredients = [ing for ing in ingredients if ing not in ingredients_fetched]

    if remaining_ingredients:
        type(f"\nYou still need to find: {", ".join(remaining_ingredients)}")

type("\nCongratulations! You've found all the ingredients!")

make_bomb = get_input("\nDo you want to assemble the thermonuclear bomb?", ["yes", "y", "no", "n"])

states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

if make_bomb == "yes" or make_bomb == "y":
    type("\nYou have assembled the thermonuclear bomb!")

    state = random.choice(states)

    launch = get_input(f"\nDo you launch it and nuke {state}, United States?", ["yes", "y", "no", "n"])

    if launch == "yes" or launch == "y":
        type(f"\nYou launched the bomb to {state}, United States. The thermonuclear bomb killed {random.randint(1000000, 9999999)} people, you are now a war criminal and lost the game :(")
    else:
        type(f"\nYou didn't launch the bomb. You saved {random.randint(1000000, 9999999)} people who lived in {state}, United States! You win the game!")
else:
    type("\nYou decided not to assemble the bomb. Maybe that's for the best. You win the game!")

type("\nThank you for playing the make-a-thermonuclear-bomb game!")
type("See you next time!")
