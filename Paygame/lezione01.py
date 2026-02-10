import pygame

pygame.init()
screen = pygame.display.set_mode(640, 480)
pygame.display.set_caption("test Pygame")
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
     keys=pygame.key.get_pressed()
     if keys[pygame.K_LE]:
         x=speed
    elif keys [pygame.K.RIGHT]
        x=speed
    elif keys [pygame.K.UP]
        y=speed
    elif keys[ pygame..k.DOWN]
    y=speed
    
    screen.fill((255, 100, 100))
    pygame.draw.circle(320, 240,255, 100, 100)
    x=320
    y=340
    speed=5
   