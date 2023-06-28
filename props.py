import numpy as np

class Prop:
    def __init__(self, position, shape):
        self.position = np.array(position)  # 3D position
        self.shape = shape  # Shape of the prop

    def get_position(self):
        return self.position.tolist()

    def get_shape(self):
        return self.shape

class BandMember:
    def __init__(self, position, shape, direction, speed):
        self.position = np.array(position)  # 3D position
        self.shape = shape  # Shape of the band member
        self.direction = np.array(direction) / np.linalg.norm(direction)  # Normalized direction
        self.speed = speed

    def move(self):
      self.position = self.position.astype(np.float64)
      self.position += self.direction * self.speed


    def get_position(self):
        return self.position.tolist()

    def get_shape(self):
        return self.shape
def main():
    # Create a Prop
    prop = Prop(position=[10, 5, 0], shape="Guitar")

    # Print the prop's position and shape
    print("Prop Position:", prop.get_position())
    print("Prop Shape:", prop.get_shape())

    # Create a BandMember
    band_member = BandMember(position=[0, 0, 0], shape="Singer", direction=[1, 0, 0], speed=2)

    # Move the band member
    band_member.move()

    # Print the band member's position and shape
    print("Band Member Position:", band_member.get_position())
    print("Band Member Shape:", band_member.get_shape())

if __name__ == "__main__":
    main()
