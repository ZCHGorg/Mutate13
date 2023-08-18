import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colorful Evolution Simulation")

# Mutation rate (adjust as needed)
MUTATION_RATE = 0.1

# Organism class
class Organism:
    def __init__(self, x, y, color):
        self.position = pygame.Vector2(x, y)
        self.color = color
        self.radius = 10
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3)
    
    def update(self):
        self.position += self.velocity
        self.bounce()
    
    def bounce(self):
        if self.position.x < 0 or self.position.x > width:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
    
    def collide(self, other_organism):
        distance = self.position.distance_to(other_organism.position)
        return distance <= self.radius + other_organism.radius
    
    def breed(self, other_organism):
        if self.collide(other_organism):
            new_color = self.mutate_color(self.mix_colors(self.color, other_organism.color))
            new_x = (self.position.x + other_organism.position.x) / 2
            new_y = (self.position.y + other_organism.position.y) / 2
            return Organism(new_x, new_y, new_color)
        return None
    
    def eat(self, other_organism):
        if self.collide(other_organism):
            return self.color != other_organism.color
        return False
    
    def mix_colors(self, color1, color2):
        return tuple((c1 + c2) // 2 for c1, c2 in zip(color1, color2))
        
    def mutate_color(self, color):
        return tuple(
            max(0, min(int(c + random.uniform(-MUTATION_RATE, MUTATION_RATE) * 255), 255))
            for c in color
        )

# Create initial organisms
num_organisms = 20
organisms = [Organism(random.randint(50, width - 50), random.randint(50, height - 50), 
                      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) 
              for _ in range(num_organisms)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    new_organisms = []
    
    for org in organisms:
        org.update()
        pygame.draw.circle(screen, org.color, (int(org.position.x), int(org.position.y)), org.radius)
        
        for other_org in organisms:
            if org != other_org:
                new_org = org.breed(other_org)
                if new_org:
                    new_organisms.append(new_org)
                if org.eat(other_org):
                    organisms.remove(other_org)
    
    organisms.extend(new_organisms)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
