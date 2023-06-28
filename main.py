from cher0 import Choreography

if __name__ == "__main__":
    choreography = Choreography('state.json', 'actions.json')
    choreography.perform()
