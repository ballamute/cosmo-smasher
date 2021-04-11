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
    """
    Необходима для инициализации переменных и обновления их пре рестарте игры
    """
    values.player_score = 0
    values.player_armor = 0
    values.player_armor_got = 0

    values.is_alive = False

    values.begin_of_life = 0

    values.started = False
    values.again = False

    values.nice_shot = False
    values.nice_shot_start = 0
    values.shot = " "


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


def print_buttons(display):
    """
    Необходима для вывода текста кнопок Exit и Try again с заданными параметрами
    :param display: Дисплей для вывода и отрисовки
    """
    print_text(display, 'Try again', values.try_again_x, values.try_again_y, font_size=values.try_again_size,
               font_color=values.try_again_color)
    print_text(display, 'Exit', values.exit_x, values.exit_y, font_size=values.exit_size,
               font_color=values.exit_color)


def end_events(events, pos):
    """
    Необходима для обработки событий на экранах Победы и поражения
    :param events: Массив событий клавиатуры и мыши
    :param pos: Координаты положения курсора мыши
    """
    for i in events:
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                if values.try_again_tl[0] <= pos[0] <= values.try_again_br[0] and values.try_again_tl[1] <= pos[1] \
                        <= values.try_again_br[1]:
                    values.again = True
                    return
                elif values.exit_tl[0] <= pos[0] <= values.exit_br[0] and values.exit_tl[1] <= pos[1] \
                        <= values.exit_br[1]:
                    sys.exit()


def color_buttons(pos):
    """
    Необходима для контроля цвета текста кнопок Try again и Exit в зависимости
    от положения курсора пользователя
    :param pos: Координаты положения курсора мыши
    """
    if values.try_again_tl[0] <= pos[0] <= values.try_again_br[0] and values.try_again_tl[1] <= pos[1] <= \
            values.try_again_br[1]:
        values.try_again_color = colors.GRAY
    elif values.exit_tl[0] <= pos[0] <= values.exit_br[0] and values.exit_tl[1] <= \
            pos[1] <= values.exit_br[1]:
        values.exit_color = colors.GRAY
    else:
        values.try_again_color = colors.WHITE
        values.exit_color = colors.WHITE


def print_bear_shot_text(display, score):
    """
    Необходима для печати текста экрана поражения при условии попадания в медведя
    :param display: Дисплей для вывода и отрисовки
    :param score: Количество очков игрока
    """
    print_text(display, 'How dare you shoot a harmless bear?', values.bear_ask_x, values.bear_ask_y,
               font_size=values.bear_ask_size, font_color=values.bear_ask_color)
    print_text(display, 'YOUR FUCKING SCORE IS: ' + str(score), values.bear_score_x, values.bear_score_y,
               font_size=values.bear_score_size, font_color=values.bear_score_color)


def print_game_over_text(display, score):
    """
    Необходима для печати текста экрана поражения
    :param display: Дисплей для вывода и отрисовки
    :param score: Количество очков игрока
    """
    print_text(display, 'GAME OVER', values.over_x, values.over_y, font_size=values.over_size,
               font_color=values.over_color)
    print_text(display, 'YOUR SCORE IS: ' + str(score), values.ov_score_x, values.ov_score_y,
               font_size=values.ov_score_size, font_color=values.ov_score_color)


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
