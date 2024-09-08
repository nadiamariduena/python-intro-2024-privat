#🟡 with DT multiplication within the LOOP (check this * dt: line 131)


import pygame
import os
from random import randint


pygame.init()
script_dir = os.path.dirname(__file__)



WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")


#while loop related
running = True
#✋ CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()




# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}



player_surf = pygame.image.load(image_paths['player']).convert_alpha()




meteor_surf = pygame.image.load(image_paths['meteor']).convert_alpha()
laser_surf = pygame.image.load(image_paths['laser']).convert_alpha()

# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane at the center of the screen/window
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))

# start
star_surf = pygame.image.load(image_paths['star']).convert_alpha()
# star pos
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# 1. -----  move right to left loop  ---

#
##20 X, - 10Y axis
#🤚 VECTOR
player_direction = pygame.math.Vector2(1, 1) # This vector represents the direction and speed at which the player is moving:



# player speed
#🟡 actual movement
player_speed = 300
# -----  move right to left loop  ---

while running:


    # clock.tick(10) #✋
    # dt = clock.tick(120)
    # dt = clock.tick()
    # print(dt)
    # print(clock.get_fps())

    # frame rate / division
    dt = clock.tick(120) / 1000
    # print(dt)


    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False

    display_surface.fill("lavenderblush2")


    for pos in star_positions:
        display_surface.blit(star_surf, pos)


   # player
    display_surface.blit(player_surf, player_rect)

    # meteor
    display_surface.blit(meteor_surf, meteor_rect)
    # laser
    display_surface.blit(laser_surf, laser_rect)



    # CONDITION for player to bounce when reaching the walls of the window, we wont be using elif, instead i will add a second "if" so to evaluate them independently

    # --- no good
    # if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
    #       player_direction.y *= -1

    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction.x *= -1
    #------

    #--- short term solution
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
          player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    # ---------





    # vector
    # The line below updates the position of the player's sprite by adding the player_direction vector to the current center position of player_rect
    player_rect.center += player_direction * player_speed * dt

    #

    # The += operator modifies player_rect.center in-place, so the player's position changes according to player_direction

    # # ----- the multiplication
    # For a direction vector (2, -1) and a speed of 10, the result of this multiplication is (20, -10). This means that in each frame, the player should move 20 units to the right and 10 units up.
    # By adding player_direction * player_speed to player_rect.center, you’re effectively moving the player’s position by (20, -10) pixels each frame.
    # ----- the multiplication

    pygame.display.update()



pygame.quit()



