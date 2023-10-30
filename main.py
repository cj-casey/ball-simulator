import pygame
import os
import math
import random
#constant declaratiom
WIDTH,HEIGHT = 1600,1080
SUB_COUNT = 50
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAVITY = 1

#declaration of orb list
orblist = []
#vector class creation
class vector():
    def __init__(self,startx,starty,endx,endy):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
#orb class creation
class orb_class():
    def __init__(self,x,y,vel_x,vel_y,force_x,force_y,angle,bouncy,mass):
        self.obj = pygame.Rect(x,y,1,1)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.force_x = force_x
        self.force_y = force_y
        self.angle = angle
        self.bouncy = bouncy
        self.mass = mass
#draw window function
def draw_window():
    WIN.fill(WHITE)
    for orb in orblist:
        pygame.draw.circle(WIN,BLACK,(orb.obj.x,orb.obj.y),5,5,5,True,True,True)
    pygame.display.update()
    #future collision optimization function
def subdivisioner():
    width = WIDTH/SUB_COUNT
    height = HEIGHT/SUB_COUNT
#detection collision function
def ball_collision():
    for orb in orblist:
        orb1 = orb
        for orb in orblist:
            if orb != orb1:
                dist,avec,bvec = distance(orb1.obj.x,orb1.obj.y,orb.obj.x,orb.obj.y)
                if dist <= 10 and dist != 0:
                    orb1vec = vector(orb1.obj.x, orb1.obj.y, orb1.obj.x + orb1.vel_x, orb1.obj.y + orb1.vel_y)
                    orbvec = vector(orb.obj.x, orb.obj.y, orb.obj.x + orb.vel_x, orb.obj.y + orb.vel_y)
                    orb1vec = dot(orb1vec,avec,dist)
                    orb1.vel_x = orb1vec.endx - orb1.obj.x
                    orb1.vel_y = orb1vec.endy - orb1.obj.y
                    orbvec = dot(orbvec, bvec, dist)
                    orb.vel_x = (orbvec.endx - orb.obj.x)
                    orb.vel_y = orbvec.endy - orb.obj.y

#distance function
def distance(ax, ay, bx, by):

    #vector pointing from a to b, then moved so it starts at b, that is bvec
    #vector pointing from b to a, then moved so it starts at a, that avec

    adeltax = ax - bx
    adeltay = ay - by
    distance = math.sqrt((pow(adeltax,2) + pow(adeltay,2)))
    bdeltax = bx - ax
    bdeltay = by - ay
    avec = vector(ax,ay,ax+adeltax,ay+adeltay)
    bvec = vector(bx,by,bx+bdeltax,by+bdeltay)
    return distance,avec,bvec
#dot product function
def dot(a,b,distance):
    coefficient = (((a.endx-a.startx)*(b.endx-b.startx)+(a.endy-a.starty)*(b.endy-b.starty)))/pow(distance,2)
    resultant_x = coefficient * (b.endx - b.startx)
    resultant_y = coefficient * (b.endy - b.starty)
    resultant = vector(b.startx,b.starty,b.startx + resultant_x,b.starty + resultant_y)
    return resultant

#wall collision function
def wall_collision():
    for orb in orblist:
        if orb.obj.y >= HEIGHT-8:
            orb.obj.y = HEIGHT-10
            orb.vel_y = orb.bouncy*-1*orb.vel_y
        elif orb.obj.y <= 8:
            orb.obj.y = 10
            orb.vel_y = orb.bouncy*-1*orb.vel_y
        elif orb.obj.x >= WIDTH - 8:
            orb.obj.x = WIDTH - 10
            orb.vel_x = orb.bouncy * -1 * orb.vel_x
        elif orb.obj.x <= 8:
            orb.obj.x = 10
            orb.vel_x = orb.bouncy * -1 * orb.vel_x
#gravity function
def gravity():
    for orb in orblist:
            orb.force_y = GRAVITY

#calculate force function
def force_calculator():
    for orb in orblist:
        orb.vel_x = orb.vel_x + (orb.force_x/orb.mass)
        orb.vel_y = orb.vel_y + (orb.force_y/orb.mass)

#velocity function
def velocity():
    for orb in orblist:
        orb.obj.x = orb.vel_x + orb.obj.x
        orb.obj.y = orb.vel_y + orb.obj.y
       # print("X:" + str(orb.obj.x))
       # print("Y:" + str(orb.obj.y))
#main function
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                orb = orb_class(pos[0],pos[1],0,0,0,0,0,0.8,1)
                orblist.append(orb)
        gravity()
        force_calculator()
        velocity()
        ball_collision()
        wall_collision()
        draw_window()
 #   math.floor(5.67)


if __name__ == "__main__":
    main()
