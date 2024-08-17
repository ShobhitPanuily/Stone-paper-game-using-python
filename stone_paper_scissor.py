import tkinter as tk
from PIL import Image, ImageTk
import random
import os

class StonePaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Expert Stone-Paper-Scissors Game")

        # Initialize scores
        self.player_score = 0
        self.computer_score = 0

        # Define the path to the images folder
        self.images_folder = os.path.join(os.path.dirname(__file__), 'images')

        # Load and resize images
        self.image_size = (200, 200)  # Define a consistent size for all images
        self.images = {
            "stone": ImageTk.PhotoImage(Image.open(os.path.join(self.images_folder, "stone.png")).resize(self.image_size)),
            "paper": ImageTk.PhotoImage(Image.open(os.path.join(self.images_folder, "paper.png")).resize(self.image_size)),
            "scissor": ImageTk.PhotoImage(Image.open(os.path.join(self.images_folder, "scissor.png")).resize(self.image_size)),
            "blank": ImageTk.PhotoImage(Image.open(os.path.join(self.images_folder, "blank.png")).resize(self.image_size))  # For initial state
        }

        # Set up the layout frames
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(side="top", pady=(0, 20))

        self.center_frame = tk.Frame(self.main_frame)
        self.center_frame.pack(side="top", pady=20)

        self.bottom_frame = tk.Frame(self.main_frame)
        self.bottom_frame.pack(side="bottom", pady=(20, 0))

        # Labels for displaying hands
        self.player_hand_label = tk.Label(self.center_frame, image=self.images["blank"])
        self.player_hand_label.pack(side="left", padx=20)

        self.computer_hand_label = tk.Label(self.center_frame, image=self.images["blank"])
        self.computer_hand_label.pack(side="right", padx=20)

        # Labels for displaying choices
        self.computer_choice_label = tk.Label(self.bottom_frame, text="Computer: ?", font=('Arial', 14))
        self.computer_choice_label.pack(pady=10)

        # Score labels
        self.score_label = tk.Label(self.top_frame, text="Player: 0 | Computer: 0", font=('Arial', 18))
        self.score_label.pack()

        # Buttons for user to choose Stone, Paper, or Scissor
        self.stone_button = tk.Button(self.bottom_frame, text="Stone", width=10, command=lambda: self.play("stone"))
        self.stone_button.pack(side="left", padx=10, pady=10)

        self.paper_button = tk.Button(self.bottom_frame, text="Paper", width=10, command=lambda: self.play("paper"))
        self.paper_button.pack(side="left", padx=10, pady=10)

        self.scissor_button = tk.Button(self.bottom_frame, text="Scissor", width=10, command=lambda: self.play("scissor"))
        self.scissor_button.pack(side="left", padx=10, pady=10)

        # Reset button
        self.reset_button = tk.Button(self.bottom_frame, text="Reset", width=15, command=self.reset_game)
        self.reset_button.pack(pady=10)

    def play(self, player_choice):
        computer_choice = random.choice(["stone", "paper", "scissor"])

        # Update hand images
        self.player_hand_label.config(image=self.images[player_choice])
        self.computer_hand_label.config(image=self.images[computer_choice])

        # Update computer choice label
        self.computer_choice_label.config(text=f"Computer: {computer_choice.capitalize()}")

        # Determine result
        result = self.get_result(player_choice, computer_choice)
        if result == "Win":
            self.player_score += 1
        elif result == "Lose":
            self.computer_score += 1

        # Update score label
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")

    def reset_game(self):
        # Reset the game to initial state
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text="Player: 0 | Computer: 0")
        self.player_hand_label.config(image=self.images["blank"])
        self.computer_hand_label.config(image=self.images["blank"])
        self.computer_choice_label.config(text="Computer: ?")

    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Draw"
        elif (player_choice == "stone" and computer_choice == "scissor") or \
             (player_choice == "paper" and computer_choice == "stone") or \
             (player_choice == "scissor" and computer_choice == "paper"):
            return "Win"
        else:
            return "Lose"

# Main execution
root = tk.Tk()
game = StonePaperScissorsGame(root)
root.mainloop()
