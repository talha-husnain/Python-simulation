import pygame
import json
import time
from light1 import Light
from smoke1 import SmokeMachine
from props1 import Prop, BandMember
from Backdrop1 import Backdrop

class Choreography:
    def __init__(self):
        self.lights = []
        self.smoke_machine = None
        self.props_bands = []
        self.backdrop = None
        self.screen = None

    def load_scene(self, file_path):
        try:
            with open(file_path, 'r') as file:
                scene_data = json.load(file)

            if 'lights' in scene_data:
                for light_data in scene_data['lights']:
                    light = Light(
                        color=light_data['color'],
                        position=light_data['position'],
                        direction=light_data['direction'],
                        intensity=light_data['intensity'],
                        light_type=light_data['light_type']
                    )
                    self.lights.append(light)

            if 'smoke_machine' in scene_data:
                smoke_machine_data = scene_data['smoke_machine']
                self.smoke_machine = SmokeMachine(
                    position=smoke_machine_data['position'],
                    direction=smoke_machine_data['direction'],
                    intensity=smoke_machine_data['intensity'],
                    neighborhood_type=smoke_machine_data['neighborhood_type']
                )

            if 'props_bands' in scene_data:
                for prop_band_data in scene_data['props_bands']:
                    if 'velocity' in prop_band_data:
                        prop_band = BandMember(
                            position=prop_band_data['position'],
                            shape=prop_band_data['shape'],
                            color=prop_band_data['color'],
                            direction=prop_band_data['direction'],
                            speed=prop_band_data['velocity']
                        )
                    else:
                        prop_band = Prop(
                            position=prop_band_data['position'],
                            shape=prop_band_data['shape'],
                            color=prop_band_data['color']
                        )
                    self.props_bands.append(prop_band)

            if 'backdrop' in scene_data:
                backdrop_data = scene_data['backdrop']
                if 'color' in backdrop_data:
                    self.backdrop = Backdrop(color=backdrop_data['color'])
                elif 'image' in backdrop_data:
                    self.backdrop = Backdrop(image=backdrop_data['image'])

        except IOError:
            print("Error: Failed to load the scene file.")

    def load_commands(self, file_path):
        try:
            with open(file_path, 'r') as file:
                commands = json.load(file)
            return commands
        except IOError:
            print("Error: Failed to load the command file.")
            return []

    def execute_commands(self, commands):
        commands.sort(key=lambda cmd: cmd['time'])
        
        start_time = time.time()
        for command in commands:
            while time.time() - start_time < command['time']:
                time.sleep(0.01)

            obj = None
            if command['object'] == 'backdrop':
                obj = self.backdrop
            elif command['object'] == 'smoke_machine':
                obj = self.smoke_machine
            elif command['object'].startswith('light'):
                index = int(command['object'][len('light'):])
                if index < len(self.lights):
                    obj = self.lights[index]
            elif command['object'].startswith('prop_band'):
                index = int(command['object'][len('prop_band'):])
                if index < len(self.props_bands):
                    obj = self.props_bands[index]

            if obj is not None:
                method = getattr(obj, command['method'], None)
                if method is not None:
                    method()  # Remove the *command['args'] from method invocation

    def draw(self):
        if self.backdrop is not None:
            self.backdrop.draw(self.screen)

        for prop_band in self.props_bands:
            prop_band.draw(self.screen)

        for light in self.lights:
            light.draw(self.screen)

        if self.smoke_machine is not None:
            self.smoke_machine.draw(self.screen)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    choreography = Choreography()
    choreography.screen = screen

    choreography.load_scene('scene.json')

    commands = choreography.load_commands('commands.json')
    choreography.execute_commands(commands)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        choreography.draw()

        pygame.display.flip()

    pygame.quit()
