import pygame
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1000

BG_SKY = (173, 216, 230)

ITEM_SPEED = 0.5

# need new background
def load_background(screen: pygame.Surface):
    bg = pygame.image.load("Images/Background/background_yard.png").convert()
    return bg



def load_fruit_images() -> list[pygame.Surface]:
    fruits = []

    pear = pygame.image.load("Images/Items/pear.png").convert_alpha()
    sca_pear = pygame.transform.scale(pear,
                                    (pear.get_width() * 0.3,
                                    pear.get_height() * 0.3))
    fruits.append(sca_pear)

    apple = pygame.image.load("Images/Items/apple.png").convert_alpha()
    sca_apple = pygame.transform.scale(apple,
                                       (apple.get_width() * 0.3,
                                        apple.get_height() * 0.3))
    fruits.append(sca_apple)

    orange = pygame.image.load("Images/Items/orange.png").convert_alpha()
    sca_orange = pygame.transform.scale(orange,
                                       (orange.get_width() * 0.3,
                                        orange.get_height() * 0.3))
    fruits.append(sca_orange)

    banana = pygame.image.load("Images/Items/banana.png").convert_alpha()
    sca_banana = pygame.transform.scale(banana,
                                       (banana.get_width() * 0.3,
                                        banana.get_height() * 0.3))
    fruits.append(sca_banana)

    cherry = pygame.image.load("Images/Items/cherry.png").convert_alpha()
    sca_cherry = pygame.transform.scale(cherry,
                                       (cherry.get_width() * 0.3,
                                        cherry.get_height() * 0.3))
    fruits.append(sca_cherry)

    bomb = pygame.image.load("Images/Items/bomb.png").convert_alpha()
    sca_bomb = pygame.transform.scale(bomb,
                                       (bomb.get_width() * 0.2,
                                        bomb.get_height() * 0.2))
    fruits.append(sca_bomb)
    # add the other fruits...
    
    return fruits



def move_item_vertical(screen: pygame.Surface, image: pygame.Surface, y: float) -> float:
    y += ITEM_SPEED
    
    screen.blit(
        image,
        ((WINDOW_WIDTH / 2) - (image.get_width()/2), y)
    )
    return y



def item_switcher(fruit_list: pygame.Surface) -> pygame.Surface:
    return random.choice(fruit_list)
    

def move_item_horizontal(x: float, screen: pygame.Surface, image: pygame.Surface) -> float:
    x += ITEM_SPEED
    screen.blit(
        image,
        (x, ((WINDOW_WIDTH / 2) - (image.get_width()/2)))
    )
    return x
