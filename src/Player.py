import random
import pygame

class Player:
    line_width=6
    
    def __init__(self,world_size):
        self.radius=random.randint(30,80)
        self.color=pygame.Color(random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.pos=pygame.Vector2(random.randint(0,world_size.x),random.randint(0,world_size.y)) 
        self.speed=pygame.Vector2(0,0)
        
    def update(self,action_list,world_size):
        for a in action_list:
            self.speed+=a.accel
        self.pos+=self.speed
        if self.pos.x <0 or self.pos.x>world_size.x:
            self.pos-=self.speed
            self.speed.x =-self.speed.x
            self.radius *= 0.9
        if self.pos.y<0 or self.pos.y>world_size.y:
            self.pos-=self.speed
            self.speed.y=-self.speed.y
            self.radius *= 0.9
        self.speed*=0.995
    
    def bounce(self,otherplayer):
        diff = self.pos - otherplayer.pos
        if diff.length() < (self.radius + otherplayer.radius):
            temp=self.speed
            self.speed=otherplayer.speed
            otherplayer.speed=temp

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.line_width)