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


def print_text(display, message, f_x, f_y, font_color=colors.WHITE, font_type=values.def_font, font_size=30):
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
    print_text(display, 'Back to main menu', values.back_x, values.back_y, font_size=values.back_size,
               font_color=values.back_color)


def end_events(events, pos):
    """
    Необходима для обработки событий на экранах Победы и поражения
    :param events: Массив событий клавиатуры и мыши
    :param pos: Координаты положения курсора мыши
    """
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                if values.try_again_tl[0] <= pos[0] <= values.try_again_br[0] and values.try_again_tl[1] <= pos[1] \
                        <= values.try_again_br[1]:
                    values.again = True
                    return
                elif values.exit_tl[0] <= pos[0] <= values.exit_br[0] and values.exit_tl[1] <= pos[1] \
                        <= values.exit_br[1]:
                    sys.exit()
                elif values.back_tl[0] <= pos[0] <= values.back_br[0] and values.back_tl[1] <= pos[1] \
                        <= values.back_br[1]:
                    values.game_is_on = True
                    values.again = True
                    return


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
    elif values.back_tl[0] <= pos[0] <= values.back_br[0] and values.back_tl[1] <= pos[1] <= values.back_br[1]:
        values.back_color = colors.GRAY
    else:
        values.try_again_color = colors.WHITE
        values.exit_color = colors.WHITE
        values.back_color = colors.WHITE


