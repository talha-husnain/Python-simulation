import numpy as np
import pygame
class Light:
    def __init__(self, color, position, direction, intensity, light_type, spread):
        self.color = color
        self.position = np.array(position)  # 3D position
        self.direction = np.array(direction) / np.linalg.norm(direction)  # Normalized direction
        self.intensity = intensity
        self.light_type = light_type
        self.spread = spread  # Angle of the light cone in degrees

    def set_color(self, color):
        self.color = color

    def set_position(self, position):
        self.position = np.array(position)

    def set_direction(self, direction):
        self.direction = np.array(direction) / np.linalg.norm(direction)

    def set_intensity(self, intensity):
        self.intensity = intensity

    def set_light_type(self, light_type):
        self.light_type = light_type

    def set_spread(self, spread):
        self.spread = spread

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position.tolist()

    def get_direction(self):
        return self.direction.tolist()

    def get_intensity(self):
        return self.intensity

    def get_light_type(self):
        return self.light_type

    def get_spread(self):
        return self.spread

    def illuminate(self, point):
        """Calculate the illumination at a given point."""
        point = np.array(point)
        vector = point - self.position
        distance = np.linalg.norm(vector)
        angle = np.degrees(np.arccos(np.dot(vector, self.direction) / distance))
        
        if angle < self.spread / 2:  # Inside the light cone
            return self.intensity * (1 - distance / 500)  # Assuming the max distance is 500
        else:  # Outside the light cone
            return 0
class LightGroup:
    def __init__(self, lights=None):
        self.lights = lights if lights else []

    def add_light(self, light):
        self.lights.append(light)

    def set_color(self, color):
        for light in self.lights:
            light.set_color(color)

    def set_position(self, position):
        for light in self.lights:
            light.set_position(position)

    def set_direction(self, direction):
        for light in self.lights:
            light.set_direction(direction)

    def set_intensity(self, intensity):
        for light in self.lights:
            light.set_intensity(intensity)

    def set_light_type(self, light_type):
        for light in self.lights:
            light.set_light_type(light_type)

    def set_spread(self, spread):
        for light in self.lights:
            light.set_spread(spread)

def main():
    # Create a light
    light1 = Light("red", [0, 0, 0], [1, 0, 0], 10, "solid", 90)
    print(f"Light1 color: {light1.get_color()}")
    print(f"Light1 position: {light1.get_position()}")
    print(f"Light1 direction: {light1.get_direction()}")
    print(f"Light1 intensity: {light1.get_intensity()}")
    print(f"Light1 light type: {light1.get_light_type()}")
    print(f"Light1 spread: {light1.get_spread()}")

    # Create another light
    light2 = Light("blue", [100, 0, 0], [-1, 0, 0], 10, "solid", 90)
    print(f"Light2 color: {light2.get_color()}")
    print(f"Light2 position: {light1.get_position()}")
    print(f"Light2 direction: {light1.get_direction()}")
    print(f"Light2 intensity: {light1.get_intensity()}")
    print(f"Light2 light type: {light1.get_light_type()}")
    print(f"Light2 spread: {light1.get_spread()}")

    # Create a light group
    group = LightGroup([light1, light2])
    group.set_intensity(11)  # Increase the intensity of all lights in the group

    print(f"Light1 intensity after group set: {light1.get_intensity()}")
    print(f"Light2 intensity after group set: {light2.get_intensity()}")

    # Test illumination
    print(f"Illumination at [50, 0, 0] by light1: {light1.illuminate([50, 0, 0])}")
    print(f"Illumination at [150, 0, 0] by light1: {light1.illuminate([150, 0, 0])}")
    print(f"Illumination at [50, 0, 0] by light2: {light2.illuminate([50, 0, 0])}")
    print(f"Illumination at [150, 0, 0] by light2: {light2.illuminate([150, 0, 0])}")

pygame.quit()

if __name__ == "__main__":
    main()
