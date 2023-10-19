import pygame
from lazer import Lazer

#basic sprite making class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load("imgs/player/player_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(32,32))
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.lazer_time = 0 
        self.lazer_cd = 600
        self.lazer = pygame.sprite.Group()
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
             self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.lazer_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.lazer_time >= self.lazer_cd:
                self.ready = True
    
    def shoot_laser(self):
        print("lazer shot!")
        self.lazer.add(Lazer(self.rect.center,-12,self.rect.bottom))
            
    
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    
    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lazer.update()
        