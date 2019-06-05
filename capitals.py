# an array of state dictionaries
import random

# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]

states = [
{
    "name": "Alabama",
    "capital": "Montgomery",
    "correct": 0,
    "incorrect": 0
}, {
    "name": "Alaska",
    "capital": "Juneau",
    "correct": 0,
    "incorrect": 0
}, {
    "name": "Arizona",
    "capital": "Phoenix",
    "correct": 0,
    "incorrect": 0
}, {
    "name": "Arkansas",
    "capital": "Little Rock",
    "correct": 0,
    "incorrect": 0
}, {
    "name": "California",
    "capital": "Sacramento",
    "correct": 0,
    "incorrect": 0
}, {
    "name": "Colorado",
    "capital": "Denver",
    "correct": 0,
    "incorrect": 0
}]


# Welcome
print("""
*******************************************************************************
Welcome to *Learn Your Capitals*! You will be given a random state and asked to
correctly guess its capital city. Please type your answer into the terminal
window and remember that your answer is case sensitive (this includes trailing
and leading spaces)! Best of luck!
******************************************************************************* \n
""")


# Shuffle states
random.shuffle(states)
list_length = len(states)

# counter for in/correct guesses
correct_guesses = 0
incorrect_guesses = 0

game_state = True
game_session = 0

def wrong_sort(state):
    return state["incorrect"]

while game_state:
    game_session += 1
    # Iterate through states
    for index in range(list_length):
        state_name = states[index]["name"]
        state_capital = states[index]["capital"]
        print(f"State: {index+1} out of {list_length}")

        # checks to see if a state has any incorrect guesses; if yes, then display hint
        lose_record = states[index]["incorrect"]
        hint = states[index]["capital"][:3]
        if lose_record > 0:
            print(f"Hint: The {state_name}'s capital begins with {hint}...")

        user_guess = input(f"Guess the capital of {state_name}: ")
        # let the user quit whenever they want
        if user_guess == "quit":
            break

        if user_guess == states[index]["capital"]:
            correct_guesses += 1
            states[index]["correct"] += 1
            win_record = states[index]["correct"]
            print(f"You got it right! The capital of {state_name} is {state_capital}. Your guess was {user_guess}.")
            print(f"""You have played the game {game_session} times. 
In that time, you have guessed {state_name}'s capital correctly {win_record} times.""")
        else:
            incorrect_guesses += 1
            states[index]["incorrect"] += 1
            print(f"You got it wrong! The capital of {state_name} is {state_capital}. Your guess was {user_guess}.")

        print(f"You have guessed {correct_guesses} out of {index+1} right so far. \n")

    user_continue = input("Would you like to play again? (Yes/No) ").lower()
    if user_continue == "yes":
        game_state = True
        random.shuffle(states)
        states.sort(reverse=True, key=wrong_sort)
        correct_guesses = 0
        incorrect_guesses = 0
    else:
        game_state = False
        #todo print out the list of states you guessed the capital wrong on 
print("You have exited the game!")

# print(f"Your got {correct_guesses} out of {list_length} correct.")


































