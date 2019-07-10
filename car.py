import pygame
from math import sin, cos, pi, radians



class Car(object):
    def __init__(self):
        """ Конструктор класса """
        self.x = 100                                        # координата x
        self.y = 100                                        # координата y
        self.angle = 0.0                                    # угол поворота
        self.V = 3                                          # скорость
        self.vel_x = self.V * cos(radians(self.angle))      # скорость по оси x
        self.vel_y = self.V * sin(radians(self.angle))      # скорость по оси y

        self.original_image = pygame.image.load('car.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        """ Обновление координат """
        self.vel_x = self.V * cos(radians(self.angle))
        self.vel_y = self.V * sin(radians(self.angle))
        self.x += self.vel_x
        self.y += self.vel_y
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.

    def handle_keys(self):
        """ Обработка нажатых клавиш """
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
        elif key[pygame.K_DOWN]:
            self.V = -3
        elif key[pygame.K_UP]:
            self.V = 3
        if key[pygame.K_RIGHT]:
            self.angle = (self.angle + 3) % 360
        elif key[pygame.K_LEFT]:
            self.angle = (self.angle - 3) % 360
            
    def draw(self, surface):
        """ Отрисовка машины """
        surface.blit(self.image, (self.x, self.y))



pygame.init()
screen = pygame.display.set_mode((720, 480))

car = Car()
clock = pygame.time.Clock()

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    car.handle_keys()
    pygame.time.delay(30)
    screen.fill((255,255,255))
    car.draw(screen)
    car.update()
    pygame.display.update()
    
    clock.tick(60)