import pygame, sys
from player import Player
from enemy import Enemy
from level import LevelMaker
from settings import *

 
class Game:
    def __init__(self):
        self.text_color = (235,100,50)
        self.score = 0
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.start_menu = False
        
        #need if statement here to run the state of game for each level  
        
        self.map = LevelMaker(level_2)
            
        self.enemy_amount_1 = 0
        self.enemy_amount_2 = 0
        self.enemy_amount_3 = 0
        self.enemy_1 = pygame.sprite.Group()
        self.enemy_2 = pygame.sprite.Group()
        self.enemy_3 = pygame.sprite.Group()
            
        for cord in self.map.generate_sprite_cords()[0]:
            self.enemy_amount_1 += 1
            self.enemy_1.add(Enemy('a', '03',cord,screen_width,2))
            
        for cord in self.map.generate_sprite_cords()[1]:
            self.enemy_amount_2 += 1
            self.enemy_2.add(Enemy('b', '02',cord,screen_width,2))
            
        for cord in self.map.generate_sprite_cords()[2]:
            self.enemy_amount_3 += 1
            self.enemy_3.add(Enemy('c', '01',cord,screen_width,2))
            
        # Player setup will need a loop to generate 
        player_sprite = Player((screen_width / 2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.lives = 3
        
       
        #print(self.enemy,self.player)
        #print(self.player.sprite.lazer)
        
        pygame.sprite.groupcollide(self.player.sprite.lazer,self.enemy_1,True,True)
        #print(self.list_of_enemys)
        #print(self.enemy_amount)


    # I think I need to make game states here
    def run(self):
        self.display_points = self.font.render(f'Score: {self.score}', False, self.text_color)
        self.display_points_rect = self.display_points.get_rect(center = (390, 50))
        
        screen.blit(self.display_points, self.display_points_rect)
        
        self.enemy_1.update()
        self.enemy_1.draw(screen)
        self.enemy_2.update()
        self.enemy_2.draw(screen)
        self.enemy_3.update()
        self.enemy_3.draw(screen)
            

        if pygame.sprite.groupcollide(self.player.sprite.lazer,self.enemy_3,True,True):
            self.enemy_amount_3 -= 1
            self.score += 100
            print(f'Enemy destroyed {self.enemy_amount_3} remain')
            if self.enemy_amount_3 == 0:
                print("You have won the battle! Level 2 will begin shortly")

        if pygame.sprite.groupcollide(self.player.sprite.lazer,self.enemy_2,True,True):
            self.enemy_amount_2 -= 1
            self.score += 50
            print(f'Enemy destroyed {self.enemy_amount_2} remain')
            if self.enemy_amount_2 == 0:
                print("You have won the battle! Level 2 will begin shortly")
                     
        if pygame.sprite.groupcollide(self.player,self.enemy_2,False,True):
            self.lives -= 1
            print(f'You have {self.lives} left')
            if self.lives == 0:
                print('Youve been defeated try harder next time. \nWould you like to try again? ')
            
        if pygame.sprite.groupcollide(self.player.sprite.lazer,self.enemy_1,True,True):
            self.enemy_amount_1 -= 1
            self.score += 25
            print(f'Enemy destroyed {self.enemy_amount_1} remain')
            if self.enemy_amount_1 == 0:
                print("You have won the battle! Level 2 will begin shortly")
                     
        if pygame.sprite.groupcollide(self.player,self.enemy_1,False,True):
            self.lives -= 1
            print(f'You have {self.lives} left')
            if self.lives == 0:
                print('Youve been defeated try harder next time. \nWould you like to try again? ')
            
        self.player.update()
        self.player.draw(screen)
        self.player.sprite.lazer.draw(screen)
        
#i think states of game go down here
if __name__ == '__main__':
    pygame.init()
    
    screen_width = 480
    
    screen_height = 640
	
    screen = pygame.display.set_mode((screen_width,screen_height))
	
    background = pygame.image.load('imgs/space.png').convert()
    background = pygame.transform.scale(background,(screen_width,screen_height))
    
    
    clock = pygame.time.Clock()
	#states of game around here i think
    game = Game()
	

	
    while True:
		
        for event in pygame.event.get():
			
            if event.type == pygame.QUIT:
				
                pygame.quit()
				
                sys.exit()
			
        screen.blit(background,(0,0))
        #screen.fill((30,30,30))
		
        game.run()
			
		
        pygame.display.flip()
		
        clock.tick(60)