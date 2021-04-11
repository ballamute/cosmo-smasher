import pygame
import sys

import random
import time

import colors
import values


class GameObject:
    """
    Класс GameObject - родительский класс для Enemy и Player
    Отдает им координаты
    """
    def __init__(self):
        self.x = values.object_pos_x
        self.y = values.object_pos_y


class Background(pygame.sprite.Sprite):
    """
    Класс Background описывает задний фон для игры
    Является дочерним для pygame.sprite.Sprite
    """
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def init_game():
    values.player_score = 0
    values.player_armor = 0
    values.player_armor_got = 0

    values.is_alive = False

    values.begin_of_life = 0

    values.started = False

    values.nice_shot = False
    values.nice_shot_start = 0


def fix(num, digits=0):
    """
    Необходима для фиксации количества цифр после запятой у десятичных чисел
    :param num: Число для проведения fix`а
    :param digits: Необходимое количество знаков после запятой
    :return: Число с необходимым количеством знаков после запятой
    """
    return f"{num:.{digits}f}"


def print_text(display, message, f_x, f_y, font_color=colors.WHITE, font_type='fonts/rostov.ttf', font_size=30):
    """
    Необходима для вывода текста с заданными параметрами
    :param display: Дисплей для вывода и отрисовки
    :param message: Сообщение подаваемое на печать
    :param f_x: Левая верхняя координата по иксу
    :param f_y: Левая верхняя координата по игреку
    :param font_color: Цвет текста
    :param font_type: Шрифт текста
    :param font_size: Размер текста
    """
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (f_x, f_y))


def praise_player(display):
    """
    Необходима для похвалы игрока в случае меткого выстрела
    :param display: Дисплей для вывода и прорисовки
    """
    if values.nice_shot:
        print_text(display, values.praise_chs, values.ns_x, values.ns_y, font_color=values.ns_color)
        if time.time() - values.nice_shot_start > values.ns_time:
            values.nice_shot = False
    else:
        values.praise_chs = values.praises[random.randint(0, len(values.praises)) - 1]


def init_snd():
    """
    Необходима для инициализации звука в игре
    """
    pygame.mixer.pre_init(values.mixer_frequency, values.mixer_size, values.mixer_channels, values.mixer_buffer)
    pygame.mixer.init()
    pygame.mixer.music.load(values.back_music)
    pygame.mixer.music.play(-1)


def print_interface(display, pl, en):
    """
    Необходима для вывода интерфейса с параметрами Player на display
    :param display: Дисплей для вывода и отрисовки
    :param pl: Объект класса Player
    :param en: Объект класса Enemy
    """
    print_text(display, "SCORE: " + str(pl.score), values.score_x, values.score_y, font_color=values.score_color)
    print_text(display, "ARMOR: " + str(pl.armor), values.armor_x, values.armor_y, font_color=values.armor_color)
    print_text(display, "TIME FOR KILL: " + fix(pl.time_for_kill - (time.time() - en.born_time), 2),
               values.t_for_k_x, values.t_for_k_y, font_color=values.t_for_k_color)


def track_event(pl, en):
    """
    Необходима для отслеживания событий клавиатуры
    :param pl: Объект класса Player
    :param en: Объект класса Enemy
    """
    for i in pygame.event.get():
        # Обработка результата нажатия клавиши ESCAPE и комбинации Alt + F4
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                # Обработка результата нажатия клавиши SPACE
                values.line_color = values.line_shot_color
                values.started = True
                pygame.mixer.Sound.play(pl.shot_sound)
                # Задание места, попав в которое выстрел будет защитан как меткий
                if en.x + en.width // 3 <= pl.x <= en.x + 2 * en.width // 3 and en.y + en.height // 3 <= \
                        pl.y <= en.y + 2 * en.height // 3:
                    pl.shot_count(values.nice_shot_bonus, en)
                    values.nice_shot = True
                    values.nice_shot_start = time.time()
                # Задание места, попав в которое выстрел будет защитан как удачный
                elif en.x <= pl.x <= en.x + en.width and en.y <= pl.y <= en.y + en.height:
                    pl.shot_count(values.shot_bonus, en)
                # Задание результата промаха
                else:
                    pl.score -= values.miss_penalty
