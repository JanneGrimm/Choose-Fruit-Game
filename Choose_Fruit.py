import pygame
from sys import exit

from functions import WINDOW_WIDTH, WINDOW_HEIGHT, BG_SKY
from functions import load_background, item_switcher, load_fruit_images
from functions import move_item_horizontal, move_item_vertical



pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Background
sky_surface = pygame.Surface((800,1000))
sky_surface.fill('#87CEEB')



fruit_list = load_fruit_images()
curr_item = item_switcher(fruit_list)



running = True
item_y = 600
item_x = 600

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()



    screen.blit(sky_surface,(0,0))
    
    #screen.blit(bg_yard, (0,500))


    clock.tick(60)
    pygame.display.flip()

    


pygame.quit()
sys.exit()
