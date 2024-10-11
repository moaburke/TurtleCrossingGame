"""
Turtle Crossing Game

Author: Moa Burke
Date: 11 Oct 2024
Description:
        This module defines the Player class for a Turtle Crossing Game, inheriting from the Turtle class.
        The Player class represents the player's turtle and includes methods to control its movement,
        reset its position, and check for successful crossing.

Version: 1.0

Changelog:
- v1.0.0:   Initial release of the Player class, featuring movement controls and crossing detection.
"""

from turtle import Turtle

# Game constants
STARTING_POSITION = (0, -280) # Starting position of the player's turtle
MOVE_DISTANCE = 10 #  Distance the player's turtle moves per key press
FINISH_LINE_Y = 280 # Y-coordinate for the finish line
PLAYER_COLOR = "honeydew3" # Player turtle color
PLAYER_SHAPE = "turtle" # Player turtle shape

class Player(Turtle):
    def __init__(self):
        super().__init__() # Initialize the parents Turtle class
        self.FINISH_LINE_Y = FINISH_LINE_Y # Set the finish line y-coordinate
        self.shape(PLAYER_SHAPE) # Set the shape of the turtle
        self.color(PLAYER_COLOR) # Set the color of the turtle
        self.penup() # Prevent the turtle from drawing a line when moving
        self.starting_position() # Move the turtle to its starting position
        self.left(90)  # Turn turtle 90 deg to face upwards

    def starting_position(self):
        """
        Resets the player's position to the starting coordinates.
        """
        self.goto(STARTING_POSITION) # Move turtle to its starting position

    def move_forward(self):
        """
        Moves the player forward by a defined distance.
        """
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        """
        Moves the player backward by a defined distance.
        """
        self.backward(MOVE_DISTANCE)

    def successful_crossing(self):
        """
        Checks if the player has successfully crossed the finish line.

        Returns:
            bool: True if the player has crossed the finish line, False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y: # Checks if the player's y-coordinate is above the finish line
            return True # Return False if the player has not crossed

