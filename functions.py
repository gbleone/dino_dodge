import pygame

class Player(pygame.sprite.Sprite):
    '''PLAYER CHARACTER'''
    
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/green_player_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/green_player_2.png').convert_alpha()
        player_walk_3 = pygame.image.load('graphics/player/green_player_3.png').convert_alpha()
        player_walk_4 = pygame.image.load('graphics/player/green_player_4.png').convert_alpha()
        player_walk_5 = pygame.image.load('graphics/player/green_player_5.png').convert_alpha()
        player_walk_6 = pygame.image.load('graphics/player/green_player_6.png').convert_alpha()
        player_walk_7 = pygame.image.load('graphics/player/green_player_7.png').convert_alpha()
        player_walk_8 = pygame.image.load('graphics/player/green_player_8.png').convert_alpha()

        self.player_walk = [
            player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, 
            player_walk_6, player_walk_7, player_walk_8
            ]
    
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))

        self.gravity = 0

    def player_animation(self):
        '''PLAYER JUMP, WALK, & IDLE ANIMATION'''
        keys = pygame.key.get_pressed()
                
        if self.rect.bottom <= 299:
            self.player_index = 4
            self.image = self.player_walk[int(self.player_index)]
        elif keys[pygame.K_d]:
            self.player_index += 0.275
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        elif keys[pygame.K_a]:
            self.player_index += 0.275
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        else:
            self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def apply_gravity(self):
        '''GRAVITY MECHANICS'''
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def player_keybinds(self):
        '''PLAYER KEY-BINDINGS'''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_a]:
            self.rect.x += -3
        elif keys[pygame.K_w] and self.rect.bottom >= 300:
            self.gravity = -20

    def player_scale(self):
        '''SET PLAYER-DIMENSIONS'''
        self.image = pygame.transform.scale(self.player_walk[int(self.player_index)], (125, 125))
        
    def update(self):
        '''UNIVERSAL UPDATER'''
        self.player_animation()
        self.player_keybinds()
        self.player_scale()
        self.apply_gravity()

