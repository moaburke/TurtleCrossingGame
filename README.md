# Turtle Crossing Game

## Description
The Turtle Crossing Game is a fun and interactive game where players control a turtle trying to cross a road filled with moving turtle obstacles.

## Classes

### Player Class
- Handles the player’s turtle movement on the screen.
- Moves forward and backward based on keyboard input.
- Resets to the starting position when needed.
- Checks if the turtle has successfully crossed the finish line.

### Scoreboard Class
- Displays the current level and high score on the screen.
- Updates the scoreboard whenever the player crosses the finish line.
- Increases the level after successful crossings.
- Saves the new high score to a file if the player surpasses it.
- Displays game over messages and restart instructions when the game ends.

### Game Class
- Manages the overall game logic and flow.
- Initializes the player and scoreboard classes.
- Contains the main game loop that checks for player inputs.
- Handles collisions with turtle obstacles and manages game-over conditions.
