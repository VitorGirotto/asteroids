from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x , y , radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # return super().draw(screen)
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        # return super().update(dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroids(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = first_vector * 1.2
        asteroid2 = Asteroids(self.position.x, self.position.y, self.radius)
        asteroid2.velocity = second_vector * 1.2