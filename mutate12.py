import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fish Eating Simulation")

# Colors
WHITE = (255, 255, 255)

# Fish class
class Fish:
    def __init__(self, x, y, color):
        self.position = pygame.Vector2(x, y)
        self.color = color
        self.radius = 10
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 3)
        self.health = 100  # Introduce a health attribute
    
    def update(self):
        self.position += self.velocity
        self.bounce()
        self.health -= 0.1  # Decrease health over time
        self.color = (self.color[0], max(0, self.color[1] - 0.1 * self.health), self.color[2])
    
    def bounce(self):
        if self.position.x < 0 or self.position.x > width:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
    
    def collide(self, other_fish):
        distance = self.position.distance_to(other_fish.position)
        return distance <= self.radius + other_fish.radius
    
    def eat(self, other_fish):
        if self.collide(other_fish) and self.color != other_fish.color:
            self.health += 30  # Increase health after eating
            return True
        return False

# Create initial fish
num_fish = 20
fish = [Fish(random.randint(50, width - 50), random.randint(50, height - 50), 
             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) 
        for _ in range(num_fish)]

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
        pygame.draw.circle(screen, f.color, (int(f.position.x), int(f.position.y)), f.radius)
        
        for other_f in fish:
            if f != other_f:
                if f.eat(other_f):
                    fish.remove(other_f)
                    new_fish.append(Fish(f.position.x + random.uniform(-20, 20),
                                         f.position.y + random.uniform(-20, 20),
                                         f.color))
    
    fish.extend(new_fish)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
