import pygame
import time
import gamemanager


pygame.init()
running = True
screen_width=1300
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("I love Monkeys... and turtles")

gm=gamemanager.GameManager((screen_width,screen_height))

t=pygame.time.get_ticks()
    

while running:
    oldtime=t
    t=pygame.time.get_ticks()
    
    #TODO add event processing system
    for e in pygame.event.get():
        if pygame.QUIT==e.type:
            running=False
        else :
            pass
    gm.update(t-oldtime)
    gm.draw(screen)
    pygame.display.flip()       
    time.sleep(0.01)


pygame.quit()

# core-s->gm-s->worls-s->tons of sprites
