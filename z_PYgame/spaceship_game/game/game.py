import pygame


pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True


surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100


player_surf = pygame.image.load('../images/player.png')


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("lavenderblush2")
    x += 0.1
    display_surface.blit(player_surf, (x,150))


    pygame.display.update()




pygame.quit()