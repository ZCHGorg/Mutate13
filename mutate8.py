import random
import time

# Constants
TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 24

# Initial population
population = {'H': 1, 'F': 10, 'P': 0}

def display_environment():
    environment = [' ' for _ in range(TERMINAL_WIDTH)]
    for entity, count in population.items():
        for _ in range(count):
            position = random.randint(0, TERMINAL_WIDTH - 1)
            environment[position] = entity
    print(''.join(environment))

def simulate():
    while True:
        # Display the environment
        display_environment()

        # Behavior logic
        new_population = population.copy()

        # Hunters (H) behavior
        if 'F' in population and population['F'] > 0:
            new_population['H'] += 1
            new_population['F'] -= 1
        else:
            new_population['H'] -= 1

        # Food gatherers (F) behavior
        if 'P' in population and population['P'] > 0:
            new_population['F'] += 1

        # Poop (P) behavior
        if 'H' in population and population['H'] > 0:
            new_population['P'] += population['H']
        if 'F' in population and population['F'] > 0:
            new_population['P'] += population['F']

        # Breeding logic
        if 'P' in population and population['P'] > 0:
            new_population['P'] -= 1
            if 'F' in population and population['F'] > 0:
                new_population['F'] += 1
            if 'H' in population and population['H'] > 1:
                new_population['H'] -= 2
                new_population['F'] += 1

        if 'H' in population and population['H'] > 0:
            if 'F' not in population or population['F'] == 0:
                new_population['F'] += 1

        if 'F' in population and population['F'] > 1:
            new_population['F'] -= 2
            new_population['H'] += 1

        # Update the population
        population.update(new_population)
        for entity in population.keys():
            if population[entity] <= 0:
                del population[entity]

        # Delay for 1 second
        time.sleep(1)

if __name__ == "__main__":
    simulate()
