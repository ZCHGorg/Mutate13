import random
import time

def main():
    food_gatherers = "F"
    predators = "P"
    huts = "H"
    spears = "S"
    empty_space = " "

    ecosystem_width = 50
    ecosystem_height = 20
    evolving_ecosystem = [[random.choice([food_gatherers, predators, huts, spears, empty_space]) for _ in range(ecosystem_width)] for _ in range(ecosystem_height)]

    while True:
        print("\033[H\033[J")  # Clear the terminal screen
        
        new_ecosystem = []
        for y in range(ecosystem_height):
            new_row = []
            for x in range(ecosystem_width):
                current = evolving_ecosystem[y][x]
                neighbors = get_neighbors(evolving_ecosystem, x, y)
                
                if current == empty_space:
                    if food_gatherers in neighbors and random.random() < 0.1:
                        new_row.append(food_gatherers)
                    elif predators in neighbors and random.random() < 0.05:
                        new_row.append(predators)
                    elif huts in neighbors and random.random() < 0.02:
                        new_row.append(huts)
                    elif spears in neighbors and random.random() < 0.02:
                        new_row.append(spears)
                    else:
                        new_row.append(empty_space)
                else:
                    new_row.append(current)
            new_ecosystem.append(new_row)
        
        evolving_ecosystem = new_ecosystem

        for row in evolving_ecosystem:
            print("".join(row))

        time.sleep(0.5)  # Add a delay to observe changes

def get_neighbors(ecosystem, x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(ecosystem[0]) and 0 <= ny < len(ecosystem) and (dx, dy) != (0, 0):
                neighbors.append(ecosystem[ny][nx])
    return neighbors

if __name__ == "__main__":
    main()
