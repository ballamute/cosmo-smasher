import pygame

import random
import time

import colors
import game
import values


class Player(game.GameObject):
    """
    Класс Player используется для создания игрока
    Наследуется от класса GameObject
    """
    def __init__(self):
        """
        Инициализация значений, связанных с игроком
        Принимает в аргументы объект класса Player, с которым и соотносится
        """
        game.GameObject.__init__(self)
        self.r = values.player_radius
        self.cross = pygame.image.load(values.cross_img)
        self.move_speed = values.player_move_speed
        self.time_for_kill = values.player_time_for_kill
        self.score = values.player_score
        self.armor = values.player_armor
        self.armor_got = values.player_armor_got
        self.shot_sound = pygame.mixer.Sound(values.shot_snd)
        self.dead_sound = pygame.mixer.Sound(values.dead_snd)

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

        # Проверка того, была ли клавиша движения или стрельбы, если да, то хотя бы одно значение массива keys равно 1
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN] or \
                keys[pygame.K_SPACE]:
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
        sound = f"music/en_down{random.randint(1, 4)}.wav"
        en_down_sound = pygame.mixer.Sound(sound)
        en_down_sound.set_volume(values.en_down_sound_volume)
        pygame.mixer.Sound.play(en_down_sound)

        # Увеличение очков
        self.score += bonus
        if self.score // values.plus_armor_border > self.armor_got:
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
        if self.armor < values.arm_lose_border or self.score < values.scr_lose_border:

            # Ограничение в 0 очков
            if self.score < 0:
                self.score = 0

            # Обработка звука и смена сцены на сцену проигранной игры
            pygame.mixer.Sound.play(self.dead_sound)
            time.sleep(0.5)
            pygame.mixer.music.load(values.game_over_snd)
            pygame.mixer.music.play()
            while True:
                clock.tick(values.FPS)
                display.fill(colors.BLACK)
                # Событие попадания в бедного мишку
                if values.shot in values.friends_images:
                    game.print_bear_shot_text(display, self.score)
                # Основное событие проигрыша
                else:
                    game.print_game_over_text(display, self.score)
                game.print_buttons(display)
                pygame.display.update()

                # Окрашивание кнопок, если на них наведен курсор
                pos = pygame.mouse.get_pos()
                game.color_buttons(pos)
                # Обработка событий
                events = pygame.event.get()
                game.end_events(events, pos)
                if values.again:
                    return

        # Проверка на победу
        if self.score >= values.win_border:

            # Обработка звука и смена сцены на сцену выигранной игры
            pygame.mixer.music.load(values.win_snd)
            pygame.mixer.music.play()
            while True:
                pygame.display.update()
                clock.tick(values.FPS)
                display.fill(colors.BLACK)
                game.print_text(display, 'YOU WIN', values.win_x, values.win_y, font_size=values.win_size,
                                font_color=values.win_color)
                game.print_buttons(display)
                pygame.display.update()

                # Окрашивание кнопок, если на них наведен курсор
                pos = pygame.mouse.get_pos()
                game.color_buttons(pos)
                # Обработка событий
                events = pygame.event.get()
                game.end_events(events, pos)
                if values.again:
                    return

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
