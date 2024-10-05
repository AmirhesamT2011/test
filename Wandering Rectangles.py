import pygame,sys,time
from pygame.locals import*
pygame.init()

T=400
A=400
windowsurface=pygame.display.set_mode((T,A),0,32)
pygame.display.set_caption('Wandering rectangles')

DOWNLEFT='downleft'
DOWNRIGHT='downright'
UPLEFT='upleft'
UPRIGHT='upright'
movespeed=4

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

b1={'rect':pygame.Rect(300,80,50,100),'color':red,'dir':UPRIGHT}
b2={'rect':pygame.Rect(200,100,20,30),'color':green,'dir':UPLEFT}
b3={'rect':pygame.Rect(100,150,60,60),'color':blue,'dir':DOWNLEFT}

box=[b1,b2,b3]

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    windowsurface.fill(black)
            
    for b in box:
        if b['dir']==DOWNLEFT:
            b['rect'].left -= movespeed
            b['rect'].top += movespeed

        if b['dir']==DOWNRIGHT:
            b['rect'].left += movespeed
            b['rect'].top += movespeed

        if b['dir']==UPLEFT:
            b['rect'].left -= movespeed
            b['rect'].bottom -= movespeed

        if b['dir']==UPRIGHT:
           b['rect'].right += movespeed
           b['rect'].top -= movespeed      
       
        if b['rect'].top<0:
            if b['dir']==UPLEFT:
                b['dir']=DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']=DOWNRIGHT

        if b['rect'].bottom>A:
            if b['dir']==DOWNLEFT:
                b['dir']=UPLEFT
            if b['dir']==DOWNRIGHT:
                b['dir']=UPRIGHT

        if b['rect'].left<0:
            if b['dir']==DOWNLEFT:
                b['dir']=DOWNRIGHT
            if b['dir']==UPLEFT:
                b['dir']=UPRIGHT

        if b['rect'].right>T:
            if b['dir']==DOWNRIGHT:
                b['dir']=DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']=UPLEFT

        pygame.draw.rect(windowsurface,b['color'],b['rect'])
    time.sleep(0.02)
    pygame.display.update()


