import pygame
import sys
from pygame.locals import *
import random


def main():
    pygame.init()
    
    bg_size = width, height = 1000, 600
    bg_image = "bg.jpg"
    butterfly_image = "butterfly.gif"

    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("butterfly-flying")

    background = pygame.image.load(bg_image)
    
    butterfly = pygame.image.load(butterfly_image).convert_alpha()
    butterfly_rect = position = butterfly.get_rect()
    butterfly_rect.left, butterfly_rect.top =  500, 300
    butterfly_rect.width, butterfly_rect.height = 213, 174
    speed = [2, 1]
    

    t = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #移动图像
        position = position.move(speed)

        if position.left < 0 or position.right > width:
            
            #翻转图像
            butterfly = pygame.transform.flip(butterfly,True,False)
            
            #反方向移动
            speed[0] = -speed[0] 

        if position.top < 0 or position.bottom > height:
            speed[1] = -speed[1] 
            
        screen.blit(background, (0, 0))
        screen.blit(butterfly, position)
        
        pygame.display.flip()
        t.tick(120)

if __name__ == "__main__":
    main()
            

    
    


