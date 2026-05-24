import random

class Game:
    def get_user_item(self):
        # Demander à l'utilisateur jusqu'à ce qu'il donne une entrée valide
        while True:
            user_item = input("Choisissez (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Entrée invalide. Essayez encore.")

    def get_computer_item(self):
        # Choix aléatoire pour l'ordinateur
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        # Déterminer le résultat
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

        print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}.")
        if result == "win":
            print("🎉 Vous avez gagné !")
        elif result == "loss":
            print("😢 Vous avez perdu.")
        else:
            print("🤝 Match nul.")

        return result

                    

         
             
    
             
             
             

