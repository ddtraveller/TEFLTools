import pygame
import sys
import random
import json

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 700
GAME_HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vocab Typer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Load vocabulary words and random words
with open('json/vocab.json', 'r') as f:
    vocab_data = json.load(f)
    vocab_words = {word['word']: word for word in vocab_data['vocabulary']}

with open('json/random_words.json', 'r') as f:
    random_words = json.load(f)

# Game variables
score = 0
words = []
game_active = True
explanations = []

class Player:
    def __init__(self):
        self.width = 60
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - 40
        self.speed = 5
        self.bullets = []

    def move_left(self):
        self.x = max(0, self.x - self.speed)

    def move_right(self):
        self.x = min(WIDTH - self.width, self.x + self.speed)

    def shoot(self):
        self.bullets.append(Bullet(self.x + self.width // 2, self.y))

    def update(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        for bullet in self.bullets:
            bullet.draw(screen)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.radius = 5

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

    def collides_with(self, word):
        return (self.x > word.x and self.x < word.x + 100 and
                self.y > word.y and self.y < word.y + 30)

class Word:
    def __init__(self, text, is_vocab):
        self.text = text
        self.is_vocab = is_vocab
        self.x = random.randint(0, WIDTH - 100)
        self.y = 0
        self.speed = random.randint(1, 3)
        self.color = WHITE

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))

class ExplanationText:
    def __init__(self, text):
        self.text = text
        self.creation_time = pygame.time.get_ticks()

    def draw(self, screen):
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (10, GAME_HEIGHT + 10))

    def should_remove(self):
        return pygame.time.get_ticks() - self.creation_time > 5000  # 5 seconds

def game_over(win):
    global score, game_active
    game_active = False
    screen.fill(BLACK)
    if win:
        game_over_text = font.render(f"You win! Final score: {score}", True, GREEN)
    else:
        game_over_text = font.render(f"Game Over! Final score: {score}", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    
    play_again_text = font.render("Press SPACE to play again or ESC to quit", True, WHITE)
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 50))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def reset_game():
    global score, words, player, game_active, explanations
    score = 0
    words = []
    player = Player()
    game_active = True
    explanations = []

player = Player()
clock = pygame.time.Clock()

def main():
    global score, words, player, game_active, explanations
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_SPACE:
                    player.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        if game_active:
            screen.fill(BLACK)

            player.update()
            player.draw(screen)

            if random.randint(1, 100) == 1:
                word_text = random.choice(list(vocab_words.keys()) if random.random() < 0.3 else random_words)
                is_vocab = word_text in vocab_words
                words.append(Word(word_text, is_vocab))

            words_to_remove = []
            words_hit = []

            for word in words:
                word.move()
                word.draw(screen)

                if word.y > GAME_HEIGHT:
                    words_to_remove.append(word)
                    if word.is_vocab:
                        score -= 5
                        if score <= -100:
                            game_over(False)

                for bullet in player.bullets[:]:
                    if bullet.collides_with(word):
                        words_hit.append(word)
                        words_to_remove.append(word)
                        player.bullets.remove(bullet)
                        if word.is_vocab:
                            score += 10
                            if score >= 100:
                                game_over(True)
                            explanation = vocab_words[word.text]['definition']
                            explanations = [ExplanationText(explanation)]
                        else:
                            score -= 2

            for word in words_to_remove:
                if word in words:
                    words.remove(word)

            if explanations:
                explanations[0].draw(screen)
                if explanations[0].should_remove():
                    explanations.clear()

            pygame.draw.line(screen, WHITE, (0, GAME_HEIGHT), (WIDTH, GAME_HEIGHT), 2)

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)
        else:
            game_over(score >= 100)

if __name__ == "__main__":
    main()