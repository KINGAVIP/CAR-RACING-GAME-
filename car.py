import random
import pygame
import time
import os
from pygame import mixer
width=600
height=600
white=(255,255,255)
pygame.init()
a=pygame.display.set_mode((width,height))
pygame.display.set_caption("new car game")
exit_game=False
import
FPS=60

def bg(file,x,y):
    c=pygame.image.load(file)
    c=pygame.transform.scale(c,(width,height))
    a.blit(c,(0,0))
    #a.blit(c,(x,y))

def objs(file,x,y):
    c=pygame.image.load(file)
    a.blit(c,(x,y))

def fonter(text,color,x,y,size):
    font=pygame.font.SysFont(None,size)
    b=font.render(text,True,color)
    a.blit(b,[x,y])
def menu():
    menu='C:/Users/lenovo/Desktop/cargame/images/menu.png'
    bg(menu,0,0)
    pygame.display.update()
    while not exit_game:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
            elif events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    game()
def game():
    t = time.time()
    pygame.mixer.init()
    obsx1=random.randint(25,400)
    pygame.mixer_music.load('C:/Users/lenovo/Desktop/cargame/images/roaring_proud_music_preview.mp3')
    clock=pygame.time.Clock()
    pygame.mixer_music.play(-1)
    game_over = False
    x = 250
    y = 450
    vx = 0
    vy = 0
    score = 0
    road = 'C:/Users/lenovo/Desktop/cargame/images/road.png'
    mycar = 'C:/Users/lenovo/Desktop/cargame/images/red_car.png'
    obs = 'C:/Users/lenovo/Desktop/cargame/images/1.png'
    coin = 'C:/Users/lenovo/Desktop/cargame/images/coin.png'
    roadx = 0
    roady = 0
    high=0
    obsx = random.randint(width / 10, 450)

    coinx = random.randint(width / 10, 450)
    coiny = 0
    obsy1=-200
    obsy = -50

    if(not os.path.exists("scores.txt")):
        with open("scores.txt","w") as f:
            f.write("0")

    with open("scores.txt","r") as f:
        high=f.read()
    while not exit_game:
        bgm='C:/Users/lenovo/Desktop/cargame/images/roaring_proud_music_preview.mp3'

        if game_over:
            o='C:/Users/lenovo/Desktop/cargame/images/over.jpg'
            bg(o,0,0)
            with open("scores.txt","w") as f:
                f.write(str(high))
            fonter("high score:"+str(high),(255,255,0),100,100,100)

            pygame.display.update()
            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    pygame.quit()
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_RETURN:
                        game()
        else:
          #  music(bgm)
            tb=int(time.time()-t)
            roady+=20
            r=pygame.image.load(road)
            r=pygame.transform.scale(r,(width,height))

            obsy+=20
            coiny+=8

            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    pygame.quit()

                elif events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_LEFT:
                        vx=-30
                        vy=0
                    if events.key==pygame.K_RIGHT:
                        vx=30
                        vy=0

                    if events.key==pygame.K_UP:
                        roady+=100
                        obsy+=5
                        coiny+=10



                elif events.type==pygame.KEYUP:
                    vx=0


            if obsy>height:
                obsx=random.randint(50, 400)

                obsy=0
            if obsy1>height:
                obsx1=random.randint(50,400)
                obsy1=0

            if roady>80:
                roady=0
            if coiny>height:
                coinx=random.randint(50, 400)
                coiny=0
            if score>10 and score<40:
                obsy+=5

            if score>=40:
                obsy+=5
                #obsx = random.randint(50, 400)
               # obsx1 = random.randint(50, 400)
                obsy1+=15


            x += vx
            y += vy
            if x>420 or x<90:
                game_over=True

            if abs(y-coiny)<50 and abs(x-coinx)<50:
                mixer.init()
                k=mixer.Sound('C:/Users/lenovo/Desktop/cargame/images/point.ogg')
                k.play()
                score+=10
                coiny=0
                coinx=random.randint(50, 400)
                if score>int(high):
                    high=score

            if abs(y-obsy)<110 and abs(x-obsx)<80:
                game_over=True


        #    a.fill((255,255,255))
            bg(road,roadx,roady)
            a.blit(r, (roadx, roady))
            #objs(road,roadx,roady)
            objs(mycar,x,y)
            objs(obs,obsx,obsy)
            objs(obs,obsx1,obsy1)
            objs(coin,coinx,coiny)

            fonter("score:"+str(score),(255,255,0),50,50,50)
            fonter("time:"+str(tb),(255,255,0),450,30,50)
            #fonter("carspeed:"+str(roady)+"km/h",(255,255,0),50,100,50)
        clock.tick(FPS)
        pygame.display.update()

menu()