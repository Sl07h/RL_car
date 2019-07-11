from car import *
from road import *
from math import sqrt

class Game:
    def __init__(self):
        """ Констуктор класса """
        pygame.init()
        self.screen = pygame.display.set_mode((720, 480))
        self.car = Car()
        self.road = Road()
        self.clock = pygame.time.Clock()
        self.running = True

    def gameLoop(self):
        """ Основной цикл событий """
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

            self.car.handle_keys()
            pygame.time.delay(100)
            self.screen.fill((255,255,255))
            self.car.draw(self.screen)
            self.road.draw(self.screen)
            self.car.update()

            if self.checkCollition() == True:
                self.running = False

            pygame.display.update()
            self.clock.tick(60)

    def calcDistance(self, p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def checkCollition(self):
        """ Проверяем на вылет с трассы """
        
        # Проверяем столкновение с левой обочиной
        nearestPointLeft = self.road.l[0]
        nearestPointLeftIndex = 0
        nearestDistanceLeft = self.calcDistance(nearestPointLeft, (self.car.x, self.car.y))
        for i in range(1, len(self.road.l)):
            if self.calcDistance(self.road.l[i], (self.car.x, self.car.y)) < nearestDistanceLeft:
                nearestPointLeft = self.road.l[i]
                nearestPointLeftIndex = i
                nearestDistanceLeft = self.calcDistance(nearestPointLeft, (self.car.x, self.car.y))
        pygame.draw.circle(self.screen, (0,0,0), nearestPointLeft, 10, 2)
        # Ищем точку вторую по удалённости
        if self.calcDistance(self.road.l[nearestPointLeftIndex-1], (self.car.x, self.car.y)) < self.calcDistance(self.road.l[nearestPointLeftIndex+1], (self.car.x, self.car.y)):
            pygame.draw.circle(self.screen, (0,0,0), self.road.l[nearestPointLeftIndex-1], 10, 2)
        else:
            pygame.draw.circle(self.screen, (0,0,0), self.road.l[nearestPointLeftIndex+1], 10, 2)
        

        # Проверяем столкновение с правой обочиной
        nearestPointRight = self.road.r[0]
        nearestPointRightIndex = 0
        nearestDistanceRight = self.calcDistance(nearestPointRight, (self.car.x, self.car.y))
        for i in range(1, len(self.road.r)):
            if self.calcDistance(self.road.r[i], (self.car.x, self.car.y)) < nearestDistanceRight:
                nearestPointRight = self.road.r[i]
                nearestPointRightIndex = i
                nearestDistanceRight = self.calcDistance(nearestPointRight, (self.car.x, self.car.y))

        pygame.draw.circle(self.screen, (0,0,0), nearestPointRight, 10, 2)
        # Ищем точку вторую по удалённости
        if self.calcDistance(self.road.r[nearestPointRightIndex-1], (self.car.x, self.car.y)) < self.calcDistance(self.road.r[nearestPointRightIndex+1], (self.car.x, self.car.y)):
            pygame.draw.circle(self.screen, (0,0,0), self.road.r[nearestPointRightIndex-1], 10, 2)
        else:
            pygame.draw.circle(self.screen, (0,0,0), self.road.r[nearestPointRightIndex+1], 10, 2)
        

        pygame.draw.circle(self.screen, (0,0,0), (int(self.car.x), int(self.car.y)), 5, 2)
        pygame.draw.circle(self.screen, (0,0,0), (int(self.car.center_x), int(self.car.center_y)), 10, 2)

        return False


game = Game()
game.gameLoop()