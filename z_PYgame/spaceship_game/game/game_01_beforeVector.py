#🟡 before vector


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
surf = pygame.Surface((100,200))
# animation related
x = 100

# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png')
}



player_surf = pygame.image.load(image_paths['player']).convert_alpha()

# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane at the center of the screen/window
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))




# start
star_surf = pygame.image.load(image_paths['star']).convert_alpha()
# star pos
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]



while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False



 # FILL thplayer_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))e window with a red color
 # player = pygame.Rect((300, 250, 50, 50))
 # https://pyga.me/docs/ref/pygame.html

 # 7 --- DRAW the game ----
 # list of colors: https://pyga.me/docs/ref/color_list.html
    display_surface.fill("lavenderblush2")




    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # x += 0.1
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left  += 6

    display_surface.blit(player_surf, player_rect)
    pygame.display.update()



pygame.quit()