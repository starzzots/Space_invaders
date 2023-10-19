import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,imgletter,imgnumber,pos,constraint, speed):
        super().__init__()
        file_path = 'imgs/enemy/aliens/spaceships/'+ imgletter + '-' + imgnumber + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(32,32))
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.move_right = True
        self.delta = 0
        self.hit = False

        
    

    def movement(self):
        #will need to update all this too i think
        if self.move_right == True:
            self.rect.x += 2 + self.delta
        if self.move_right == False:
            self.rect.x -= 2 + self.delta
    

    def check_if_hit_wall(self):
        # works for now but will have to come back to it to edit when more enemys are in game
        if self.rect.left <= 0:
            self.rect.left = 0
            self.rect.y += 24
            self.delta += .25
            if self.delta >= 2:
                self.delta = 2
            self.move_right = True
            return self.move_right
            
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
            self.rect.y += 24
            self.delta += .25
            if self.delta >= 2:
                self.delta = 2
            self.move_right = False
            return self.move_right
            
    
    def update(self):
            self.movement()
            self.check_if_hit_wall()