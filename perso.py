import pygame
from pygame.locals import * 




class Perso( pygame.sprite.Sprite):
	def __init__(self, droite, gauche, haut, bas):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		pygame.sprite.Sprite.__init__(self)
		
		self.image = self.droite
		self.speed = 4
		self.position = pygame.Rect(300,240,40,40);
	
	def deplacer(self, direction):	
		if direction == 'droite':
			self.image = self.droite
                        self.position.x+=self.speed
		if direction == 'gauche':
			self.image = self.gauche
                        self.position.x-=self.speed
		if direction == 'haut':
			self.image = self.haut
                        self.position.y-=self.speed
		if direction == 'bas':
			self.image = self.bas
                        self.position.y+=self.speed
        def collisionEffet(self, direction):	
		if direction == 'droite':
			self.position.x+=self.speed
		if direction == 'gauche':
			self.position.x-=self.speed
		if direction == 'haut':
			self.position.y-=self.speed
		if direction == 'bas':
			self.position.y+=self.speed
