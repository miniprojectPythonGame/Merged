from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes

from .Button import Button

# WINDOW PARAMETERS
size_factor = SIZE_FACTOR
window_width = SCREEN_WIDTH * size_factor
window_height = SCREEN_HEIGHT * size_factor
margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12 * 0.5)

# NAVBAR MEASURES
navbar_width = 80
navbar_height = window_height
navbar_padding_vert = 20
navbar_padding_hori = 15
buttons_size = navbar_width - 2 * navbar_padding_hori

navbar = {
    "colors": ColorSchemes(),
    "x": 0,
    "y": 0,
    "width": navbar_width,
    "height": navbar_height,
}

# BUTTON: Character Profile
bt_profile = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": navbar_padding_vert,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/navbar/user_white.png',
}

# BUTTON: Settings
bt_settings = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": 2 * navbar_padding_vert + buttons_size,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/navbar/settings_white.png',
}

# BUTTON: World map
bt_world_map = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": 3 * navbar_padding_vert + 2 * buttons_size,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/navbar/map_white.png',
}

# BUTTON: Swap hero
bt_swap_hero = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": 4 * navbar_padding_vert + 3 * buttons_size,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/navbar/swap_hero.png',
}

# BUTTON: Logout
bt_logout = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": navbar_height - (navbar_padding_vert + buttons_size),
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/navbar/logout.png',
}


class Navbar():
    def __init__(self, screen):
        self.colorSchemes = ColorSchemes()
        self.color = self.colorSchemes.inactive
        self.x = navbar['x']
        self.y = navbar['y']
        self.width = navbar['width']
        self.height = navbar['height']
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bt_profile = Button(bt_profile['color'], bt_profile['x'], bt_profile['y'],
                                 bt_profile['width'], bt_profile['height'], self.screen,
                                 path=bt_profile['path'])
        self.bt_settings = Button(bt_settings['color'], bt_settings['x'], bt_settings['y'],
                                  bt_settings['width'], bt_settings['height'], self.screen,
                                  path=bt_settings['path'])
        self.bt_world_map = Button(bt_world_map['color'], bt_world_map['x'], bt_world_map['y'],
                                   bt_world_map['width'], bt_world_map['height'], self.screen,
                                   path=bt_world_map['path'])
        self.bt_swap_hero = Button(bt_swap_hero['color'], bt_swap_hero['x'], bt_swap_hero['y'],
                                   bt_swap_hero['width'], bt_swap_hero['height'], self.screen,
                                   path=bt_swap_hero['path'])
        self.bt_logout = Button(bt_logout['color'], bt_logout['x'], bt_logout['y'],
                                   bt_logout['width'], bt_logout['height'], self.screen,
                                   path=bt_logout['path'])

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.bt_profile.draw()
        self.bt_settings.draw()
        self.bt_world_map.draw()
        self.bt_swap_hero.draw()
        self.bt_logout.draw()
