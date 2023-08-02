import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, KEYUP
from ball import Ball
from bar import Bar
from brick import Brick

pygame.init()

myFont = pygame.font.Font("Nanum.ttf", 50)
myFont2 = pygame.font.Font("Nanum.ttf", 20)
background = pygame.display.set_mode((640, 480))
pygame.display.set_caption("게임")

fps = pygame.time.Clock()

black = 0, 0, 0
white = 255, 255, 255
Playing, Ready = True, True

bar_x_pos = background.get_size()[0] // 2 - 115 // 2
bar_y_pos = background.get_size()[1] - 50

bar = Bar(bar_x_pos, bar_y_pos, 115, 23, 100)
ball = Ball(bar_x_pos + bar_x_pos // 2, bar_y_pos - bar.height, 22, 23)
ball_x, ball_y = 0, 0
bar_dl, bar_dr = 0, 0
ball_dx, ball_dy = 0, 0

brick_width, brick_height = 80, 40
brick_spacing = 0  # 벽돌 사이의 간격
num_bricks = 8  # 설치할 벽돌의 개수
total_bricks_width = num_bricks * (brick_width + brick_spacing) - brick_spacing
brick_x = background.get_size()[0] // 2 - total_bricks_width // 2  # 화면 중앙에 벽돌들을 나란히 배치
brick_y = 0

# 벽돌 객체들을 리스트에 저장합니다.
bricks = []
for i in range(num_bricks):
    bricks.append(Brick(brick_x + i * (brick_width + brick_spacing), brick_y, brick_width, brick_height))

# ball의 상수 속도를 정의합니다. (밀리초당 픽셀 수)
BALL_SPEED_X = 0.5
BALL_SPEED_Y = -0.5

play = True
while play:
    deltaTime = fps.tick(120)
    if Playing:
        for event in pygame.event.get():
            if event.type == QUIT:
                play = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bar_dl = -1 * deltaTime
                    bar_dr = 0
                elif event.key == pygame.K_RIGHT:
                    bar_dr = 1 * deltaTime
                    bar_dl = 0
                elif event.key == pygame.K_SPACE:
                    if Ready:
                        Ready = False
                        ball_dx = BALL_SPEED_X * deltaTime
                        ball_dy = BALL_SPEED_Y * deltaTime
            if event.type == KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    bar_dl = 0
                    bar_dr = 0

        bar_x_pos += bar_dl + bar_dr

        if bar_x_pos <= 0:
            bar_x_pos = 0
        if bar_x_pos + bar.width >= background.get_size()[0]:
            bar_x_pos = background.get_size()[0] - bar.width

        if Ready:
            for event in pygame.event.get():
                if event.type == QUIT:
                    play = False
            background.fill(white)
            ball_x = bar_x_pos + (bar.width // 2) - ball.width // 2
            ball_y = bar_y_pos - bar.height
            bar.draw(background, bar_x_pos, bar_y_pos)
            ball.draw(background, ball_x, ball_y)

            # 모든 벽돌을 그립니다.
            for brick in bricks:
                brick.draw(background)

        elif not Ready:
            for event in pygame.event.get():
                if event.type == QUIT:
                    play = False
            ball_x += ball_dx
            ball_y += ball_dy
            if ball_x <= 0:
                ball_x = 0
                ball_dx = -ball_dx
            if ball_x + ball.width >= background.get_size()[0]:
                ball_x = background.get_size()[0] - ball.width
                ball_dx = -ball_dx
            if ball_y <= 0:
                ball_y = 0
                ball_dy = -ball_dy

            if ball_y >= background.get_size()[1]:
                Playing = False
            bar_rect = bar.getrect()
            bar_rect.left = bar_x_pos
            bar_rect.top = bar_y_pos

            ball_rect = ball.getrect()
            ball_rect.left = ball_x
            ball_rect.top = ball_y

            if bar_rect.colliderect(ball_rect):
                # 바와 충돌 시, 수직 방향으로 튕겨나가도록 처리
                ball_dy = -ball_dy

            # 각각의 벽돌과 충돌을 감지합니다.
            for brick in bricks:
                if brick.check_collision(ball_rect):
                    brick_rect = brick.getrect()
                    overlap_x = max(0, min(ball_rect.right, brick_rect.right) - max(ball_rect.left, brick_rect.left))
                    overlap_y = max(0, min(ball_rect.bottom, brick_rect.bottom) - max(ball_rect.top, brick_rect.top))

                    if overlap_x > overlap_y:  # x 충돌이 y 충돌보다 큰 경우 (가로로 부딪힌 경우)
                        ball_dy = -ball_dy
                    else:  # y 충돌이 x 충돌보다 큰 경우 (세로로 부딪힌 경우)
                        ball_dx = -ball_dx

                    # 벽돌과 충돌했으므로 반복문을 빠져나옵니다.
                    break

            background.fill(white)
            bar.draw(background, bar_x_pos, bar_y_pos)
            ball.draw(background, ball_x, ball_y)

            # 모든 벽돌을 그립니다.
            for brick in bricks:
                brick.draw(background)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                Playing = True
                Ready = True
                bar_x_pos = background.get_size()[0] // 2 - 115 // 2
                bar_y_pos = background.get_size()[1] - 50
                bar_dl = 0
                bar_dr = 0

        background.fill(black)
        gameover = myFont.render("게임 오버", True, (255, 0, 0))
        restart = myFont.render("재시작 : R 키", True, (255, 0, 0))
        background.blit(gameover, (240, 100))
        background.blit(restart, (220, 200))

    pygame.display.update()

pygame.quit()
