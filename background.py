import pygame
class Background:
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/bg.png')
        self.position = 0
        self.uncoloredSprite = pygame.image.load('data/gfx/bg.png') 
    def setSprite(self, tint):  
        copy = self.uncoloredSprite.copy()
        color = (0.7,0.3,0.6)
        copy.fill((color[0]*255, color[1]*255, color[2]*255), special_flaZgs=pygame.BLEND_ADD)
        self.sprite = copy