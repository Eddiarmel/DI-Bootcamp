import random

class Game:
    def get_user_item(self):
        # Ask the user until they give a valid input
        while True:
            user_item = input("Choose (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid input. Try again.")

    def get_computer_item(self):
        # Random choice for the computer
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        # Determine the result
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("You won!")
        elif result == "loss":
            print("You lost.")
        else:
            print("It's a draw.")

        return result
