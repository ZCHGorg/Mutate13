import random
import os
import time

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24
NUM_HUNTERS = 5
NUM_FOOD_GATHERERS = 20
MAX_FOOD = 100

# ASCII characters
HUNTER_CHAR = 'H'
FOOD_GATHERER_CHAR = 'F'
POOP_CHAR = 'P'
EMPTY_CHAR = ' '

# Initialize hunters and food gatherers
hunters = [{'x': random.randint(0, SCREEN_WIDTH-1), 'y': random.randint(0, SCREEN_HEIGHT-1), 'food': 0} for _ in range(NUM_HUNTERS)]
food_gatherers = [{'x': random.randint(0, SCREEN_WIDTH-1), 'y': random.randint(0, SCREEN_HEIGHT-1), 'food': random.randint(1, MAX_FOOD)} for _ in range(NUM_FOOD_GATHERERS)]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_environment():
    clear_screen()
    environment = [[EMPTY_CHAR] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

    for hunter in hunters:
        environment[hunter['y']][hunter['x']] = HUNTER_CHAR

    for gatherer in food_gatherers:
        environment[gatherer['y']][gatherer['x']] = FOOD_GATHERER_CHAR

    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            print(environment[y][x], end='')
        print()

def main():
    while True:
        print_environment()

        # Simulate movement and interactions
        for hunter in hunters:
            # Hunters move randomly
            hunter['x'] = (hunter['x'] + random.randint(-1, 1)) % SCREEN_WIDTH
            hunter['y'] = (hunter['y'] + random.randint(-1, 1)) % SCREEN_HEIGHT

            # Hunters leave poop behind
            if random.random() < 0.1:
                food_gatherers.append({'x': hunter['x'], 'y': hunter['y'], 'food': 0})

            # Hunters eat food gatherers
            for gatherer in food_gatherers:
                if gatherer['x'] == hunter['x'] and gatherer['y'] == hunter['y']:
                    hunter['food'] += gatherer['food']
                    food_gatherers.remove(gatherer)

            # Hunters die if they run out of food
            if hunter['food'] <= 0:
                hunters.remove(hunter)

        for gatherer in food_gatherers:
            # Gatherers move randomly
            gatherer['x'] = (gatherer['x'] + random.randint(-1, 1)) % SCREEN_WIDTH
            gatherer['y'] = (gatherer['y'] + random.randint(-1, 1)) % SCREEN_HEIGHT

            # Gatherers eat poop and lose food
            if random.random() < 0.2:
                gatherer['food'] -= 1

            # Gatherers die if they have no food left
            if gatherer['food'] <= 0:
                food_gatherers.remove(gatherer)

        time.sleep(1)

import random
import os
import time

# ... (previous code)

# Additional ASCII character for breeding
BREEDING_CHAR = 'B'

# Breeding constants
BREEDING_RATE_F = 0.05
BREEDING_RATE_H = 0.01

def breed(creature):
    if creature == FOOD_GATHERER_CHAR:
        return BREEDING_CHAR if random.random() < BREEDING_RATE_F else creature
    elif creature == HUNTER_CHAR:
        return BREEDING_CHAR if random.random() < BREEDING_RATE_H else creature
    return creature

def main():
    while True:
        print_environment()

        # ... (previous movement and interaction code)

        # Breeding
        new_food_gatherers = []
        new_hunters = []

        for gatherer in food_gatherers:
            if random.random() < BREEDING_RATE_F:
                new_food_gatherers.append({'x': gatherer['x'], 'y': gatherer['y'], 'food': gatherer['food']})
            gatherer['food'] -= 1

        for hunter in hunters:
            if random.random() < BREEDING_RATE_H:
                new_hunters.append({'x': hunter['x'], 'y': hunter['y'], 'food': hunter['food']})
            hunter['food'] -= 1

        food_gatherers.extend(new_food_gatherers)
        hunters.extend(new_hunters)

        # ... (population control and other code)

        time.sleep(1)

if __name__ == "__main__":
    main()
