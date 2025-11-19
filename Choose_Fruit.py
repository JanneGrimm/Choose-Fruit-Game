import pygame
import sys

from functions import WINDOW_WIDTH, WINDOW_HEIGHT, BG_SKY
from functions import load_background, item_switcher, load_fruit_images
from functions import move_item_horizontal, move_item_vertical



pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Background
screen.fill((BG_SKY))
#bg_yard = load_background(screen)


fruit_list = load_fruit_images()
curr_item = item_switcher(fruit_list)



running = True
item_y = 600
item_x = 600

while running:
    screen.fill((BG_SKY))
    item_y = move_item_vertical(screen, curr_item, item_y)



    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
            
        # i want to make the exact fruit variable to move left
        # need to stop it going down
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            item_x = move_item_horizontal(item_x, screen, curr_item)




    
    #screen.blit(bg_yard, (0,500))


    clock.tick(60)
    pygame.display.flip()

    


pygame.quit()
sys.exit()
