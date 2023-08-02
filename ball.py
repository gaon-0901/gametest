import pygame

class Ball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.ballImage = pygame.image.load("./ball.png")
        # self.ballImage = pygame.transform.scale(self.ballImage, (self.width, self.height))
        print(self.ballImage.get_size()[0], self.ballImage.get_size()[1])

    def draw(self, display, x, y):
        # 공 이미지를 주어진 위치에 그립니다.
        display.blit(self.ballImage, [x, y])

    def getrect(self):
        # 공 이미지의 사각형 영역 정보를 반환합니다.
        return self.ballImage.get_rect()
