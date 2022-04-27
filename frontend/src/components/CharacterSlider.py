from .CharacterPreview import CharacterPreview
from frontend.src.pages.choose_character.Measurements import Measurements as meas

class CharacterSlider:
    def __init__(self, characters, screen):
        self.characters = characters
        self.curr_index = None
        self.curr_main = None
        self.curr_left = None
        self.curr_right = None
        self.screen = screen
        self.initiateIndex()
        self.loadVisible()

    def initiateIndex(self):
        if len(self.characters) < 1:
            print("[ChooseCharacter > CharacterSlider > initiateIndex]: Error")

        if len(self.characters) == 1:
            self.curr_index = 0

        if len(self.characters) > 1:
            self.curr_index = 1

    def loadVisible(self):
        self.curr_main = CharacterPreview(meas.cp_main['x'], meas.cp_main['y'],
                                          meas.cp_main['width'], meas.cp_main['height'],
                                          meas.cp_main['bar_width'], meas.cp_main['bar_height'],
                                          self.characters[self.curr_index]['name'],
                                          self.characters[self.curr_index]['spec'],
                                          self.characters[self.curr_index]['level'],
                                          self.characters[self.curr_index]['img'],
                                          self.screen, meas.cp_main['font'])

        if self.curr_index - 1 >= 0:
            self.curr_left = CharacterPreview(meas.cp_left['x'], meas.cp_left['y'],
                                              meas.cp_left['width'], meas.cp_left['height'],
                                              meas.cp_left['bar_width'], meas.cp_left['bar_height'],
                                              self.characters[self.curr_index - 1]['name'],
                                              self.characters[self.curr_index - 1]['spec'],
                                              self.characters[self.curr_index - 1]['level'],
                                              self.characters[self.curr_index - 1]['img'],
                                              self.screen, meas.cp_left['font'])
        else:
            self.curr_left = None

        if self.curr_index + 1 < len(self.characters):
            self.curr_right = CharacterPreview(meas.cp_right['x'], meas.cp_right['y'],
                                               meas.cp_right['width'], meas.cp_right['height'],
                                               meas.cp_right['bar_width'], meas.cp_right['bar_height'],
                                               self.characters[self.curr_index + 1]['name'],
                                               self.characters[self.curr_index + 1]['spec'],
                                               self.characters[self.curr_index + 1]['level'],
                                               self.characters[self.curr_index + 1]['img'],
                                               self.screen, meas.cp_right['font'])
        else:
            self.curr_right = None

    def draw(self):
        self.curr_main.draw()
        if self.curr_left:
            self.curr_left.draw()
        if self.curr_right:
            self.curr_right.draw()

    def swipeLeft(self):
        print('Prev')
        if self.curr_index > 0:
            self.curr_index -= 1
            self.loadVisible()

    def swipeRight(self):
        print('Next')
        if self.curr_index < len(self.characters) - 1:
            self.curr_index += 1
            self.loadVisible()