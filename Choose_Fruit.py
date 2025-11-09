import pygame
import sys



pygame.init()
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()

bg = pygame.image.load("images/background.png").convert()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


    screen.blit(bg, (0, 0))
    pygame.display.flip()
    clock.tick(120)


pygame.quit()
sys.exit()
