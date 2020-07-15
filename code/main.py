import pygame
import numpy as np
from pixel import Pixel
from brain import Brain


class MainGui:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Number Predictor')

        # neural network
        self.brain = Brain()
        # load train data
        self.brain.load("../nn_data/data.ckpt")

        self.WIDTH = 560
        self.HEIGHT = 560
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill(pygame.Color('#ffffff'))

        self.resolution = 28
        self.pixelWidth = self.WIDTH / self.resolution
        self.pixelHeigth = self.HEIGHT / self.resolution
        self.board = []

        for i in range(self.resolution):
            for j in range(self.resolution):
                self.board.append(Pixel(
                    self.pixelWidth * j, self.pixelHeigth * i, self.pixelWidth, self.pixelHeigth))

        self.isRunnning = True
        self.clock = pygame.time.Clock()

    def getBoard(self):
        newBoard = []
        for pixel in self.board:
            if pixel.painted:
                newBoard.append(1)
            else:
                newBoard.append(0)

        return np.array(newBoard)

    def makeGuess(self, board):
        return np.argmax(self.brain.guess(board))

    def run(self):
        painting = False

        while self.isRunnning:
            self.clock.tick(100)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.isRunnning = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    painting = True
                if event.type == pygame.MOUSEBUTTONUP:
                    painting = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        for pixel in self.board:
                            pixel.painted = False

                    if event.key == pygame.K_g:
                        print(f"Prediction: {self.makeGuess(self.getBoard())}")

            self.screen.blit(self.background, (0, 0))

            # store the mouse position for otmization
            currentMousePos = pygame.mouse.get_pos()
            for pixel in self.board:

                if pixel.checkUserCLicked(currentMousePos) and painting == True:
                    pixel.painted = True

                pixel.show(self.background)

            pygame.display.update()


if __name__ == "__main__":
    clss = MainGui()

    clss.run()
