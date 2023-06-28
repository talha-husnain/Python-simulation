import pygame
import numpy as np

class Prop:
    def __init__(self, position, shape, color):
        self.position = np.array(position, dtype=np.int32)
        self.shape = shape
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)

class BandMember:
    def __init__(self, position, shape, color, direction, speed):
        self.position = np.array(position, dtype=np.int32)
        self.shape = shape
        self.color = color
        self.direction = np.array(direction) / np.linalg.norm(direction)
        self.speed = speed

    def move(self):
        self.position = (self.position + self.direction * self.speed).astype(np.int32)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    prop = Prop([100, 100], (50, 50, 100, 100), (255, 0, 0))
    band_member = BandMember([50, 50], (200, 200, 50, 50), (0, 255, 0), [1, 0], 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen

        prop.draw(screen)
        band_member.draw(screen)

        band_member.move()

        pygame.display.flip()

    pygame.quit()
