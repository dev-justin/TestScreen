import pygame
import os
import time

def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    # The Waveshare 5inch DSI LCD has a resolution of 800x480
    os.environ['SDL_FBDEV'] = '/dev/fb0'
    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption('Hello Display')

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Clear the screen with black background
    screen.fill(BLACK)

    # Set up the font
    font = pygame.font.Font(None, 74)  # None uses default font, 74 is the size

    # Render the text
    text = font.render('Hello', True, WHITE)

    # Get the rectangle containing the text
    text_rect = text.get_rect()

    # Center the text on screen
    text_rect.center = (800 // 2, 480 // 2)

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