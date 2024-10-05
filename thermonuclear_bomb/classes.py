import random, sys, time

# slow type
def type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10 / 2500)
    print()

# Get input function
def get_input(prompt, valid_options=None, validation_fn=None, error_message="Invalid input. Please try again."):
    while True:
        # Get user input
        user_input = input(f"{prompt} ").strip().lower()

        # check if input is in the valid_options array
        if valid_options and user_input in valid_options:
            return user_input
        # Validate the input using the provided function
        elif validation_fn and validation_fn(user_input):
            return user_input
        # Return error message
        else:
            type(error_message)

class Room:
    def __init__(self, name, ingredient=None):
        self.name = name
        self.ingredient = ingredient

class Game:
    def __init__(self, rooms, ingredients):
        self.rooms = [Room(name) for name in rooms]
        self.ingredients = ingredients
        self.rooms_already_been_to = []
        self.ingredients_fetched = []

        # check if enough rooms are available for all the ingredients
        if len(self.rooms) < len(self.ingredients):
            type("There are not enough rooms for all of the ingredients. Add more rooms or remove some ingredients.")
            exit()

        remaining_ingredients = self.ingredients[:]
        random.shuffle(self.rooms)

        for room in self.rooms:
            if remaining_ingredients:
                room.ingredient = remaining_ingredients.pop()

    def play(self):
        type("Welcome to the make-a-thermonuclear-bomb game!")
        type("In this game, you make a thermonuclear bomb and can blow up the United States!")

        type(f"\nYou need to find all {len(self.ingredients)} ingredients:")
        type(("- ", "\n- ".join(self.ingredients)))

        type(f"\nThere are {len(self.rooms)} rooms:")
        type(("- ", "\n- ".join([room.name for room in self.rooms])))
        print()

        while len(self.ingredients_fetched) < len(self.ingredients):
            # Show list of rooms the user hasn't searched
            self.show_rooms_left()

            # Get the room the user wants to go to
            current_room_name = get_input("Which room do you want to go to?", [room.name for room in self.rooms])

            # Get the current room
            current_room = next(room for room in self.rooms if room.name == current_room_name)

            # Check if the user has already been in the room
            if current_room.name in self.rooms_already_been_to:
                type(f"You've already been to the {current_room.name} and found {current_room.ingredient} there.")
            else:
                # Check if the user has found an ingredient
                if current_room.ingredient:
                    type(f"You found {current_room.ingredient} in the {current_room.name}!")
                    self.ingredients_fetched.append(current_room.ingredient)
                else:
                    type(f"There's nothing useful in the {current_room.name}.")

                # Add the room to the list of the rooms the user has already been in
                self.rooms_already_been_to.append(current_room.name)

            # Show rest of the ingredients
            self.show_ingredients_left()

        # Finish the game
        self.finish_game()

    def show_rooms_left(self):
        # Get the remaining rooms
        remaining_rooms = [room.name for room in self.rooms if room.name not in self.rooms_already_been_to]

        if remaining_rooms:
            type(f"\nRooms you haven't been to yet: {", ".join(remaining_rooms)}\n")

    def show_ingredients_left(self):
        # Get the remaining ingredients to find
        remaining_ingredients = [ing for ing in self.ingredients if ing not in self.ingredients_fetched]

        if remaining_ingredients:
            type(f"\nYou still need to find: {", ".join(remaining_ingredients)}")

    def finish_game(self):
        type("\nCongratulations! You've found all the ingredients!")
        make_bomb = get_input("\nDo you want to assemble the thermonuclear bomb?", ["yes", "y", "no", "n"])

        # Assemble the bomb if the user agreed
        if make_bomb in ["yes", "y"]:
            self.assemble_bomb()
        else:
            type("\nYou decided not to assemble the bomb. Maybe that's for the best. You win the game!")

        type("\nThank you for playing the make-a-thermonuclear-bomb game!")
        type("See you next time!")

    def assemble_bomb(self):
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

        type("\nYou have assembled the thermonuclear bomb!")

        # Select a random state to nuke
        state = random.choice(states)

        # Ask user if they want nuke the state
        launch = get_input(f"\nDo you launch it and nuke {state}, United States?", ["yes", "y", "no", "n"])

        # Launch the bomb if the user agreed
        if launch in ["yes", "y"]:
            type(f"\nYou launched the bomb to {state}, United States. The thermonuclear bomb killed {random.randint(1000000, 9999999)} people. You are now a war criminal and lost the game :(")
        else:
            type(f"\nYou didn't launch the bomb. You saved {random.randint(1000000, 9999999)} people who lived in {state}, United States! You win the game!")

# Define rooms and ingredients
rooms = [
    "bathroom",
    "bedroom",
    "playroom",
    "kitchen",
    "basement",
    "garage",
    "attic",
    "living room",
    "library",
    "office",
    "garden",
    "laundry",
    "backyard",
    "games room",
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

# Start the game
game = Game(rooms, ingredients)
game.play()
