import pygame
import os
import time

def main():
    # Initialize pygame
    pygame.init()
    
    # Set display environment variables
    os.environ['SDL_VIDEODRIVER'] = 'kms'
    os.environ['DISPLAY'] = ':0'
    
    # Initialize the display
    pygame.display.init()
    
    # Get the current display info
    display_info = pygame.display.Info()
    
    # Set up the display at full screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Hello Display')

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Clear the screen with black background
    screen.fill(BLACK)

    try:
        # Try to use font rendering
        font = pygame.font.Font(None, 74)
        text = font.render('Hello', True, WHITE)
    except (NotImplementedError, ImportError):
        # Fallback: Create a simple surface with text
        text = pygame.Surface((200, 50))
        text.fill(BLACK)
        pygame.draw.line(text, WHITE, (0, 25), (200, 25), 5)
        pygame.draw.line(text, WHITE, (0, 0), (0, 50), 5)
        pygame.draw.line(text, WHITE, (100, 0), (100, 50), 5)
        pygame.draw.line(text, WHITE, (200, 0), (200, 50), 5)

    # Get the rectangle containing the text
    text_rect = text.get_rect()

    # Center the text on screen
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Keep the window open
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pygame.quit()

if __name__ == '__main__':
    main() 