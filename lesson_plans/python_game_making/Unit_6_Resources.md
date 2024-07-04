# ## Learning Unit 6

## Learning Unit 6: Final Project - Complete Dodger Game
- Objectives:
  * Apply all learned concepts to create a complete game
  * Customize the game with local cultural elements
- Topics:
  * Game design and planning
  * Integrating all game elements
  * Debugging and testing
- Activities:
  * Develop the Dodger game with Timorese-themed graphics and sounds
  * Present and playtest games with classmates

## Required Resources
- Computer with Python 3.x and Pygame installed
- Text editor (e.g., IDLE, Visual Studio Code)
- Basic image editing software (e.g., GIMP)

## Suggested Items to Cover
- Basic game design principles
- Version control with Git
- Publishing games online or for mobile platforms

## Practical Experience and Community Engagement
- Organize a game showcase event for the local community
- Collaborate with local artists for game graphics and music
- Develop educational games for local schools or organizations

## Additional Resources
- Online Python tutorials and documentation
- Pygame documentation and examples
- Free game assets and sound libraries
- Local game development communities and forums

This syllabus has been adapted to the context of Timor-Leste by incorporating local cultural elements, using familiar examples, and suggesting community engagement activities relevant to the region. The structure provides a clear progression of learning units, each with specific objectives, topics, and activities tailored to the local context.

## Unit Resources

Here are detailed resources for Learning Unit 6: Final Project - Complete Dodger Game, formatted in Markdown:

# Resources for Learning Unit 6: Final Project - Complete Dodger Game

## 1. Lecture Notes

### Game Design and Planning

#### Introduction to Game Design Documents (GDD)
- Purpose: Blueprint for game development
- Key components:
  * Game concept and story
  * Gameplay mechanics
  * Visual style and art direction
  * Sound design
  * Technical requirements

#### Creating a GDD for Dodger Game
1. Game Concept:
   - Player controls a character avoiding falling objects
   - Timorese theme (e.g., traditional festival, historical event)
2. Gameplay Mechanics:
   - Movement controls (keyboard/mouse)
   - Scoring system
   - Difficulty progression
3. Visual Style:
   - Timorese-inspired graphics (characters, backgrounds)
   - UI design (score display, menu screens)
4. Sound Design:
   - Background music (traditional Timorese music)
   - Sound effects (collisions, point scoring)
5. Technical Requirements:
   - Python and Pygame
   - Minimum system requirements

### Integrating Game Elements

#### Main Game Loop Structure
```python
import pygame

# Initialize Pygame
pygame.init()

# Game setup
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game state
    
    # Draw game objects
    screen.fill((255, 255, 255))  # White background
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)

# Quit the game
pygame.quit()
```

#### Creating and Managing Game Objects
- Player character
- Falling objects
- Background elements

#### Implementing Core Mechanics
- Collision detection
- Scoring system
- Difficulty progression

### Debugging and Testing

#### Debugging Techniques
- Using print statements
- Pygame's debugging tools
- Common errors and solutions

#### Testing Strategies
- Playtesting methodology
- Gathering and implementing feedback
- Iterative improvement process

## 2. Discussion Questions

1. How can we incorporate Timorese cultural elements into the Dodger game while maintaining engaging gameplay?
2. What are some potential challenges in balancing difficulty progression in a game like Dodger, and how can we address them?
3. How might we adapt the Dodger game concept to create an educational game about Timorese history or culture?
4. What are the pros and cons of using keyboard controls versus mouse controls for the player character in Dodger?
5. How can sound design enhance the player's experience in a simple game like Dodger?

## 3. Writing Exercise Instructions

Create a detailed game design document (GDD) for your Timorese-themed Dodger game. Include the following sections:

1. Game Concept (100-150 words)
   - Describe the core idea of your game and its Timorese theme
2. Gameplay Mechanics (200-250 words)
   - Explain how the game is played, including controls and scoring
3. Visual Style (150-200 words)
   - Describe the art style and how it incorporates Timorese elements
4. Sound Design (100-150 words)
   - Outline your plans for background music and sound effects
5. Technical Requirements (50-100 words)
   - List the software and hardware needed to develop and play the game

## 4. Assignment Details

### Final Project: Timorese-Themed Dodger Game

#### Objectives:
- Apply all learned programming concepts to create a complete game
- Incorporate Timorese cultural elements into the game design
- Demonstrate understanding of game design principles

#### Requirements:
1. Functioning Dodger game implemented in Python using Pygame
2. Timorese-themed graphics and sounds
3. At least three levels of increasing difficulty
4. Score tracking and display
5. Start menu and game over screen
6. Background music and sound effects
7. Comments explaining key parts of the code

#### Deliverables:
1. Python source code files
2. Asset files (images, sounds)
3. Brief presentation (2-3 minutes) explaining your game concept and development process
4. Game design document (GDD)

#### Grading Criteria:
- Functionality (40%): Game works as intended without major bugs
- Creativity (20%): Innovative use of Timorese themes and game mechanics
- Code Quality (20%): Well-organized, commented, and efficient code
- Presentation (10%): Clear explanation of game concept and development process
- Documentation (10%): Comprehensive and well-written GDD

## 5. Additional Materials and Examples

### Sample Timorese-Themed Game Elements

1. Player Character Ideas:
   - Traditional Timorese warrior
   - Modern Timorese student
   - Symbolic animal (e.g., crocodile from Timorese legend)

2. Falling Objects:
   - Traditional crafts (e.g., tais patterns, woven baskets)
   - Local fruits (e.g., coconuts, mangoes)
   - Historical artifacts

3. Background Themes:
   - Dili waterfront
   - Mount Ramelau landscape
   - Traditional Timorese house (Uma Lulik)

4. Music and Sound:
   - Traditional instruments (e.g., kakalo'uta, baba-dook)
   - Ambient sounds from Timorese markets or nature

### Example Code Snippet: Adding Timorese Background Music

```python
import pygame

pygame.mixer.init()
background_music = pygame.mixer.Sound("timorese_traditional.wav")
background_music.play(-1)  # -1 means loop indefinitely
```

### Resource Links

1. Pygame Documentation: https://www.pygame.org/docs/
2. Free Timorese Music Samples: [Link to hypothetical resource]
3. Timor-Leste Cultural Heritage Images: [Link to hypothetical resource]
4. Game Design Document Templates: https://www.gamasutra.com/blogs/JasonBakker/20090604/84211/A_GDD_Template_for_the_Indie_Developer.php

This comprehensive set of resources provides students with the necessary materials, guidance, and examples to complete their final Dodger game project with a Timorese theme. The lecture notes, discussion questions, writing exercise, and assignment details are designed to reinforce learning and encourage creativity while applying programming skills in a culturally relevant context.