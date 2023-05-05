class TextBasedAdventureGame:
    def __init__(self):
        self.game_active = True

    def display_intro(self):
        """Display the introductory message for the game."""
        print("Welcome to the Text-based Adventure Game!")
        print("You find yourself at the entrance of a dark cave.")
        print("You have two options: (1) Enter the cave, (2) Walk away.")

    def get_user_input(self, prompt):
        """Prompt the user for input and return the input."""
        return input(prompt)

    def handle_intro(self, choice):
        """Handle the user's choice at the game's introduction."""
        if choice == "1":
            self.enter_cave()
        elif choice == "2":
            self.walk_away()
        else:
            print("Invalid input. Please enter 1 or 2.")
            self.main()

    def enter_cave(self):
        """Handle the user's decision to enter the cave."""
        print("\nYou enter the cave and notice two paths.")
        print("You can either (1) Take the left path or (2) Take the right path.")
        choice = self.get_user_input("Enter the number of your choice: ")
        self.handle_cave(choice)

    def handle_cave(self, choice):
        """Handle the user's choice inside the cave."""
        if choice == "1":
            self.left_path()
        elif choice == "2":
            self.right_path()
        else:
            print("Invalid input. Please enter 1 or 2.")
            self.enter_cave()

    def left_path(self):
        """Outcome when the user takes the left path."""
        print("\nYou take the left path and encounter a treasure chest!")
        print("Congratulations, you found the treasure! You win!")
        self.play_again()

    def right_path(self):
        """Outcome when the user takes the right path."""
        print("\nYou take the right path and fall into a pit of spikes!")
        print("Unfortunately, you didn't survive. Game over.")
        self.play_again()

    def walk_away(self):
        """Outcome when the user decides to walk away from the cave."""
        print("\nYou decide to walk away, never knowing the adventure that awaits.")
        print("Thanks for playing!")
        self.play_again()

    def play_again(self):
        """Prompt the user to play again or quit the game."""
        choice = self.get_user_input("\nDo you want to play again? (yes or no): ")
        self.handle_play_again(choice)

    def handle_play_again(self, choice):
        """Handle the user's decision to play again or quit."""
        if choice.lower() == "yes":
            self.main()
        elif choice.lower() == "no":
            print("Thanks for playing! Goodbye!")
            self.game_active = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.play_again()

    def main(self):
        """Main game loop."""
        self.display_intro()
        choice = self.get_user_input("Enter the number of your choice: ")
        self.handle_intro(choice)

# Game start from here !
if __name__ == "__main__":
    game = TextBasedAdventureGame()
    while game.game_active:
        game.main()