import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds?: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):
    while True:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

mode = "regular"

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0
choose_instruction = "Please choose rock (r), paper" \
                     "(p) or scissors (s)"

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:

    print()
    if mode == "infinite":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
        rounds += 1

    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)
    # choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    user_choice = choice_checker(f"{choose_instruction} or 'xxx' to quit: ", rps_list, "Please enter R / P / S")

    #  get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "Lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)
    if user_choice == "xxx":
        break

    print(feedback)

    rounds_played += 1

# Show game statistics
rounds_won = rounds_played - rounds_lost - rounds_drawn

print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")



