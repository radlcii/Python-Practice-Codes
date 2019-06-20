# Robert De La Cruz II making modifications to this to create Conway's Game of Life

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    """
    # Written by Robert De La Cruz II, based on Conway's Game of Life
    # Rules found at https://study.com/academy/lesson/conways-game-of-life-rules-instructions.html
    # 1. Birth: Any dead cell with 3 live neighbors will come to life in the next generation
             if (adjacent && alive == 3) { currentCell.activate() }
    
    # 2. Death by Isolation: Any live cell with 1 or fewer neighbors will die in the next generation
            else if (adjacent && alive < 2) { currentCell.deactivate() }

    # 3. Death by Overcrowding: Any live cell with 4 or more neighbors will die in the next generation
            else if (adjacent && alive > 3) { currentCell.deactivate() }

    # 4. Survival: Any cell with 2 or 3 living neighbors will remain alive in the next generation
            else { "Do nothing" }

    # The grid for this will wrap around

    # Variables
    gridSize = 300
    mainGrid = [gridSize,gridSize]
    storageGrid = [gridSize.gridSize] # As the name implies, this is for storing the main grid during calculations

    def nextGen():
        storageGrid = mainGrid

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

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    """ display (mainGrid) """
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()