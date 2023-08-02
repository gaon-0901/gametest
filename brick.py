import pygame

class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, display):
        # 벽돌을 그립니다.
        pygame.draw.rect(display, (102, 51, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height), 5)

    def getrect(self):
        # 충돌 영역을 크게 설정하여 반환합니다.
        padding_x = 0
        padding_y = 0
        return pygame.Rect(self.x - padding_x, self.y - padding_y, self.width + padding_x*2, self.height + padding_y*2)

    def check_collision(self, ball_rect):
        # 벽돌과 공의 충돌을 감지합니다.
        brick_rect = self.getrect()
        return brick_rect.colliderect(ball_rect)
