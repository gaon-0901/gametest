import pygame


class Bar:
    def __init__(self, x, y, width, height, gHeight):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.gHeight = gHeight
        self.barImage = pygame.image.load("./bar.png")
        # self.barImage = pygame.transform.scale(self.barImage, (self.width, self.height))
        print(self.barImage.get_size()[0], self.barImage.get_size()[1])

    def draw(self, display, x, y):
        # 바 이미지를 주어진 위치에 그립니다.
        display.blit(self.barImage, [x, y])

    def getrect(self):
        # 바 이미지의 사각형 영역 정보를 반환합니다.
        return self.barImage.get_rect()
