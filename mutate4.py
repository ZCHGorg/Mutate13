import random
import time

def main():
    food_gatherers = "F"
    predators = "P"
    empty_space = "."

    ecosystem_size = 30
    evolving_ecosystem = []

    for _ in range(ecosystem_size):
        evolving_ecosystem.append(random.choice([food_gatherers, predators, empty_space]))

    for iteration in range(12):
        print(f"Iteration {iteration + 1}:")

        for _ in range(ecosystem_size):
            print(evolving_ecosystem[_], end="")
        print("\n")

        new_ecosystem = evolving_ecosystem.copy()
        for i in range(ecosystem_size):
            current = evolving_ecosystem[i]
            if current == empty_space:
                neighbors = evolving_ecosystem[max(i - 1, 0):min(i + 2, ecosystem_size)]
                if food_gatherers in neighbors and random.random() < 0.2:
                    new_ecosystem[i] = food_gatherers
                elif predators in neighbors and random.random() < 0.1:
                    new_ecosystem[i] = predators
        evolving_ecosystem = new_ecosystem

        time.sleep(1)  # Add a delay to observe changes

if __name__ == "__main__":
    main()
