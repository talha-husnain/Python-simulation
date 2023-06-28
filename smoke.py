import numpy as np

class SmokeMachine:
    def __init__(self, position, direction, intensity, neighborhood_type):
        self.position = np.array(position)  # 3D position
        self.direction = np.array(direction) / np.linalg.norm(direction)  # Normalized direction
        self.intensity = intensity
        self.neighborhood_type = neighborhood_type
        self.smoke_particles = []

    def emit_smoke(self):
        """Generate smoke particles based on intensity."""
        for _ in range(self.intensity):
            # Each smoke particle has a position and a diffusion factor
            self.smoke_particles.append([self.position, np.random.rand()])

    def diffuse_smoke(self):
        """Update position of smoke particles based on direction, intensity, and diffusion factor."""
        new_particles = []
        for particle in self.smoke_particles:
            position, diffusion_factor = particle
            position = position.astype(np.float64)
            position += self.direction * self.intensity * diffusion_factor
            new_particles.append([position, diffusion_factor])
        self.smoke_particles = new_particles

    def get_smoke_particles(self):
        return [[p[0].tolist(), p[1]] for p in self.smoke_particles]
def diffuse_smoke(self):
    """Update position of smoke particles based on direction, intensity, and diffusion factor."""
    new_particles = []
    for particle in self.smoke_particles:
        position, diffusion_factor = particle

        # Apply the neighborhood rule
        if self.neighborhood_type == 'Moore':
            # Spread in all directions
            position += np.random.randn(3) * self.intensity * diffusion_factor
        elif self.neighborhood_type == 'Van Neumann':
            # Spread in the direction of the smoke machine
            position += self.direction * self.intensity * diffusion_factor

        new_particles.append([position, diffusion_factor])
    self.smoke_particles = new_particles
    import numpy as np

def main():
    # Create a SmokeMachine
    smoke_machine = SmokeMachine(position=[0, 0, 0], direction=[1, 0, 0], intensity=5, neighborhood_type='Moore')
    
    # Emit smoke particles
    smoke_machine.emit_smoke()

    # Print initial smoke particles
    print("Initial Smoke Particles:")
    print(smoke_machine.get_smoke_particles())

    # Diffuse smoke particles for 10 timesteps
    for i in range(10):
        smoke_machine.diffuse_smoke()
        print(f"Smoke Particles after timestep {i + 1}:")
        print(smoke_machine.get_smoke_particles())

if __name__ == "__main__":
    main()
