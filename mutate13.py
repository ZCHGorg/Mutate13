import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Inheritable Fish Mutation Simulation")

# Colors
WHITE = (255, 255, 255)

# List of possible shapes for the fish
fish_shapes = [
    [(0, 0), (20, 0), (30, 10), (20, 20), (0, 20)],  # Simple fish shape
    # Add more shapes here
]

# Fish class
class Fish:
    def __init__(self, x, y, parent=None):
        self.position = pygame.Vector2(x, y)
        self.attributes = {
            "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            "radius": random.randint(5, 20),
            "velocity": pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3),
            "health": 100
        }
        self.shape = random.choice(fish_shapes)  # Randomly select a shape
        self.parent = parent
        if parent:
            self.inherit_attributes(parent)
    
    def inherit_attributes(self, parent):
        for attr, value in parent.attributes.items():
            if random.random() < 0.5:
                self.attributes[attr] = value
    
    def update(self):
        self.position += self.attributes["velocity"]
        self.bounce()
        self.attributes["health"] -= 0.001
        self.attributes["color"] = (
            self.attributes["color"][0],
            max(0, self.attributes["color"][1] - 0.1 * self.attributes["health"]),
            self.attributes["color"][2]
        )
    
    def bounce(self):
        if self.position.x < 0 or self.position.x > width:
            self.attributes["velocity"].x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.attributes["velocity"].y *= -1
    
    def collide(self, other_fish):
        distance = self.position.distance_to(other_fish.position)
        return distance <= self.attributes["radius"] + other_fish.attributes["radius"]
    
    def eat(self, other_fish):
        if self.collide(other_fish) and self.attributes["color"] != other_fish.attributes["color"]:
            self.attributes["health"] += 30
            return True
        return False
    
    def mutate(self):
        attribute_to_mutate = random.choice(list(self.attributes.keys()))
        new_value = random.choice(attribute_library[attribute_to_mutate])
        if isinstance(new_value, tuple) or isinstance(new_value, pygame.math.Vector2):
            self.attributes[attribute_to_mutate] += new_value
        else:
            self.attributes[attribute_to_mutate] = new_value
    
    def draw(self):
        color = tuple(max(0, min(int(c), 255)) for c in self.attributes["color"])
        points = [(p[0] + int(self.position.x), p[1] + int(self.position.y)) for p in self.shape]
        pygame.draw.polygon(screen, color, points)
    
    def inherit_attributes(self, parent):
        for attr, value in parent.attributes.items():
            if random.random() < 0.5:
                self.attributes[attr] = value
    
    def update(self):
        self.position += self.attributes["velocity"]
        self.bounce()
        self.attributes["health"] -= 0.1  # Decrease health over time
        self.attributes["color"] = (
            self.attributes["color"][0],
            max(0, self.attributes["color"][1] - 0.1 * self.attributes["health"]),
            self.attributes["color"][2]
        )
    
    def bounce(self):
        if self.position.x < 0 or self.position.x > width:
            self.attributes["velocity"].x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.attributes["velocity"].y *= -1
    
    def collide(self, other_fish):
        distance = self.position.distance_to(other_fish.position)
        return distance <= self.attributes["radius"] + other_fish.attributes["radius"]
    
    def eat(self, other_fish):
        if self.collide(other_fish) and self.attributes["color"] != other_fish.attributes["color"]:
            self.attributes["health"] += 30  # Increase health after eating
            return True
        return False
    
    def mutate(self):
        attribute_to_mutate = random.choice(list(self.attributes.keys()))
        self.attributes[attribute_to_mutate] = random.choice(attribute_library[attribute_to_mutate])
    
# Create initial fish
num_fish = 20
fish = [Fish(random.randint(50, width - 50), random.randint(50, height - 50)) for _ in range(num_fish)]

# Attribute library with a wider range of values
attribute_library = {
    "color": [
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(20)
    ],
    "radius": [random.randint(5, 20) for _ in range(20)],
    "velocity": [
        pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3)
        for _ in range(20)
    ],
    "health": [100 + random.uniform(-10, 10) for _ in range(20)]
    # Add more attributes with a wider range of values here
}

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(WHITE)
    
    new_fish = []
    
    for f in fish:
        f.update()
        color = tuple(max(0, min(int(c), 255)) for c in f.attributes["color"])  # Corrected color handling
        pygame.draw.circle(screen, color, (int(f.position.x), int(f.position.y)), f.attributes["radius"])
        
        if random.random() < 0.01:  # Mutate fish occasionally
            f.mutate()
        
        for other_f in fish:
            if f != other_f:
                if f.eat(other_f):
                    fish.remove(other_f)
                    new_fish.append(Fish(f.position.x + random.uniform(-20, 20),
                                         f.position.y + random.uniform(-20, 20), f))
    
    fish.extend(new_fish)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
