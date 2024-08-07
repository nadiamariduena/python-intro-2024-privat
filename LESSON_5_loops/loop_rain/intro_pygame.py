# 1
import pygame
# 2
pygame.init()
# 3
# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 4 create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
#
# the rect() function, similar to canvas i guess https://www.w3schools.com/jsref/canvas_rect.asp


# 11 create the tool to draw (outside of the loop), the functioning tool logic, will be added within the WHILE loop after this.
#
#
# we want to draw as a small box on the screen. To decide where this box will go, we use four numbers:  is like saying: “Put a small box that’s 50 steps wide and 50 steps tall, starting 300 steps from the left and 250 steps down from the top of the screen.
player = pygame.Rect((300, 250, 50, 50))
#300, 250:  a bit towards the center of the screen


# 5 create a variable that is going to be used for the condition on the WHILE LOOP
run = True

#------------- GAME LOOP
# 6 WHILE 'run' is  (equal to true) ':' execute all the code below
while run:
    # Note: The while loop contains a nested for loop, so make sure to keep an eye on the indentation.

    # 12 THE TOOL: contain 3 arguments, the screen , the rgb and the player who is going to draw
    pygame.draw.rect(screen, (255, 0, 0), player)


    #------------- EVENT handler
    for event in pygame.event.get():
        # 7 This for loop goes through all the events that Pygame has collected.

        # We can examine each event individually to find specific ones.

        # For simplicity, we are only interested in the event that allows us to close the game window,

        # which is triggered by clicking the X in the top-right corner of the screen.


        # 8 We can detect this event with an if statement.
        if event.type == pygame.QUIT:
            # 9 If the condition is true (i.e., the QUIT event is detected),
            # we set 'run' to False to exit the while loop, effectively closing the game.
            run = False

    # 13 Think of pygame.display.update() as a final step to show what you’ve drawn.
    pygame.display.update()
    # the purpose is to refresh or update the screen with any changes that have been made.

#-------------
# 10 at this point we can run the game (which is only a black window for now)
pygame.quit()