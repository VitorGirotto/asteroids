# In your Player class initialization
def __init__(self):
    # Other initialization code...
    self.image = pygame.image.load('path/to/your/ship.png').convert_alpha()
    # You might need to scale the image
    self.image = pygame.transform.scale(self.image, (width, height))
    
def draw(self, screen):
    # Instead of the triangle drawing code...
    rotated_image = pygame.transform.rotate(self.image, -self.rotation)
    rect = rotated_image.get_rect(center=self.position)
    screen.blit(rotated_image, rect)