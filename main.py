# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
	print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	delta_timer = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	player_main = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
	feild = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen,(0,0,0))
		updatable.update(dt)
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		for bullet in shots:
			for asteroid in asteroids:
				if bullet.check_colision(asteroid):
					asteroid.split()
					bullet.kill()
		for asteroid in asteroids:
			if asteroid.check_colision(player_main):
				print("Game Over!")
				return
		dt = delta_timer.tick(60)/1000


if __name__ == "__main__":
	main()