def print_bear_shot_text(display, score):
    """
    Необходима для печати текста экрана поражения при условии попадания в медведя
    :param display: Дисплей для вывода и отрисовки
    :param score: Количество очков игрока
    """
    print_text(display, 'How dare you shoot a harmless bear?', values.bear_ask_x, values.bear_ask_y,
               font_size=values.bear_ask_size, font_color=values.bear_ask_color)
    print_text(display, 'YOUR SCORE IS: ' + str(score), values.bear_score_x, values.bear_score_y,
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

    for event in pygame.event.get():
        # Обработка результата нажатия клавиши ESCAPE и комбинации Alt + F4
        if event.type == pygame.QUIT:
            sys.exit()
        elif values.control == values.key_control:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    process_shot(pl, en)
        elif values.control == values.mouse_control:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == values.LMB_key:
                    process_shot(pl, en)


def process_shot(pl, en):
    """
    Необходима для обработки выстрела, его визуализации, вывода аудио и для начисления очков в зависимости от меткости
    попадания
    :param pl: Объект класса Player
    :param en: Объект класса Enemy
    """
    values.line_color = values.line_shot_color
    values.started = True
    pygame.mixer.Sound.play(pl.shot_sound)

    # Задание места, попав в которое выстрел будет защитан как меткий
    nice_shot_tl = (en.x + int(values.ns_coefficient * en.width), en.y + int(values.ns_coefficient * en.height))
    nice_shot_br = (en.x + int((1 - values.ns_coefficient) * en.width), en.y +
                    int((1 - values.ns_coefficient) * en.height))
    if nice_shot_tl[0] <= pl.x <= nice_shot_br[0] and nice_shot_tl[1] <= pl.y <= nice_shot_br[1]:
        pl.shot_count(values.nice_shot_bonus, en)
        values.nice_shot = True
        values.nice_shot_start = time.time()
    # Задание места, попав в которое выстрел будет защитан как удачный
    elif en.x <= pl.x <= en.x + en.width and en.y <= pl.y <= en.y + en.height:
        pl.shot_count(values.shot_bonus, en)
    # Задание результата промаха
    else:
        pl.score -= values.miss_penalty


def show_menu(display):
    """
    Необходима для вывода главного меню и обработки нажатия кнопок на нем
    :param display: Дисплей для вывода и отрисовки
    """
    clock = pygame.time.Clock()
    menu_bg = Background(values.menu_bg_img, [0, 0])
    while True:
        display.blit(menu_bg.image, menu_bg.rect)
        clock.tick(values.FPS)
        print_text(display, 'COSMO SMASHER', values.caption_x, values.caption_y, font_size=values.caption_size,
                   font_color=values.caption_color)
        print_menu_buttons(display)
        pos = pygame.mouse.get_pos()
        color_menu_buttons(pos)
        for event in pygame.event.get():
            # Обработка результата нажатия клавиши ESCAPE и комбинации Alt + F4
            if event.type == pygame.QUIT:
                sys.exit()
            # Обработка результата нажатия кнопок в главном меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == values.LMB_key:
                    if values.play_tl[0] <= pos[0] <= values.play_br[0] \
                            and values.play_tl[1] <= pos[1] <= values.play_br[1]:
                        return
                    elif values.exit_menu_tl[0] <= pos[0] <= values.exit_menu_br[0] \
                            and values.exit_menu_tl[1] <= pos[1] <= values.exit_menu_br[1]:
                        sys.exit()
                    elif values.key_menu_tl[0] <= pos[0] <= values.key_menu_br[0] \
                            and values.key_menu_tl[1] <= pos[1] <= values.key_menu_br[1]:
                        values.control = values.key_control
                    elif values.mouse_menu_tl[0] <= pos[0] <= values.mouse_menu_br[0] \
                            and values.mouse_menu_tl[1] <= pos[1] <= values.mouse_menu_br[1]:
                        values.control = values.mouse_control
                    elif values.easy_tl[0] <= pos[0] <= values.easy_br[0] \
                            and values.easy_tl[1] <= pos[1] <= values.easy_br[1]:
                        values.difficulty = values.easy_diff
                        if values.control == values.key_control:
                            values.player_time_for_kill = values.easy_key_kill_time
                        elif values.control == values.mouse_control:
                            values.player_time_for_kill = values.easy_mouse_kill_time
                    elif values.medium_tl[0] <= pos[0] <= values.medium_br[0] \
                            and values.medium_tl[1] <= pos[1] <= values.medium_br[1]:
                        values.difficulty = values.medium_diff
                        if values.control == values.key_control:
                            values.player_time_for_kill = values.medium_key_kill_time
                        elif values.control == values.mouse_control:
                            values.player_time_for_kill = values.medium_mouse_kill_time
                    elif values.hard_tl[0] <= pos[0] <= values.hard_br[0] \
                            and values.hard_tl[1] <= pos[1] <= values.hard_br[1]:
                        values.difficulty = values.hard_diff
                        if values.control == values.key_control:
                            values.player_time_for_kill = values.hard_key_kill_time
                        elif values.control == values.mouse_control:
                            values.player_time_for_kill = values.hard_mouse_kill_time
        pygame.display.update()


def print_menu_buttons(display):
    """
    Необходима для вывода текста кнопок и просто текста с заданными параметрами
    :param display: Дисплей для вывода и отрисовки
    """
    print_text(display, 'PLAY', values.play_x, values.play_y, font_size=values.play_size,
               font_color=values.play_color)
    print_text(display, 'CONTROL', values.control_x, values.control_y, font_size=values.control_size,
               font_color=values.control_color)
    print_text(display, 'Mouse', values.mouse_menu_x, values.mouse_menu_y, font_size=values.mouse_menu_size,
               font_color=values.mouse_menu_color)
    print_text(display, 'Keyboard', values.key_menu_x, values.key_menu_y, font_size=values.key_menu_size,
               font_color=values.key_menu_color)
    print_text(display, 'Exit', values.exit_menu_x, values.exit_menu_y, font_size=values.exit_menu_size,
               font_color=values.exit_menu_color)
    print_text(display, 'DIFFICULTY', values.difficulty_x, values.difficulty_y, font_size=values.difficulty_size,
               font_color=values.difficulty_color)
    print_text(display, 'Easy', values.easy_x, values.easy_y, font_size=values.easy_size, font_color=values.easy_color)
    print_text(display, 'Medium', values.medium_x, values.medium_y, font_size=values.medium_size,
               font_color=values.medium_color)
    print_text(display, 'Hard', values.hard_x, values.hard_y, font_size=values.hard_size, font_color=values.hard_color)


def color_menu_buttons(pos):
    """
    Необходима для контроля цвета текста кнопок главного меню в зависимости от положения курсора пользователя
    :param pos: Координаты положения курсора мыши
    """
    # Контроль цвета нажатых кнопок выбора управления
    if values.control == values.key_control:
        values.key_menu_color = colors.GRAY
        values.mouse_menu_color = colors.WHITE
    else:
        values.key_menu_color = colors.WHITE
        values.mouse_menu_color = colors.GRAY

    # Контроль цвета нажатых кнопок выбора сложности
    if values.difficulty == values.easy_diff:
        values.easy_color = colors.GRAY
        values.medium_color = colors.WHITE
        values.hard_color = colors.WHITE
    elif values.difficulty == values.medium_diff:
        values.easy_color = colors.WHITE
        values.medium_color = colors.GRAY
        values.hard_color = colors.WHITE
    elif values.difficulty == values.hard_diff:
        values.easy_color = colors.WHITE
        values.medium_color = colors.WHITE
        values.hard_color = colors.GRAY

    # Контроль цвета кнопок при наведении на них курсора
    if values.play_tl[0] <= pos[0] <= values.play_br[0] \
            and values.play_tl[1] <= pos[1] <= values.play_br[1]:
        values.play_color = colors.DARK_GREEN
    elif values.exit_menu_tl[0] <= pos[0] <= values.exit_menu_br[0] \
            and values.exit_menu_tl[1] <= pos[1] <= values.exit_menu_br[1]:
        values.exit_menu_color = colors.MAROON
    else:
        values.play_color = colors.GREEN
        values.exit_menu_color = colors.BRICK_RED

    if values.key_menu_tl[0] <= pos[0] <= values.key_menu_br[0] \
            and values.key_menu_tl[1] <= pos[1] <= values.key_menu_br[1]:
        values.key_menu_color = colors.GRAY
    elif values.mouse_menu_tl[0] <= pos[0] <= values.mouse_menu_br[0] \
            and values.mouse_menu_tl[1] <= pos[1] <= values.mouse_menu_br[1]:
        values.mouse_menu_color = colors.GRAY

    if values.easy_tl[0] <= pos[0] <= values.easy_br[0] \
            and values.easy_tl[1] <= pos[1] <= values.easy_br[1]:
        values.easy_color = colors.GRAY
    elif values.medium_tl[0] <= pos[0] <= values.medium_br[0] \
            and values.medium_tl[1] <= pos[1] <= values.medium_br[1]:
        values.medium_color = colors.GRAY
    elif values.hard_tl[0] <= pos[0] <= values.hard_br[0] \
            and values.hard_tl[1] <= pos[1] <= values.hard_br[1]:
        values.hard_color = colors.GRAY


def set_difficulty():
    """
    Необходима для контроля времени для убийства в зависимости от выбранного в меню управления и сложности
    """
    if values.control == values.mouse_control:
        if values.difficulty == values.easy_diff:
            values.player_time_for_kill = values.easy_mouse_kill_time
        elif values.difficulty == values.medium_diff:
            values.player_time_for_kill = values.medium_mouse_kill_time
        else:
            values.player_time_for_kill = values.hard_mouse_kill_time
    elif values.control == values.key_control:
        if values.difficulty == values.easy_diff:
            values.player_time_for_kill = values.easy_key_kill_time
        elif values.difficulty == values.medium_diff:
            values.player_time_for_kill = values.medium_key_kill_time
        else:
            values.player_time_for_kill = values.hard_key_kill_time
