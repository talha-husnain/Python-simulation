import pygame
from PIL import Image
import numpy as np

class Backdrop:
    def __init__(self, color=(0, 0, 0), image=None):
        self.color = pygame.Color(color) if isinstance(color, str) else color
        self.image = self.set_image(image) if image else None

    def set_color(self, color):
        self.color = pygame.Color(color) if isinstance(color, str) else color

    def set_image(self, image_path):
        try:
            image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(image, (1500, 1500))
        except pygame.error:
            print("Error: Failed to load the image.")
            return None
        return image

    def get_color(self):
        return self.color

    def get_image(self):
        return self.image

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (0, 0))
        else:
            screen.fill(self.color)

    def is_monochrome(self):
        if self.image:
            grayscale = self.image.convert('L')
            return not (grayscale != self.image)
        else:
            return None

    def apply_lighting(self, light_intensity):
        if self.image:
            image_array = pygame.surfarray.array3d(self.image).astype(np.float32)
            enhanced_array = image_array * light_intensity
            enhanced_array = np.clip(enhanced_array, 0, 255)
            enhanced_image = pygame.surfarray.make_surface(enhanced_array.astype(np.uint8))
            self.image = enhanced_image

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))

    backdrop = Backdrop(color="white", image="backdrop_image.jpg")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        backdrop.draw(screen)

        pygame.display.flip()

    pygame.quit()
