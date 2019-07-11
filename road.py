import pygame


class Road:
    def __init__(self):
        """ Констурктор класса """
        self.l = [(80, 50),
                  (80, 100),
                  (110, 150),
                  (130, 180),
                  (180, 230),
                  (230, 380)]

        self.r = [(150, 50),
                  (180, 100),
                  (200, 150), 
                  (230, 280),
                  (380, 330),
                  (450, 480)]
        self.lineColor = (128, 128, 128)


    def draw(self, screen):
        """ Отрисовка обеих сторон дорог """
        # Рисуем левую обочину
        for i in range(len(self.l) - 1):
            pygame.draw.line(screen, self.lineColor, self.l[i], self.l[i+1])
            pygame.draw.circle(screen, (50,50,50), self.l[i], 3, 1)
        # Рисуем правую обочину
        for i in range(len(self.r) - 1):
            pygame.draw.line(screen, self.lineColor, self.r[i], self.r[i+1])
            pygame.draw.circle(screen, (50,50,50), self.r[i], 3, 1)

