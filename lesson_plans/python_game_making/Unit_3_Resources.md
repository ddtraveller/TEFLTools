# ## Learning Unit 3

## Learning Unit 3: User Input and Game Controls
- Objectives:
  * Handle keyboard and mouse input
  * Implement player movement
- Topics:
  * Pygame event handling
  * Keyboard and mouse input
  * Moving game objects
- Activities:
  * Create a program to move a character using arrow keys
  * Implement mouse control for character movement

## Unit Resources

Here are detailed resources for Learning Unit 3: User Input and Game Controls, formatted in Markdown:

# Learning Unit 3: User Input and Game Controls - Detailed Resources

## 1. Lecture Notes

### Introduction to Pygame Event Handling

- Events in Pygame represent user actions or system occurrences
- The event loop continuously checks for and processes events
- Basic structure of an event loop:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game logic and drawing code here

    pygame.display.flip()

pygame.quit()
```

### Keyboard Input

- Pygame provides constants for keyboard keys (e.g., `pygame.K_UP`, `pygame.K_SPACE`)
- Two main ways to handle keyboard input:
  1. Event-based: Check for `pygame.KEYDOWN` and `pygame.KEYUP` events
  2. State-based: Use `pygame.key.get_pressed()` for continuous input

Example of event-based input:

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("Left arrow pressed")
        elif event.key == pygame.K_RIGHT:
            print("Right arrow pressed")
```

Example of state-based input:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player_x -= 5
if keys[pygame.K_RIGHT]:
    player_x += 5
```

### Mouse Input

- Mouse events include movement, button clicks, and scroll wheel
- Common mouse events:
  - `pygame.MOUSEMOTION`: Mouse movement
  - `pygame.MOUSEBUTTONDOWN`: Mouse button pressed
  - `pygame.MOUSEBUTTONUP`: Mouse button released

Example of mouse input:

```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            print("Left click at", event.pos)
    elif event.type == pygame.MOUSEMOTION:
        print("Mouse moved to", event.pos)
```

### Moving Game Objects

- Update object positions based on input in the game loop
- Consider frame rate and delta time for smooth movement
- Example of moving a player sprite:

```python
player_x, player_y = 400, 300
player_speed = 5

# In the game loop
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player_x -= player_speed
if keys[pygame.K_RIGHT]:
    player_x += player_speed
if keys[pygame.K_UP]:
    player_y -= player_speed
if keys[pygame.K_DOWN]:
    player_y += player_speed

# Draw the player at the new position
screen.blit(player_image, (player_x, player_y))
```

## 2. Discussion Questions

1. How does event handling in Pygame differ from traditional input methods in console applications?
2. What are the advantages and disadvantages of event-based vs. state-based keyboard input?
3. How can mouse input enhance the user experience in a game? Provide examples from games you've played.
4. Discuss the importance of smooth movement in games. How can we ensure consistent movement across different devices?
5. How might you implement diagonal movement using keyboard controls? What challenges might this present?
6. In what ways could you use mouse input to control character movement instead of keyboard input?
7. How could you combine keyboard and mouse input to create more complex game controls?

## 3. Writing Exercise Instructions

Write a short design document (300-500 words) for a simple game that utilizes both keyboard and mouse input. Include the following elements:

1. Game concept and objective
2. Description of player character or controlled object
3. Detailed explanation of keyboard controls
4. Detailed explanation of mouse controls
5. How the two input methods complement each other
6. Any challenges you foresee in implementing these controls

## 4. Assignment Details

### Character Movement Game

Create a Pygame program that implements the following features:

1. A player character (use a simple shape or image) that can move in four directions using arrow keys
2. The ability to "sprint" (move faster) when holding the Shift key
3. A target object that appears at random locations when the player clicks the mouse
4. A score that increases each time the player character touches the target object
5. Display the score and a timer on the screen
6. End the game after 60 seconds and display a "Game Over" message with the final score

Requirements:
- Use both event-based and state-based input handling
- Implement smooth movement for the player character
- Ensure the character and target cannot move outside the screen boundaries
- Add sound effects for movement and collecting the target (use placeholder sounds)

Bonus challenges:
- Add acceleration and deceleration to the character's movement
- Implement diagonal movement
- Create obstacles that the player must avoid

## 5. Additional Resources

### Code Examples

1. Basic event loop with quit functionality:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill((255, 255, 255))  # Fill screen with white
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
```

2. Simple character movement with keyboard:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x, player_y = 400, 300
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(player_x), int(player_y)), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

3. Mouse input example:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                print(f"Left click at {event.pos}")
            elif event.button == 3:  # Right click
                print(f"Right click at {event.pos}")
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse moved to {event.pos}")
    
    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### Useful Links

1. [Pygame Documentation - Event handling](https://www.pygame.org/docs/ref/event.html)
2. [Pygame Documentation - Keyboard](https://www.pygame.org/docs/ref/key.html)
3. [Pygame Documentation - Mouse](https://www.pygame.org/docs/ref/mouse.html)
4. [Real Python - Pygame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
5. [Pygame Newbie Guide - Input Handling](https://nerdparadise.com/programming/pygame/part3)

These resources provide a comprehensive set of materials for teaching and learning about user input and game controls in Pygame. The lecture notes, discussion questions, writing exercise, assignment, and additional resources offer a mix of theoretical knowledge and practical application to help students understand and implement these concepts in their game projects.