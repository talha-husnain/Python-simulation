import pygame
import numpy as np

class Light:
    def __init__(self, color, position, direction, intensity, light_type):
        self.color = color
        self.position = np.array(position)
        self.direction = np.array(direction) / np.linalg.norm(direction)
        self.intensity = intensity
        self.light_type = light_type

    def turn_on(self, screen):
        self.screen = screen
        self.draw()

    def draw(self):
        color_rgb = self.color[:3]  # Remove the alpha channel

        # Calculate the radius based on the intensity
        radius = int(self.intensity * 5)

        # Draw the light as a cone shape
        light_cone = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(light_cone, color_rgb, (radius, radius), radius)
        self.rotate_cone(light_cone)

        # Get the position to draw the light cone
        x, y = self.position - np.array([radius, radius])

        # Draw the light cone on the screen
        self.screen.blit(light_cone, (x, y))

    def rotate_cone(self, cone_surface):
        angle = np.arctan2(-self.direction[1], self.direction[0])
        rotated_cone = pygame.transform.rotate(cone_surface, np.degrees(angle))
        rotated_rect = rotated_cone.get_rect(center=cone_surface.get_rect(center=(self.intensity * 5, self.intensity * 5)).center)
        cone_surface.fill((0, 0, 0, 0))
        cone_surface.blit(rotated_cone, rotated_rect.topleft)

class LightGroup:
    def __init__(self):
        self.lights = []

    def add_light(self, light):
        self.lights.append(light)

    def turn_on_all(self, screen):
        for light in self.lights:
            light.turn_on(screen)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # Create a 500x500 window

    group = LightGroup()

    # Create individual lights
    red_light = Light((255, 0, 0, 100), [250, 250], [1, 0], 5, 'spot')
    green_light = Light((0, 255, 0, 100), [150, 150], [-1, 0], 5, 'spot')
    blue_light = Light((0, 0, 255, 100), [350, 350], [0, 1], 5, 'spot')

    # Add lights to the group
    group.add_light(red_light)
    group.add_light(green_light)
    group.add_light(blue_light)

    # Turn on all lights in the group
    group.turn_on_all(screen)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
