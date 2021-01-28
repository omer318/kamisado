import pygame


class Textbox:
    pygame.font.init()

    def __init__(self, screen, txt, location, fg, bg, margin=20, font=pygame.font.Font('freesansbold.ttf', 70)):
        self.fg = fg
        self.bg = bg
        self.location = location
        self.margin = margin
        self.font = font
        self.txt = txt
        self.txt_surf = self.get_surface()
        self.txt_rect = self.txt_surf.get_rect(center=location)
        self.screen = screen
        self.rect = self.get_rect()

    def draw(self):
        pygame.draw.rect(self.screen, self.bg, self.rect)
        self.screen.blit(self.txt_surf, self.txt_rect)

    def update(self, txt):
        self.font.size("100")
        self.txt = txt
        self.txt_surf = self.get_surface()
        self.draw()

    def get_surface(self):
        return self.font.render(self.txt, True, self.fg)

    def get_rect(self):
        rect = pygame.rect.Rect((1, 1), (self.screen.get_width(), self.screen.get_height() / 2))
        rect.center = self.location
        return rect
