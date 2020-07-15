import pygame


class Pixel():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # to define the thickness of the drawing
        self.paintRadius = 0

        # to define if it should be black or not
        self.painted = False

    def checkUserCLicked(self, mousePos):
        x, y = mousePos

        if x + self.paintRadius >= self.x and x - self.paintRadius < self.x + self.w:
            if y + self.paintRadius >= self.y and y - self.paintRadius < self.y + self.h:
                return True

    def show(self, screen):
        if self.painted:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
                self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                self.x, self.y, self.w, self.h))
