import pygame
from math import sin, cos, pi, radians



class Car(object):
    def __init__(self):
        """ Конструктор класса """
        self.original_image = pygame.image.load('car.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.w = 50
        self.h = 30
        self.x = 100                                        # координата x
        self.y = 100                                        # координата y
        self.angle = 0.0                                    # угол поворота
        self.V = 3                                          # скорость
        self.vel_x = self.V * cos(radians(self.angle))      # скорость по оси x
        self.vel_y = self.V * sin(radians(self.angle))      # скорость по оси y

        self.center_x = self.x + self.image.get_rect()[2] / 2 #* cos(radians(self.angle))
        self.center_y = self.y + self.image.get_rect()[3] / 2 #* sin(radians(self.angle))
        #print(self.image.get_rect())
        print(self.rect)
        self.rect.center = (self.x, self.y)

    def update(self):
        """ Обновление координат """
        self.vel_x = self.V * cos(radians(self.angle))
        self.vel_y = self.V * sin(radians(self.angle))
        
        # if self.V > 0:
        #     self.x += self.vel_x
        #     self.y += self.vel_y
        
        self.x += self.vel_x
        self.y += self.vel_y

        self.center_x = self.x + self.image.get_rect()[2] / 2 #* cos(radians(self.angle))
        self.center_y = self.y + self.image.get_rect()[3] / 2 #* sin(radians(self.angle))
        print(self.image.get_rect())

        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)

    def handle_keys(self):
        """ Обработка нажатых клавиш """
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
        elif key[pygame.K_DOWN] or key[pygame.K_SPACE]:
            self.V = 0
        elif key[pygame.K_UP]:
            self.V += 3
        if key[pygame.K_RIGHT]:
            self.angle = (self.angle + 10) % 360
        elif key[pygame.K_LEFT]:
            self.angle = (self.angle - 10) % 360
            
    def draw(self, surface):
        """ Отрисовка машины """
        surface.blit(self.image, (self.x, self.y))