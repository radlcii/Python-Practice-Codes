# Robert De La Cruz II making modifications to this to create Conway's Game of Life

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define states on/off
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
gridSize = 100 # Bringing all the grid related variables into a unified variable, the rest is simple math.
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
            if  (random.randint(1,10) is 5):
                nextGrid[ i ][ j ] = ON

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
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(WHITE)
 
    # Copy grid into nextGrid.  Comparisons are made on grid, changes made to nextGrid
    nextGrid = grid.copy()
    for i in range(gridSize):
        for j in range(gridSize):
            color = WHITE
            total = ( (     grid[ i ] [ ( j - 1 ) % gridSize ] +                                              # To the Top
                                grid[ i ] [ (  j + 1 ) % gridSize ] +                                             # To the Bottom
                                grid[ ( i - 1 ) % gridSize] [ j ] +                                                # To the Left 
                                grid[ ( i + 1 ) % gridSize] [ j ] +                                               # To the Right
                                grid[ ( i - 1 ) % gridSize] [ ( j - 1 ) % gridSize ] +                     # Below and to the Left
                                grid[ ( i - 1 ) % gridSize] [ ( j +1 ) % gridSize ] +                     # Above and to the Left
                                grid[ ( i + 1 ) % gridSize] [ ( j - 1 ) % gridSize ] +                    # Below and to the Right
                                grid[ ( i + 1 ) % gridSize] [ ( j +1 ) % gridSize ] ) )                   # Above and to the Right

            # Conway's rules
            if (grid[ i ][ j ] == ON):                      # If alive
                if (total < 2) or (total > 3):            # Check for death by Isolation or Overcrowding
                    nextGrid[ i ][ j ] = OFF               # It dies
                    color = WHITE
            else:                                                   # If dead
                    if total == 3:                              # And the magic birth number of 3 is present
                        nextGrid[ i ][ j ] = ON            # It comes to life
                        color = GREEN

            # copy nextGrid, with its updated info, onto grid.
            grid = nextGrid.copy()
            pygame.draw.rect( screen,
                             color,
                             [ ( MARGIN + WIDTH ) * j + 
                             MARGIN, ( MARGIN + HEIGHT ) * i + 
                              MARGIN, WIDTH, HEIGHT ] )

 
    """
    # Written by Robert De La Cruz II, based on Conway's Game of Life
    # Rules found at https://study.com/academy/lesson/conways-game-of-life-rules-instructions.html
    # 1. Birth: Any dead cell with 3 live neighbors will come to life in the next generation
             if (adjacent && alive == 3) { currentCell.activate() }
    
    # 2. Death by Isolation: Any live cell with 1 or fewer neighbors will die in the next generation
            else if (adjacent && alive < 2) { currentCell.deactivate() }

    # 3. Death by Overciding: Any live cell with 4 or more neighbors will die in the next generation
            else if (adjacent && alive > 3) { currentCell.deactivate() }

    # 4. Survival: Any cell with 2 or 3 living neighbors will remain alive in the next generation
            else { "Do nothing" }

    # The grid for this will wrap around

    # Variables
    gridSize = 300
    mainGrid = [gridSize,gridSize]
    nextGrid = [gridSize.gridSize] # As the name implies, this is for storing the main grid during calculations

    def nextGen():
        nextGrid = mainGrid

        for each cell in mainGrid_X-Axis 
            for each cell in mainGrid_Y-Axis
                if (adjacent && alive == 3)
                    currentCell.activate()
                else if (adjacent && alive < 2) 
                    currentCell.deactivate()
                else if (adjacent && alive > 3)
                    currentCell.deactivate()
                else
                    "Do nothing"
            
    # display( mainGrid )

    # Pause function
    def (onclick)
        while(true || oneGen)
            # Forward 1 generation
            oneGen = true
            # Forward
            break

    
    Repeat until program is closed
    """
     # --- Limit to 60 frames per second
    clock.tick(5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
 