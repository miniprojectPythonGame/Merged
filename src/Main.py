from src.pages.login_screen.LoginScreen import LoginScreen

from globals.const_values import *


def getWindowSize():
    return SCREEN_WIDTH * SIZE_FACTOR, SCREEN_HEIGHT * SIZE_FACTOR


# Pygame initials
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Heroic: Login screen")
programIcon = pygame.image.load('../images/icon.png')
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode(getWindowSize(), 0, 32)
base_font = pygame.font.Font(None, 32)

if __name__ == "__main__":
    LoginScreen(screen, mainClock)
