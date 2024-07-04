# ## Learning Unit 4

## Learning Unit 4: Collision Detection and Game Logic
- Objectives:
  * Understand and implement collision detection
  * Develop game rules and scoring system
- Topics:
  * Rectangular collision detection
  * Implementing game rules
  * Scoring and game state management
- Activities:
  * Create a simple collection game with local fruits (e.g., coconuts, papayas)
  * Implement scoring based on collected items

## Unit Resources

Here are detailed resources for Learning Unit 4: Collision Detection and Game Logic, formatted in Markdown:

# Learning Unit 4: Collision Detection and Game Logic Resources

## 1. Lecture Notes

### Collision Detection

#### Introduction to Collision Detection
- Collision detection is a fundamental concept in game development
- It determines when game objects interact or overlap
- Essential for gameplay mechanics like collecting items, avoiding obstacles, etc.

#### Rectangular Collision Detection
- Simplest form of collision detection
- Uses bounding boxes (rectangles) to approximate object shapes
- Pygame provides the `Rect` class for easy rectangle manipulation

#### Implementing Collision Detection with Pygame
```python
# Example code for rectangular collision detection
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(120, 120, 60, 60)

if rect1.colliderect(rect2):
    print("Collision detected!")
```

- `colliderect()` method checks if two rectangles overlap
- Can be used for player-item collisions, player-enemy collisions, etc.

### Game Rules and Scoring

#### Importance of Game Rules
- Rules define how the game is played
- Create structure and challenge for the player
- Examples: collecting items, avoiding obstacles, time limits

#### Implementing a Basic Scoring System
```python
score = 0

# Increase score when player collects an item
if player_rect.colliderect(item_rect):
    score += 10
    # Remove the collected item
    items.remove(item)

# Display score
font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))
```

#### Managing Game States
- Common game states: playing, paused, game over
- Use variables to track current state
```python
PLAYING = 0
PAUSED = 1
GAME_OVER = 2

current_state = PLAYING

# In the game loop
if current_state == PLAYING:
    # Update game logic
elif current_state == PAUSED:
    # Display pause menu
elif current_state == GAME_OVER:
    # Display game over screen
```

## 2. Discussion Questions

1. How does collision detection contribute to gameplay in various game genres?
2. What are the advantages and disadvantages of using rectangular collision detection?
3. How can we make collision detection more precise for irregularly shaped objects?
4. Why is a scoring system important in games? How does it affect player motivation?
5. What are some creative ways to implement game rules that are culturally relevant to Timor-Leste?
6. How can different game states enhance the overall gaming experience?

## 3. Writing Exercise Instructions

Write a short design document (300-500 words) for a simple collection game set in Timor-Leste. Include the following elements:

1. Game concept and objective
2. Description of the player character and collectible items
3. Scoring system and rules
4. How collision detection will be used in the game
5. At least two different game states and how they will be managed
6. Cultural elements from Timor-Leste incorporated into the game

## 4. Assignment Details

### Fruit Collection Game

Create a simple fruit collection game using Pygame with the following requirements:

1. Player-controlled character that moves using arrow keys
2. At least three types of falling fruits (e.g., coconuts, papayas, bananas)
3. Implement collision detection between the player and fruits
4. Scoring system with different point values for each fruit type
5. Display the current score on the screen
6. Implement a game over condition (e.g., time limit or missed fruits)
7. Create a game over screen displaying the final score
8. Add sound effects for collecting fruits and game over

Bonus challenges:
- Add power-ups that temporarily change game mechanics
- Implement levels with increasing difficulty
- Create a high score system that persists between game sessions

## 5. Additional Resources and Examples

### Collision Detection Visualization

Create a simple Pygame program that demonstrates collision detection visually:

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

rect1 = pygame.Rect(50, 50, 100, 80)
rect2 = pygame.Rect(200, 150, 80, 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect2.center = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)

    if rect1.colliderect(rect2):
        pygame.draw.rect(screen, (255, 255, 255), rect1.clip(rect2), 3)

    pygame.display.flip()
    clock.tick(60)
```

This example allows students to move one rectangle with the mouse and see the collision area highlighted when it overlaps with the stationary rectangle.

### Scoring System Example

```python
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

player = pygame.Rect(175, 250, 50, 50)
fruits = []
score = 0
font = pygame.font.Font(None, 36)

def spawn_fruit():
    x = random.randint(0, 350)
    fruits.append(pygame.Rect(x, 0, 30, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    player.clamp_ip(screen.get_rect())

    if random.randint(1, 30) == 1:
        spawn_fruit()

    for fruit in fruits[:]:
        fruit.y += 3
        if fruit.top > 300:
            fruits.remove(fruit)
        elif fruit.colliderect(player):
            fruits.remove(fruit)
            score += 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for fruit in fruits:
        pygame.draw.rect(screen, (255, 0, 0), fruit)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
```

This example demonstrates a simple fruit collection game with scoring, which students can use as a starting point for their assignment.

These resources provide a comprehensive set of materials for teaching collision detection and game logic in the context of Timor-Leste, including lecture notes, discussion questions, exercises, and code examples.