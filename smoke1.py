import pygame
import numpy as np

class SmokeMachine:
    def __init__(self, position, direction, intensity, neighborhood_type):
        self.position = np.array(position)
        self.direction = np.array(direction)
        self.intensity = intensity
        self.neighborhood_type = neighborhood_type
        self.smoke_particles = []
        self.screen = pygame.display.set_mode((1500, 1500))  # Create a 1500x1500 window

    def start(self):
        self.create_smoke_particle()
        self.update()

    def create_smoke_particle(self):
        # Create a new smoke particle
        smoke_particle = {
            'position': self.position.copy(),
            'radius': 1,  # Start with a small radius
            'transparency': 255  # Start fully opaque
        }
        self.smoke_particles.append(smoke_particle)

    def update(self):
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update and draw smoke particles
            for particle in self.smoke_particles:
                pygame.draw.circle(self.screen, (255, 255, 255, particle['transparency']), particle['position'], particle['radius'])

                # Update the particle's state for the next frame
                particle['radius'] += 1
                particle['transparency'] -= 1

            # Remove smoke particles that have disappeared
            self.smoke_particles = [particle for particle in self.smoke_particles if particle['transparency'] > 0]

            # Update the display
            pygame.display.flip()

            # Delay to control the animation speed
            pygame.time.wait(10)

        pygame.quit()

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def get_intensity(self):
        return self.intensity

    def get_neighborhood_type(self):
        return self.neighborhood_type


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # Create a 500x500 window

    smoke_machine = SmokeMachine([250, 250], [1, 0], 5, 'Moore')
    smoke_machine.start()

    pygame.quit()
