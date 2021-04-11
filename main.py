import pygame

import colors
import enemy
import game
import player
import values


def main():
    # Инициализация pygame и mixer
    pygame.init()
    game.init_snd()

    clock = pygame.time.Clock()
    # Задание дисплея
    display = pygame.display.set_mode((values.dis_width, values.dis_height))
    pygame.display.set_caption(values.game_name)

    # Задание фона игры
    bg = game.Background(values.bg_img, [0, 0])

    # Инициализация переменных
    game.init_game()

    # Создание игрока и врага
    pl = player.Player()
    en = enemy.Enemy()

    # Основной цикл игры
    while True:
        # Отслеживание FPS
        clock.tick(values.FPS)

        # Вывод фона игры
        display.blit(bg.image, bg.rect)

        # Отслеживание движений и действий игрока
        pl.track_move(pygame.key.get_pressed())

        # Рождение нового врага, если старый был преодолен
        en.born()

        # Прорисовка врага
        en.draw(display)

        # Прорисовка интерфейса игры: очков, защиты, оставшегося для убийства времени
        game.print_interface(display, pl, en)

        # Отслеживание событий клавиатуры
        game.track_event(pl, en)

        # Похвала для игрока за меткий выстрел
        game.praise_player(display)

        # Прорисовка игрока
        pl.draw(display)

        # Проверка счета игрока для определения победы и поражения
        pl.score_check(display)

        # Обработка ситуации, в которой игрок оказывается атакованным
        pl.if_attacked(display, en)

        # Отрисовка части прицела игрока
        values.line_color = colors.RED

        # Обновление экрана
        pygame.display.update()


# Запуск
main()
