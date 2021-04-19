import pygame

import random
import time

import game
import values


class Enemy(game.GameObject):
    """
    Класс Enemy используется для создания врага
    Наследуется от класса GameObject
    """

    def __init__(self):
        """
        Инициализация значений, связанных с врагом
        Принимает в аргументы объект класса Enemy, с которым и соотносится
        """
        game.GameObject.__init__(self)
        self.is_alive = values.is_alive
        self.image_name = values.def_en_image
        self.image = pygame.image.load(self.image_name)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.born_time = values.begin_of_life

    def rand_image(self):
        """
        Необходима для выбора случайного изображения врага
        """
        # 10 как правая граница randint задает шанс появления Enemy и шанс появления мишки
        if random.randint(0, 10) != 0:
            self.image_name = values.enemy_images[random.randint(0, len(values.enemy_images)) - 1]
        else:
            if values.started:
                self.image_name = values.friends_images[random.randint(0, len(values.friends_images)) - 1]
        self.image = pygame.image.load(self.image_name)

    def born(self):
        """
        Необходима для рождения нового врага, если старый был преодолен
        """
        if not values.started:
            self.born_time = time.time()
        if not self.is_alive:
            self.is_alive = True
            self.born_time = time.time()
            self.rand_image()
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.x = random.randint(0, values.dis_width - self.width)
            self.y = random.randint(0, values.dis_height - self.height)

    def draw(self, display):
        """
        Необходима для отрисовки Enemy на display
        :param display: Дисплей для вывода и отрисовки
        """
        display.blit(self.image, (self.x, self.y))
