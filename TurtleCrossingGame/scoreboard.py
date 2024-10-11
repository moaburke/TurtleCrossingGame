"""
Turtle Crossing Game

Author: Moa Burke
Date: 11 Oct 2024
Description:
        This module defines the Scoreboard class for a Turtle Crossing Game, inheriting from the Turtle class.
        It manages the display of the current level and high scorem handles the game over messages,
        and prompts for restarting or exiting the game.

Version: 1.0

Changelog:
- v1.0.0:   Initial release of the Scoreboard class with functionality to display levels and high scores.
            Implements methods for updating scores, displaying game over messages, and prompting for user actions.
"""

from turtle import Turtle

#Scoreboard appearance constants
TEXT_COLOR = "ivory"

# Font settings for the game display
FONTS = {
    "medium": ("Courier", 20, "normal"),
    "small": ("Courier", 12, "normal"),
    "game_over": ("Courier", 34, "normal"),
    "high_score": ("Courier", 14, "normal"),
}

# Message display positions
POSITIONS = {
    "level": (-275, 250),
    "high_score": (-275, 230),
    "game_over": (0, 0),
    "restart": (0, -240),
    "exit_game": (0, -270),
}

# File for high score data
DATA_FILE = "data.txt"
ALIGNMENT = "center"

# Game constants
STARTING_LEVEL = 1
LEVEL_INCREMENT = 1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__() # Initialize the parent Turtle class
        self.level = STARTING_LEVEL # Initialize the current level
        with open(DATA_FILE) as data:
            self.high_score = int(data.read()) # Read high score from the data file
        self.update_scoreboard() # Display the initial scoreboard

    def init_scoreboard(self):
        """
        Initialized the scoreboard's appearance
        Sets the turtles properties for displaying the scoreboard.
        """
        self.penup() # Prevent the turtle from drawing lines when moving
        self.hideturtle() # Hide the turtle cursor
        self.color(TEXT_COLOR) # Set the color of the text


    def update_scoreboard(self):
        """
        Clears the current scoreboard and updates it with the current level and high score.
        """
        self.clear() # Clear the previous scoreboard display
        self.init_scoreboard() # Reinitialize the scoreboard appearance
        self.setposition(*POSITIONS["level"]) # Position for current level
        self.write(f"Level: {self.level}", font=FONTS["medium"]) # Write the current level
        self.setposition(*POSITIONS["high_score"]) # Position for high score
        self.write(f"High Score: {self.high_score}", font=FONTS["high_score"]) # Write the high score

    def increase_level(self):
        """
        Increases the current level by LEVEL_INCREMENT and updates the scoreboard display.
        """
        self.level += LEVEL_INCREMENT # Increment the level
        self.update_scoreboard() # Update the scoreboard to reflect the new level

    def update_highscore(self):
        """

        """
        if self.level > self.high_score: # Check if the current level is a new high score
                self.high_score = self.level # Update the high score
                with open(DATA_FILE, mode="w") as data:
                    data.write(str(self.level)) # Write the new high score to the file

    def reset(self):
        """
        Resets the current level to 1 and updates the high score if the current level exceeds it.
        Saves the new high score to a file.
        """
        self.update_highscore()
        self.level = STARTING_LEVEL # Reset the level to 1
        self.update_scoreboard() # Update the scoreboard to reflect the reset

    def game_over(self):
        """
        Displays the 'GAME OVER' message at the center of the screen
        """
        self.setposition(*POSITIONS["game_over"]) # Position the game over message
        self.write("GAME OVER", align=ALIGNMENT, font=FONTS["game_over"]) # Write the game over message

    def display_restart_message(self):
        """
        Displays a message prompting the player to restart the game.
        """
        self.setposition(*POSITIONS["restart"])  # Position the restart message
        self.write("Press Space to restart", align=ALIGNMENT, font=FONTS["medium"])  # Write the restart message
        self.setposition(*POSITIONS["exit_game"])  # Position the exit game message
        self.write("Press Esc to exit game", align=ALIGNMENT, font=FONTS["small"])  # Write the exit game message
