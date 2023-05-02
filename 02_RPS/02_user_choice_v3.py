# Functions go here
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

rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # Ask user for choice and check its valid
    user_choice = choice_checker("choice rock / paper/ scissors (r/p/s):", rps_list,
                                 "Please choose from rock / paper/ scissors (or xxx to quit)")

    # print out choice for comparison purposes
    print(f"You chose {user_choice }")
