import pygame

import colors
import enemy
import game
import player
import values


# Инициализация pygame
pygame.init()
clock = pygame.time.Clock()

# Задание дисплея
display = pygame.display.set_mode((values.dis_width, values.dis_height))
pygame.display.set_caption(values.game_name)

# Задание фона игры
game_bg = game.Background(values.game_bg_img, [0, 0])


def main():
    # Инициализация переменных
    game.init_game()

    # Инициализация mixer
    game.init_snd()

    if values.game_is_on:
        game.show_menu(display)
        values.game_is_on = False

    # Настройка сложности
    game.set_difficulty()

    # Создание игрока и врага
    game_player = player.Player()
    game_enemy = enemy.Enemy()

    # Основной цикл игры
    while True:
        # Отслеживание FPS
        clock.tick(values.FPS)

        # Вывод фона игры
        display.blit(game_bg.image, game_bg.rect)

        # Отслеживание движений и действий игрока
        game_player.track_move(pygame.key.get_pressed())

        # Рождение нового врага, если старый был преодолен
        game_enemy.born()

        # Прорисовка врага
        game_enemy.draw(display)

        # Прорисовка интерфейса игры: очков, защиты, оставшегося для убийства времени
        game.print_interface(display, game_player, game_enemy)

        # Отслеживание событий клавиатуры
        game.track_event(game_player, game_enemy)

        # Похвала для игрока за меткий выстрел
        game.praise_player(display)

        # Прорисовка игрока
        game_player.draw(display)

        # Проверка счета игрока для определения победы и поражения
        game_player.score_check(display)

        # Если пользователь нажал на Try again, игра начинается заново
        if values.again:
            main()

        # Обработка ситуации, в которой игрок оказывается атакованным
        game_player.if_attacked(display, game_enemy)

        # Отрисовка части прицела игрока
        values.line_color = colors.RED

        # Обновление экрана
        pygame.display.update()


# Запуск
values.game_is_on = True
main()
