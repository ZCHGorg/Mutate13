import time

# ASCII characters for the animals
H = "H" # herbivore
C = "C" # carnivore
P = "P" # poop

# Initialize the animals
herbivores = [H, H, H]
carnivores = [C, C]

# Start the simulation loop
while True:
  # Move the animals around.
  for animal in herbivores + carnivores:
    animal.move()

  # Eat and poop.
  for herbivore in herbivores:
    if herbivore.is_near(P):
      herbivore.eat()
      herbivore.poop()

  # Breed.
  for herbivore in herbivores:
    if herbivore.is_near(another_herbivore):
      herbivore.breed()

  # Hunt.
  for carnivore in carnivores:
    for herbivore in herbivores:
      if carnivore.is_near(herbivore):
        carnivore.hunt(herbivore)

  # Mutate.
  for animal in herbivores + carnivores:
    animal.mutate()

  # Refresh the screen.
  for i, animal in enumerate(herbivores + carnivores):
    print(animal, end=" ")
  print()

  # Sleep for 1/10 second.
  time.sleep(0.1)
