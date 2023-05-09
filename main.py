import pygame
from sys import exit
import functions



'''ESSENTIALS'''
pygame.init()

#DISPLAY-SCREEN SETUP
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Dino Dodge')

#FRAMES-PER-SECOND (FPS)
clock = pygame.time.Clock()

#font = pygame.font.Font('directory', size)

game_active = True

#MUSIC
#background_music = pygame.mixer.Sound('directory')
#background_music.play(loops = -1)

#PLAYER CHARACTER
player = pygame.sprite.GroupSingle()
player.add(functions.Player())




'''GAME-LOOP'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        screen.fill('#F3BBC1')

        #PLAYER CHARACTER
        player.draw(screen)
        player.update()
        
    #else:

    pygame.display.update()
    clock.tick(60)