import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evolving Organism Simulation")

# Mutation rate (adjust as needed)
MUTATION_RATE = 0.1

# Organism class
class Organism:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.attributes = {
            "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            "radius": random.randint(5, 20),
            "velocity": pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3)
        }
        self.inactive_time = 0
    
    def update(self):
        self.position += self.attributes["velocity"]
        self.bounce()
        self.attributes["color"] = self.mutate_color(self.attributes["color"])
        
        if self.inactive_time >= 100:
            self.reproduce_asexual()
            self.inactive_time = 0
        
        self.inactive_time += 1
    
    def bounce(self):
        if self.position.x < 0 or self.position.x > width:
            self.attributes["velocity"].x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.attributes["velocity"].y *= -1
    
    def mutate_color(self, color):
        return tuple(
            max(0, min(int(c + random.uniform(-MUTATION_RATE, MUTATION_RATE) * 255), 255))
            for c in color
        )
    
    def reproduce_asexual(self):
        new_organism = Organism(self.position.x + random.uniform(-20, 20),
                                self.position.y + random.uniform(-20, 20))
        for attr, value in self.attributes.items():
            if random.random() < 0.5:
                new_organism.attributes[attr] = self.mutate_attribute(value)
            else:
                new_attribute = self.generate_new_attribute()
                new_organism.attributes[new_attribute] = self.generate_random_value(new_attribute)
        organisms.append(new_organism)
    
    def mutate_attribute(self, value):
        if isinstance(value, int):
            return value + random.uniform(-MUTATION_RATE, MUTATION_RATE) * value
        elif isinstance(value, pygame.math.Vector2):
            new_velocity = pygame.Vector2(value)
            new_velocity.x += random.uniform(-MUTATION_RATE, MUTATION_RATE) * abs(value.x)
            new_velocity.y += random.uniform(-MUTATION_RATE, MUTATION_RATE) * abs(value.y)
            return new_velocity
        else:
            return value  # For unsupported types
    
    def generate_new_attribute(self):
        possible_attributes = ["color", "radius", "velocity"]
        existing_attributes = list(self.attributes.keys())
        available_attributes = list(set(possible_attributes) - set(existing_attributes))
        if available_attributes:
            return random.choice(available_attributes)
        return None
    
    def generate_random_value(self, attribute):
        if attribute == "color":
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if attribute == "radius":
            return random.randint(5, 20)
        if attribute == "velocity":
            return pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3)

# Create initial organisms
num_organisms = 20
organisms = [Organism(random.randint(50, width - 50), random.randint(50, height - 50)) for _ in range(num_organisms)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    for org in organisms:
        org.update()
        pygame.draw.circle(screen, org.attributes["color"], (int(org.position.x), int(org.position.y)), org.attributes["radius"])
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
