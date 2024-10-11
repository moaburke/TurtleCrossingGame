"""
Turtle Crossing Game

Author: Moa Burke
Date: 11 Oct 2024
Description:
        This module defines the TurtleManager class for a Turtle Crossing Game, inheriting from the Turtle class.
        The TurtleManager is responsible for creating and managing turtle objects that move across the screen,
        adjusting their speed, and handling their spawning rate based on game progress.

Version: 1.0

Changelog:
- v1.0.0:   Initial release of the TurtleManager class with functionality to create, move and manage multiple turtles.
            Implements speed increments and spawn rate adjustments to enhance gameplay dynamics.
"""

import random
from turtle import Turtle

# Define a list of RGB colors to be used for the turtles
COLORS = [(242, 107, 56), (21, 168, 108), (252, 227, 7)]

# Game configuration constants
STARTING_MOVE_DISTANCE = 5 # Initial speed of the turtles
STARTING_SPAWN_RATE = 7 # Initial spawn rate (lower is more frequent)
MOVE_INCREMENT = 1 # Speed increase for the turtles
START_POS_X = 300 # Starting x-coordinates for turtles off-screen to the right

# Random Y-coordinate positioning range for turtles
Y_POS_MAX = 270
Y_POS_MIN = -230

# Turtle appearance and behavior constants
TURTLE_SHAPE = "turtle"
TURTLE_STRETCH_WID = 1.5 # Width stretch factor for turtles size
TURTLE_STRETCH_LEN = 1.5 # Length stretch factor for turtles size
TURTLE_ROTATION = 180 #Turtle face left by rotating 180 degrees

# Constants for controlling spawn rate adjustments
SPEED_INCREMENT_THRESHOLD = 3 # How often to decrease spawn rate (every 4 speed increment)
SPAWN_RATE_DECREMENT = 1 # How much to decrease the spawn rate by
SPAWN_CHANCE_LOWER_BOUND = 1 # Lower bound for random chance
MINIMUM_SPAWN_RATE = 1 # Ensure spawn rate doesn't go to low

# Off-screen coordinates for resetting turtles
OFFSCREEN_POSITION = 1000 # Position to send turtles off-screen


class TurtleManager(Turtle):
    def __init__(self):
        super().__init__() # Initialize the parent Turtle class
        self.hideturtle() # Hide the turtle since this will manage multiple turtles
        self.turtle_list = [] # List to store all created turtles
        self.speed = STARTING_MOVE_DISTANCE # Initialize turtle speed
        self.spawn_rate = STARTING_SPAWN_RATE # Control frequency of turtle creation (lower = more frequent)

    def create_turtle(self):
        """
        Create a new turtle based on a random change.
        Turtles are only created when random_chance equals 1.
        """
        # Generate a random number between 1 and spawn_rate
        random_chance = random.randint(SPAWN_CHANCE_LOWER_BOUND, self.spawn_rate)
        # Only create a turtle if random_chance equals 1
        if random_chance == 1:
            # Randomly selects a color from the COLORS list
            color = random.choice(COLORS)
            # Create a new turtle object to represent a turtle
            new_turtle = Turtle(TURTLE_SHAPE)
            new_turtle.color(color)
            new_turtle.penup()
            new_turtle.left(TURTLE_ROTATION) # Rotate to face left
            new_turtle.shapesize(stretch_wid=TURTLE_STRETCH_WID, stretch_len=TURTLE_STRETCH_LEN) # Adjust the size
            # Randomize the y-coordinate for the turtle's position within bounds
            random_y = random.randint(Y_POS_MIN, Y_POS_MAX)
            # Set the initial position of the turtle off the screen to the right
            new_turtle.goto(x=START_POS_X, y=random_y)
            # Add the new turtle to the list of turtles
            self.turtle_list.append(new_turtle)

    def move_turtles(self):
        """
        Move all turtles in the turtle_list to the left by a distance of 'self.speed'.
        """
        for turtle in self.turtle_list:
            turtle.forward(self.speed) # Move turtle forward (towards left on the screen)

    def increase_speed(self):
        """
        Increase the speed of all turtles and reduce spawn rate every 5 speed increment.
        """
        self.speed +=MOVE_INCREMENT # Increase speed by the increment value
        print(f"speed{self.speed}")
        print(f"spawn rate{self.spawn_rate}")
        # If speed is a multiple of SPEED_INCREMENT_THRESHOLD, reduce the spawn rate (more frequent turtle creation)
        if self.speed % SPEED_INCREMENT_THRESHOLD == 0:
            self.spawn_rate = max(MINIMUM_SPAWN_RATE, self.spawn_rate - SPAWN_RATE_DECREMENT) # Prevent from going below MINIMUM_SPAWN_RATE
            print(self.spawn_rate)

    def reset(self):
        """
        Reset the game by clearing all existing turtles and resetting the speed.
        """
        for turtle in self.turtle_list:
            # Move turtles off-screen
            turtle.goto(x=OFFSCREEN_POSITION, y=OFFSCREEN_POSITION)
        # Clear the list of turtles
        self.turtle_list.clear()
        # Reset the turtle speed to the starting value
        self.speed = STARTING_MOVE_DISTANCE
        # Reset the turtle spawn rate to the starting value
        self.spawn_rate = STARTING_SPAWN_RATE
