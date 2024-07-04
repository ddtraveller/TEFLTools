# ## Learning Unit 2

## Learning Unit 2: Drawing and Animation
- Objectives:
  * Learn to draw shapes and images on screen
  * Implement basic animation techniques
- Topics:
  * Pygame drawing functions
  * Loading and displaying images
  * Simple animation with Pygame
- Activities:
  * Draw Timor-Leste flag using Pygame shapes
  * Animate a local cultural symbol (e.g., tais pattern)

## Unit Resources

Here are detailed resources for Learning Unit 2: Drawing and Animation, formatted in Markdown:

# Learning Unit 2: Drawing and Animation - Detailed Resources

## 1. Lecture Notes

### Drawing Shapes with Pygame

#### Introduction to Pygame Drawing
- Pygame uses a coordinate system where (0, 0) is the top-left corner
- X-axis increases to the right, Y-axis increases downwards
- All drawing happens on a Surface object

#### Basic Drawing Functions
1. `pygame.draw.rect(surface, color, rect, width=0)`
   - Draws a rectangle
   - `surface`: where to draw
   - `color`: RGB tuple, e.g., (255, 0, 0) for red
   - `rect`: (x, y, width, height) or pygame.Rect object
   - `width`: thickness of outline (0 for filled shape)

2. `pygame.draw.circle(surface, color, center, radius, width=0)`
   - Draws a circle
   - `center`: (x, y) tuple for circle's center
   - `radius`: radius of the circle

3. `pygame.draw.line(surface, color, start_pos, end_pos, width=1)`
   - Draws a line
   - `start_pos` and `end_pos`: (x, y) tuples

#### Color in Pygame
- Colors are represented as RGB tuples
- Values range from 0 to 255
- Common colors:
  * Black: (0, 0, 0)
  * White: (255, 255, 255)
  * Red: (255, 0, 0)
  * Green: (0, 255, 0)
  * Blue: (0, 0, 255)

### Loading and Displaying Images

#### Loading Images
- Use `pygame.image.load(filename)` to load an image
- Supported formats: JPG, PNG, GIF (non-animated), BMP, PCX, TGA, TIF, LBM, PBM, XPM
- Example: `image = pygame.image.load("tais_pattern.png")`

#### Displaying Images
- Use `surface.blit(source, dest, area=None, special_flags=0)` to draw one surface on another
- `source`: Surface to draw
- `dest`: position to draw at (can be tuple or Rect)
- Example: `screen.blit(image, (100, 100))`

### Basic Animation Techniques

#### Animation Principles
- Animation is created by rapidly displaying slightly different images
- In Pygame, this is achieved by redrawing the screen in each frame

#### Frame Rate
- Controlled using `pygame.time.Clock()`
- Set desired frames per second (FPS) with `clock.tick(FPS)`

#### Moving Objects
1. Clear the screen (usually by filling with a background color)
2. Update object positions
3. Redraw all objects
4. Update the display with `pygame.display.flip()` or `pygame.display.update()`

#### Example Animation Loop
```python
clock = pygame.time.Clock()
x = 0  # Initial x position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear screen with white
    
    x += 1  # Move object to the right
    pygame.draw.rect(screen, (255, 0, 0), (x, 100, 50, 50))  # Draw red square
    
    pygame.display.flip()  # Update display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
```

## 2. Discussion Questions

1. How does the coordinate system in Pygame differ from a traditional mathematical coordinate system?
2. What are the advantages and disadvantages of using drawing functions vs. loading images in game development?
3. How might you use animation to represent aspects of Timorese culture in a game?
4. Discuss the importance of frame rate in game development. How might a low frame rate affect user experience?
5. How can you use color theory in game design to create visually appealing and culturally relevant graphics?

## 3. Writing Exercise Instructions

Write a short essay (250-300 words) on the following topic:

"The Role of Visual Elements in Preserving and Promoting Timorese Culture through Game Development"

Consider the following points in your essay:
- The significance of traditional patterns and symbols in Timorese culture
- How game graphics can be used to educate players about Timorese heritage
- The balance between authenticity and creativity in representing culture through digital art
- Potential challenges in translating physical art forms (like tais weaving) into digital game elements

## 4. Assignment Details

### Assignment 1: Timor-Leste Flag Drawing

Create a Pygame program that draws the flag of Timor-Leste using Pygame's drawing functions.

Requirements:
- Use `pygame.draw.polygon()` for the triangle
- Use `pygame.draw.rect()` for the rectangles
- Ensure correct proportions and colors
- Add a simple animation (e.g., a subtle wave effect)

Submission: Python script file (.py)

### Assignment 2: Animated Tais Pattern

Create a Pygame program that loads a tais pattern image and animates it.

Requirements:
- Load a tais pattern image (provided or found online with proper attribution)
- Implement at least two of the following animations:
  * Scrolling the pattern across the screen
  * Rotating the pattern
  * Scaling the pattern (growing/shrinking)
  * Color shifting (if using a simplified pattern)
- Allow user to switch between animations using keyboard input

Submission: Python script file (.py) and any used image files

## 5. Additional Resources

### Pygame Drawing Documentation
https://www.pygame.org/docs/ref/draw.html

### Color Theory Basics
https://www.interaction-design.org/literature/topics/color-theory

### Timor-Leste Flag Specifications
https://en.wikipedia.org/wiki/Flag_of_East_Timor

### Tais Patterns of Timor-Leste
https://en.wikipedia.org/wiki/Tais

### Animation Principles for Game Developers
https://www.gamasutra.com/view/feature/131581/principles_of_animation_for_.php

## 6. Code Examples

### Basic Shape Drawing
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((255, 255, 255))  # White background

# Drawing a red rectangle
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 80))

# Drawing a blue circle
pygame.draw.circle(screen, (0, 0, 255), (250, 150), 60)

# Drawing a green line
pygame.draw.line(screen, (0, 255, 0), (10, 200), (390, 200), 5)

pygame.display.flip()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

### Simple Animation
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

x = 0  # Initial x position of the square

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear screen with white
    
    x = (x + 2) % 400  # Move square and wrap around screen
    pygame.draw.rect(screen, (255, 0, 0), (x, 100, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
```

These resources provide a comprehensive foundation for the Drawing and Animation unit, with a focus on practical application and cultural relevance to Timor-Leste.