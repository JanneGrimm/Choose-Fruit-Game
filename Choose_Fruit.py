import pygame
import sys

from functions import WINDOW_WIDTH, WINDOW_HEIGHT
from functions import move_item, item_switcher, load_fruit_images




pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

screen.fill((173, 216, 230))

fruit_list = load_fruit_images()
curr_item = item_switcher(fruit_list)



running = True
item_y = 600

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    item_y = move_item(screen, curr_item, item_y)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()
