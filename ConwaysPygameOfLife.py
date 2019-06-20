"""
 Written by Robert De La Cruz II, based on Conway's Game of Life
 Rules found at https://study.com/academy/lesson/conways-game-of-life-rules-instructions.html
    1. Birth: Any dead cell with 3 live neighbors will come to life in the next generation
    2. Death by Isolation: Any live cell with 1 or fewer neighbors will die in the next generation
    3. Death by Overciding: Any live cell with 4 or more neighbors will die in the next generation
    4. Survival: Any cell with 2 or 3 living neighbors will remain alive in the next generation

 The grid for this will wrap around

 Code Sources:
 https://www.geeksforgeeks.org/conways-game-life-python-implementation/
 http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py
 https://docs.python.org/3/library/random.html
 https://stackoverflow.com/questions/15884527/how-can-i-prevent-the-typeerror-list-indices-must-be-integers-not-tuple-when-c

 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
 
import pygame
import random
 

# Combination or ease variables.
tickTock = 60                         # Clock speed AKA Number of loops per second
gridSize = 100                       # Bringing all the grid related variables into a unified variable, the rest is simple math.
seedOfLife = 15                     # Sets the upper bound of the random.randint that is called to decide which cells are seeded. The chance of life is 1/seedOfLife
BACKGROUND = (0, 0, 0)      # For setting a background color without a visible grid in a single variable

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define states on/off These are used for checking the states of the surrounding cells
ON = 1
OFF = 0
vals = [ON, OFF]

# This sets the WIDTH, HEIGHT and MARGIN of each grid location
WIDTH = 5
HEIGHT = 5
MARGIN = 1
 
# Create a 2 dimensional array. A two dimensional array is simply a list of lists.
grid = []
nextGrid = []

for i in range(gridSize):
    # Add an empty array that will hold each cell in this i
    grid.append([])
    nextGrid.append([])
    for j in range(gridSize):
        grid[i].append(0)  # Append a cell
        nextGrid[i].append(0)


# Seed the grid with life
for i in range(gridSize):
    for j in range(gridSize):
            if  (random.randint(1,seedOfLife) is int(seedOfLife/2)):
                nextGrid[ i ][ j ] = ON

# Seed the nextGrid, currently both of them are identical
grid = nextGrid

# The game code (runtime logic) starts here
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [gridSize*(WIDTH+MARGIN), gridSize*(HEIGHT+MARGIN)]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Conway's Pygame of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True                            # Flag that we are done so we exit this loop
 
    # Set the screen background color (Grid lines)
    screen.fill(BACKGROUND) 
 
    # Copy grid into nextGrid
    nextGrid = grid.copy()

    # Comparisons are made on grid. Changes made to nextGrid.
    for i in range(gridSize):
        for j in range(gridSize):
            color = BACKGROUND
            total = ( (     grid[ i ] [ ( j - 1 ) % gridSize ] +                                               # To the Top
                                grid[ i ] [ (  j + 1 ) % gridSize ] +                                             # To the Bottom
                                grid[ ( i - 1 ) % gridSize] [ j ] +                                                # To the Left 
                                grid[ ( i + 1 ) % gridSize] [ j ] +                                               # To the Right
                                grid[ ( i - 1 ) % gridSize] [ ( j - 1 ) % gridSize ] +                     # Below and to the Left
                                grid[ ( i - 1 ) % gridSize] [ ( j +1 ) % gridSize ] +                     # Above and to the Left
                                grid[ ( i + 1 ) % gridSize] [ ( j - 1 ) % gridSize ] +                    # Below and to the Right
                                grid[ ( i + 1 ) % gridSize] [ ( j +1 ) % gridSize ] ) )                   # Above and to the Right

            # Conway's rules
            if (grid[ i ][ j ] == ON):                      # If alive
                if (total < 2) or (total > 3):            # And it is Isolated or Overcrowded
                    nextGrid[ i ][ j ] = OFF               # It dies
                    color = BACKGROUND
            else:                                                   # If dead
                    if total == 3:                              # And the number of living adjacent cells is 3
                        nextGrid[ i ][ j ] = ON            # It comes to life
                        color = GREEN

            # Copy nextGrid, with its updated info, onto grid.
            grid = nextGrid.copy()
            
            # This redraws the grid every time
            pygame.draw.rect( screen,
                             color,
                             [ ( MARGIN + WIDTH ) * j + 
                             MARGIN, ( MARGIN + HEIGHT ) * i + 
                              MARGIN, WIDTH, HEIGHT ] )

     # --- Limit frames per second (Number of next generations per second)
    clock.tick(tickTock)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()
 