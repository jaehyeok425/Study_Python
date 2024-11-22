import pygame
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (250, 0, 0)
BLUE = (0, 0, 255)

SCORE_FILE = "ranking.txt"

class Car:
    image_car = ['C:/python/CarSorc1/RacingCar01.png','C:/python/CarSorc1/RacingCar02.png','C:/python/CarSorc1/RacingCar03.png','C:/python/CarSorc1/RacingCar04.png',
                 'C:/python/CarSorc1/RacingCar05.png','C:/python/CarSorc1/RacingCar06.png','C:/python/CarSorc1/RacingCar07.png','C:/python/CarSorc1/RacingCar08.png',
                 'C:/python/CarSorc1/RacingCar09.png','C:/python/CarSorc1/RacingCar10.png','C:/python/CarSorc1/RacingCar11.png','C:/python/CarSorc1/RacingCar12.png',
                 'C:/python/CarSorc1/RacingCar13.png','C:/python/CarSorc1/RacingCar14.png','C:/python/CarSorc1/RacingCar15.png','C:/python/CarSorc1/RacingCar16.png',
                 'C:/python/CarSorc1/RacingCar17.png','C:/python/CarSorc1/RacingCar18.png','C:/python/CarSorc1/RacingCar19.png','C:/python/CarSorc1/RacingCar20.png']
    
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(random.choice(self.image_car))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_boundaries(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.width
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height

    def check_crash(self, car):
        return (
            self.x + self.width > car.x and self.x < car.x + car.width and
            self.y < car.y + car.height and self.y + self.height > car.y
        )

def save_score(name, score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{name},{score}\n")

def load_ranking():
    ranking = []
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                ranking.append((name, int(score)))
    except FileNotFoundError:
        pass
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking[:7]

def display_ranking(screen):
    ranking = load_ranking()
    font = pygame.font.SysFont("Arial", 25, True)
    title_font = pygame.font.SysFont("Arial", 35, True)
    title_text = title_font.render("Top 7 Rankings", True, BLUE)
    screen.blit(title_text, (WINDOW_WIDTH / 2 - title_text.get_width() / 2, 100))
    
    y_offset = 180
    for i, (name, score) in enumerate(ranking, start=1):
        rank_text = font.render(f"{i}. {name}: {score}", True, BLACK)
        screen.blit(rank_text, (WINDOW_WIDTH / 2 - rank_text.get_width() / 2, y_offset))
        y_offset += 40
    pygame.display.flip()

def draw_score(screen, score):
    font_30 = pygame.font.SysFont("Arial", 30, True)
    txt_score = font_30.render(f"Score: {score}", True, BLACK)
    screen.blit(txt_score, [15, 15])

def get_user_name_with_ranking(screen):
    font = pygame.font.SysFont("Arial", 30, True)
    user_name = ""
    input_active = True

    while input_active:
        screen.fill(GRAY)

        
        prompt = font.render("Enter Your Name: " + user_name, True, BLACK)
        screen.blit(prompt, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2))

        
        display_ranking(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode

    return user_name.strip() or "Player"

def draw_lane_lines(screen, lanes):
    for lane in lanes:
        pygame.draw.rect(screen, WHITE, [lane[0], lane[1], lane[2], lane[3]])

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("PyCar : Racing Car Game")
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load('C:/python/CarSorc1/race.wav')
    sound_crash = pygame.mixer.Sound('C:/python/CarSorc1/crash.wav')
    sound_engine = pygame.mixer.Sound('C:/python/CarSorc1/engine.wav')
    
    
    sound_engine.play()


    pygame.mixer.music.play(-1)


    game_on = True

    while game_on:
        name = get_user_name_with_ranking(screen)
        score = 0
        crash = False

       
        player = Car(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 150, 0, 0)
        player.load_image()
        
        
        cars = []
        for _ in range(3):
            x = random.randrange(0, WINDOW_WIDTH - 55)
            car = Car(x, random.randrange(-150, -50), 0, random.randint(5, 10))
            car.load_image()
            cars.append(car)

        
        lanes = []
        lane_width = 10
        lane_height = 80
        lane_margin = 20
        lane_x = (WINDOW_WIDTH - lane_width) / 2
        lane_y = -10
        for i in range(10):
            lanes.append([lane_x, lane_y + (lane_height + lane_margin) * i, lane_width, lane_height])

        while not crash:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False
                    crash = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player.dx = 4
                    elif event.key == pygame.K_LEFT:
                        player.dx = -4
                    elif event.key == pygame.K_UP:
                        player.dy = -4
                    elif event.key == pygame.K_DOWN:
                        player.dy = 4
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        player.dx = 0
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        player.dy = 0

            screen.fill(GRAY)

            
            draw_lane_lines(screen, lanes)

            
            for lane in lanes:
                lane[1] += 5  
                if lane[1] > WINDOW_HEIGHT:
                    lane[1] = -lane_height - lane_margin

            player.draw_image()
            player.move()
            player.check_boundaries()

            for car in cars:
                car.draw_image()
                car.y += car.dy
                if car.y > WINDOW_HEIGHT:
                    score += 10
                    car.y = random.randrange(-150, -50)
                    car.x = random.randrange(0, WINDOW_WIDTH - car.width)
                    car.dy = random.randint(5, 10)
                    car.load_image()

            for car in cars:
                if player.check_crash(car):
                    crash = True
                    pygame.mixer.music.stop()
                    sound_crash.play()
                    save_score(name, score)
                    pygame.mouse.set_visible(True)
                    sleep(2)
                    break

            draw_score(screen, score)
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
