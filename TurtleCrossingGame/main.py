"""
Turtle Crossing Game

Author: Moa Burke
Date: 11 Oct 2024
Description: This program implements the Turtle Crossing game where the player controls a turtle that must cross a busy
road filled with moving obstacles (turtles). The player can move the turtle forward and backward using keyboard inputs.
The objective is to reach the finish line while avoiding collisions with the moving turtles. The game tracks the
player's level, high score, and provides feedback for successful crossing or game-over situations.

Version: 1.0

Changelog:
- v1.0.0 Initial release with basic gameplay functionality, including player movement, turtle creation, level
progression and score-keeping.
"""

from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from turtle_manager import TurtleManager
import time

# Game configuration constants
SCREEN_WIDTH = 600 # Width of thr game screen
SCREEN_HEIGHT = 600 # Height of the game screen
BACKGROUND_COLOR = (40, 40, 39) # Background color of the screen
TITLE = "Turtle Crossing by Moa Burke"

# Game control constants
MOVE_FORWARD_KEY = "Up" # Key to move the right paddle up
MOVE_BACKWARD_KEY = "Down" # Key to move the right paddle down
RESTART_KEY = "space" # Key to restart the game
EXIT_KEY = "Escape" # Key to end the game

# Game logic constants
INITIAL_TIME_SLEEP = 0.1
COLLISION_DISTANCE = 30 # Distance for deleting collision between player and turtles
GAME_OVER_DELAY = 1 # Delay after game over


def play_again():
    """
    Resets the game state to allow the player to start over.
    """
    global game_over_state
    scoreboard.reset()  # Reset the scoreboard to initial state
    player.starting_position()  # Reset the player to the starting position
    turtle_manager.reset()  # Clear all turtles and reset their speed
    game_over_state = False  # Reset the game-over flag to continue the game

def press_space_bar():
    """
    Handles the event of pressing the space bar to restart the game.

    If the game is in the "game over" state, this function triggers the 'play_again()'
    function to reset the game and start over.
    """
    if game_over_state:
        play_again()

def end_game():
    """
    Ends the game.
    """
    global game_is_on
    game_is_on = False

def move_turtle_forward():
    """
    Moves the player's turtle forward on the screen if the game is active.

    This function checks if the game is not in a "game over" state, and if so,
    it moves the player's turtle forward by calling the 'move_forward()' method.
    """
    if not game_over_state:
        player.move_forward()

def move_turtle_backward():
    """
    Moves the player's turtle backward on the screen if the game is active.

    This function checks if the game is not in a "game over" state, and if so,
    it moves the player's turtle backward by calling the 'move_backward()' method.
    """
    if not game_over_state:
        player.move_backward()


# Set up the screen for the game
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT) # Screen size
screen.colormode(255) # Set color mode to RGB for custom colors
screen.bgcolor(BACKGROUND_COLOR) # Set background color
screen.title(TITLE) # Set window title
screen.tracer(0) # Turn off the automatic animation to manually update the screen

# Create the player, scoreboard, and turtle manager
player = Player()
scoreboard = Scoreboard()
turtle_manager = TurtleManager()

# Allow the screen to listen for key presses
screen.listen()

# Game state variables
game_is_on = True # Main loop control variable
game_over_state = False # Flag to check if the game is in "game over" state

# Initial time delay between each screen update (controls speed of the game)
time_sleep = INITIAL_TIME_SLEEP

# Bind the space key to restart the game when it's over
screen.onkey(press_space_bar, RESTART_KEY)
# Bind the esc key to exit the game
screen.onkey(end_game, EXIT_KEY) # Exit the game on escape key press

# Main game loop
while game_is_on:
    time.sleep(time_sleep) # Pause for a short duration between frames
    screen.update() # Update the screen with the latest state

    if not game_over_state:
        # Create new turtles and move them
        turtle_manager.create_turtle()
        turtle_manager.move_turtles()

        #Detect key presses for moving the player's turtle
        screen.onkeypress(move_turtle_forward, MOVE_FORWARD_KEY) # Move forward on "Up" key press
        screen.onkeypress(move_turtle_backward, MOVE_BACKWARD_KEY)  # Move backward on "Down" key pres

        # Check if player has successfully crossed the screen
        if player.successful_crossing():
            player.starting_position() # Reset player's position
            scoreboard.increase_level() # Increase the level displayed on the scoreboard
            turtle_manager.increase_speed() # Increase the speed of the turtles

        # Check for collision with turtles
        for turtle in turtle_manager.turtle_list:
            if player.distance(turtle) < COLLISION_DISTANCE: # If the player is too close to a turtle
                scoreboard.game_over() # Display the "Game Over" message
                scoreboard.display_restart_message() # Prompt to restart the game
                time_sleep = INITIAL_TIME_SLEEP # Reset the game speed
                scoreboard.update_highscore() # Update the high score
                game_over_state = True # Set the game over state to stop the game loop
                break # Exit the loop early to stop processing
    else:
        pass # If the game is over, the game will wait for a space-bar press to reset
