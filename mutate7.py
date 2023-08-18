import random
import os
import time

# Define ASCII characters for entities
HUNTER = 'H'
FOOD_GATHERER = 'F'
POOP = 'P'
EMPTY = ' '

# Define initial parameters
width, height = os.get_terminal_size()
num_food_gatherers = 10
num_hunters = 5
food_spawn_prob = 0.2
breed_threshold = 10
hunters_hunger_threshold = 5

# Initialize the environment
environment = [[EMPTY for _ in range(width)] for _ in range(height)]

# Initialize entities
entities = []
for _ in range(num_food_gatherers):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    entities.append((x, y, FOOD_GATHERER))

for _ in range(num_hunters):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    entities.append((x, y, HUNTER))

# Simulation loop
while True:
    # Clear the terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Update and render the environment
    for y in range(height):
        for x in range(width):
            entity = EMPTY
            for ex, ey, etype in entities:
                if ex == x and ey == y:
                    entity = etype
                    break
            environment[y][x] = entity
            print(entity, end='')
        print()

    # Update entity positions and behaviors
    new_entities = []
    for x, y, etype in entities:
        if etype == FOOD_GATHERER:
            # Food gatherer behavior
            if random.random() < food_spawn_prob:
                new_entities.append((x, y, POOP))
            else:
                dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                new_x = (x + dx) % width
                new_y = (y + dy) % height
                new_entities.append((new_x, new_y, FOOD_GATHERER))
        elif etype == HUNTER:
            # Hunter behavior
            nearby_food_gatherers = [(ex, ey) for ex, ey, et in entities if et == FOOD_GATHERER and abs(ex - x) <= 1 and abs(ey - y) <= 1]
            if nearby_food_gatherers:
                target_x, target_y = random.choice(nearby_food_gatherers)
                dx = 1 if target_x > x else -1 if target_x < x else 0
                dy = 1 if target_y > y else -1 if target_y < y else 0
                new_x = (x + dx) % width
                new_y = (y + dy) % height
                new_entities.append((new_x, new_y, HUNTER))
            else:
                new_entities.append((x, y, HUNTER))
                
    entities = new_entities

    # Sleep for a short duration
    time.sleep(1)
