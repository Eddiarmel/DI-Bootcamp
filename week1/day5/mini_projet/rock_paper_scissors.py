from game import Game

def get_user_menu_choice():
    print("\nMenu principal :")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("x. Quitter")

    choice = input("Votre choix: ").lower()
    if choice in ["1", "2", "x"]:
        return choice
    else:
        print("Choix invalide.")
        return None

def print_results(results):
    print("\nRésumé des parties :")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Nuls : {results['draw']}")
    print("Merci d'avoir joué ! 👋")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        elif choice == "x":
            print_results(results)
            break

if __name__ == "__main__":
    main()
