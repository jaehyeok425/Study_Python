import pygame
import random

# 초기 설정
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("마블룰렛")
clock = pygame.time.Clock()

# 색상 및 폰트 설정
BLACK = (255, 255, 255)
WHITE = (0, 0, 0) 
FONT = pygame.font.Font(None, 36)

# 참가자 설정
participants = ["참가자1", "참가자2", "참가자3", "참가자4", "참가자5"]
positions = []

# 마블 위치 초기화
def init_positions():
    global positions
    positions = [300, 100]  # 마블 시작 위치 설정

# 애니메이션 함수
def draw_marble():
    pygame.draw.circle(screen, BLACK, (positions[0], positions[1]), 20)

# 결과를 출력하는 함수
def display_winner(winner):
    text = FONT.render(f"당첨: {winner}", True, BLACK)
    screen.blit(text, (200, 550))

# 메인 루프
running = True
init_positions()
winner = None
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not winner:
                # 무작위로 당첨자 선정
                winner = random.choice(participants)

    # 마블 애니메이션
    if not winner:
        positions[1] += 5  # 아래로 이동하는 효과
        if positions[1] > 500:
            init_positions()  # 맨 위로 초기화
    else:
        display_winner(winner)

    draw_marble()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
