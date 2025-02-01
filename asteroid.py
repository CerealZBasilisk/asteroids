from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y,radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (0,255,0), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
	
	def spawn(self, radius, position, velocity, rotation):
		asteroid = Asteroid(position[0], position[1], radius)
		asteroid.velocity = velocity.rotate(rotation)
		return asteroid

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return  # Small asteroid is destroyed here
		
		new_asteroids = []
		for i in range(2):
			random_angle = random.uniform(20, 50)
			if i == 0:  
				random_angle = -random_angle
			new_asteroid = self.spawn(
				self.radius - ASTEROID_MIN_RADIUS, 
				self.position, 
				self.velocity * 1.2,  
				random_angle
			)
			new_asteroids.append(new_asteroid)

		for asteroid in new_asteroids:
			if Asteroid.containers:  
				for container in Asteroid.containers:
					container.add(new_asteroid)
