Here's a comprehensive resource on Pygame documentation and examples for Unit 6:

# Pygame Documentation and Examples

## 1. Introduction to Pygame

Pygame is a set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

### Key Features:
- Cross-platform
- Built on top of SDL (Simple DirectMedia Layer)
- Supports both 2D and 3D graphics
- Provides modules for handling events, drawing, image and sound loading, and more

## 2. Installation

To install Pygame, use pip:

```
pip install pygame
```

## 3. Basic Structure of a Pygame Program

```python
import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game logic here
    
    # Drawing code here
    
    pygame.display.flip()

pygame.quit()
```

## 4. Key Pygame Modules

### 4.1 pygame.display
- Manages the display window and screen
- Key functions:
  - `set_mode()`: Initialize a window for display
  - `flip()`: Update the full display

### 4.2 pygame.event
- Manages events and the event queue
- Key functions:
  - `get()`: Get events from the queue

### 4.3 pygame.draw
- Contains drawing functions
- Examples:
  - `rect()`: Draw a rectangle
  - `circle()`: Draw a circle

### 4.4 pygame.image
- Handles image loading and saving
- Key functions:
  - `load()`: Load an image from a file

### 4.5 pygame.mixer
- Handles sound playback
- Key functions:
  - `Sound()`: Create a Sound object from a file

## 5. Examples

### 5.1 Drawing Shapes

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Draw a red rectangle
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))

# Draw a blue circle
pygame.draw.circle(screen, (0, 0, 255), (200, 150), 50)

pygame.display.flip()
```

### 5.2 Loading and Displaying Images

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Load an image
image = pygame.image.load("player.png")

# Display the image
screen.blit(image, (100, 100))

pygame.display.flip()
```

### 5.3 Handling User Input

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space bar pressed!")

    pygame.display.flip()

pygame.quit()
```

### 5.4 Playing Sounds

```python
import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("beep.wav")
sound.play()

pygame.time.wait(1000)  # Wait for 1 second
```

## 6. Useful Resources

- Official Pygame Documentation: https://www.pygame.org/docs/
- Pygame Tutorials: https://www.pygame.org/wiki/tutorials
- Pygame Examples: https://www.pygame.org/docs/ref/examples.html

## 7. Tips for the Dodger Game Project

- Use `pygame.sprite.Sprite` for game objects
- Implement collision detection with `pygame.sprite.spritecollide()`
- Use `pygame.time.Clock` to control the game's frame rate
- Organize your code into classes for better structure
- Use Pygame's event system for user input and game events

This resource provides a solid foundation for students to understand and use Pygame in their final Dodger game project, incorporating the key concepts and functions they'll need.