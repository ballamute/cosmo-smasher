import pygame
import sys

import random
import time

import colors
import game
import values


class Player(game.GameObject):
    """
    Класс Player используется для создания игрока
    Наследуется от класса GameObject
    В классе Player определены функции:
    __init__()
    draw(display)
    track_move(keys)
    shot_count(bonus, en)
    score_check(display, en)
    if_attacked(display, en)
    """
    def __init__(self):
        """
        Инициализация значений, связанных с игроком
        Принимает в аргументы объект класса Player, с которым и соотносится
        """
        game.GameObject.__init__(self)
        self.r = values.player_radius
        self.cross = pygame.image.load("pics/cross1.png")
        self.move_speed = values.player_move_speed
        self.time_for_kill = values.player_time_for_kill
        self.score = values.player_score
        self.armor = values.player_armor
        self.armor_got = values.player_armor_got
        self.shot_sound = pygame.mixer.Sound("music/laser.wav")
        self.dead_sound = pygame.mixer.Sound("music/dead.wav")

    def draw(self, display):
        """
        Необходима для отрисовки Player на display (Отрисовки прицела и прицельных линий)
        :param display: Дисплей для вывода и отрисовки
        """
        pygame.draw.line(display, values.line_color, [0, self.y], [values.dis_width, self.y], 2)
        pygame.draw.line(display, values.line_color, [self.x, 0], [self.x, values.dis_height], 2)
        display.blit(self.cross, (self.x - self.cross.get_width() // 2, self.y - self.cross.get_height() // 2))

    def track_move(self, keys):
        """
        Необходима для отслеживания движения Player
        :param keys: Массив со значениями, равными 1, если кнопка по соответствующему индексу нажата,
        и 0 в обратном случае
        """

        # Проверка того, была ли нажата какая-либо клавиша, если да, то хотя бы одно значение массива keys равно 1
        if 1 in keys:
            values.started = True

        # Отслеживание нажатых клавиш стрелок и положения прицела относительно границ экрана и изменение положения
        # прицела
        if keys[pygame.K_LEFT] and self.x - self.r != 0:
            self.x -= self.move_speed
        elif keys[pygame.K_RIGHT] and self.x + self.r != values.dis_width:
            self.x += self.move_speed
        if keys[pygame.K_UP] and self.y - self.r != 0:
            self.y -= self.move_speed
        elif keys[pygame.K_DOWN] and self.y + self.r != values.dis_height:
            self.y += self.move_speed
        if keys[pygame.K_SPACE]:
            values.line_color = colors.YELLOW

    def shot_count(self, bonus, en):
        """
        Необходима для регистрации попадания по Enemy и начисления ему за это bonus
        :param bonus: Количество очков начисляемых за попадание
        :param en: Объект класса Enemy
        """

        # Наказание для игрока, безжалостно застрелившего бедного мишку(. Он проигрывает с параметром очков равным -1
        if en.image_name in values.friends_images:
            values.shot = en.image_name
            self.score = -1
            return

        # Обработка звука побежденного врага
        sound = "music/en_down{}.wav".format(random.randint(1, 4))
        en_down_sound = pygame.mixer.Sound(sound)
        en_down_sound.set_volume(0.2)
        pygame.mixer.Sound.play(en_down_sound)

        # Увеличение очков
        self.score += bonus
        if self.score // 10 > self.armor_got:
            self.armor += 1
            self.armor_got += 1
        en.is_alive = False

    def score_check(self, display):
        """
        Необходима для проверки счета Player и вывода результата этой проверки на display при определенных условиях
        :param display: Дисплей для вывода и отрисовки
        """
        clock = pygame.time.Clock()

        # Проверка на проигрыш
        if self.armor < 0 or self.score < 0:

            # Ограничение в 0 очков
            if self.score < 0:
                self.score = 0

            # Обработка звука и смена сцены на сцену проигранной игры
            pygame.mixer.Sound.play(self.dead_sound)
            time.sleep(0.5)
            pygame.mixer.music.load("music/game_over.wav")
            pygame.mixer.music.play()
            while True:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                clock.tick(values.FPS)
                display.fill(colors.BLACK)

                # Событие попадания в бедного мишку
                if values.shot in values.friends_images:
                    game.print_text(display, 'How dare you shoot a harmless bear?', values.dis_width // 2 - 330,
                                    values.dis_height // 2 - 50, font_size=40, font_color=colors.RED)
                    game.print_text(display, 'YOUR FUCKING SCORE IS: ' + str(self.score), values.dis_width // 2 - 170,
                                    values.dis_height // 2 + 25, font_size=30, font_color=colors.WHITE)
                # Основное событие проигрыша
                else:
                    game.print_text(display, 'GAME OVER', values.dis_width // 2 - 150, values.dis_height // 2 - 50,
                                    font_size=60, font_color=colors.RED)
                    game.print_text(display, 'YOUR SCORE IS: ' + str(self.score), values.dis_width // 2 - 125,
                                    values.dis_height // 2 + 25, font_size=30, font_color=colors.WHITE)
                pygame.display.update()

        # Проверка на победу
        if self.score >= 25:

            # Обработка звука и смена сцены на сцену выигранной игры
            pygame.mixer.music.load("music/you_win.wav")
            pygame.mixer.music.play()
            while True:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                pygame.display.update()
                clock.tick(values.FPS)
                display.fill(colors.BLACK)
                game.print_text(display, 'YOU WIN', values.dis_width // 2 - 140, values.dis_height // 2 - 50,
                                font_size=60, font_color=colors.GREEN)

    def if_attacked(self, display, en):
        """
        Необходима для отслеживания события, при котором Player атакован
        :param display: Дисплей для вывода и отрисовки
        :param en: Объект класса Enemy
        """

        # Проверка времени со дня рождения Enemy, если прошло уже time_for_kill, игрока атакуют и он теряет очко брони
        if time.time() - en.born_time > self.time_for_kill and values.started:
            # Если врагом оказался милый мишка, то по прошествии time_for_kill секунд, мишка, скажем так, "уходит"...,
            # что безболезненно для Player
            if en.image_name in values.friends_images:
                en.is_alive = False
                return
            display.fill(colors.RED)
            pygame.display.update()
            time.sleep(0.1)
            self.armor -= 1
            en.is_alive = False
