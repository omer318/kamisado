import os

import pygame
from enums import COLOR
from textbox import Textbox


class Scoreboard:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.screen = self.setup_scoreboard()
        self.white_score = 0
        self.black_score = 0
        self.bg_color = COLOR.GRAY.value
        self.white_textbox = Textbox(self.screen, f"White: {self.white_score}", (self.height / 2, self.width / (4 / 3)),
                                     COLOR.BLACK.value, COLOR.WHITE.value)
        self.black_textbox = Textbox(self.screen, f"Black: {self.black_score}", (self.height / 2, self.width / 4),
                                     COLOR.WHITE.value, COLOR.BLACK.value)

    def setup_scoreboard(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 5)
        screen = pygame.display.set_mode((self.height, self.width))
        pygame.display.set_caption("Scoreboard")
        pygame.display.flip()
        return screen

    def main_loop(self, v):
        while True:
            self.screen.fill(self.bg_color)
            self.white_textbox.draw()
            self.black_textbox.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if v.value == 1:
                self.white_score += 1
                self.white_textbox.update(f"White: {self.white_score}")
                v.value = 0
            if v.value == 2:
                self.black_score += 1
                self.black_textbox.update(f"Black: {self.black_score}")
                v.value = 0
            pygame.display.flip()
