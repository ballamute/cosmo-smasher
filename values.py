import colors

# Значения игры
game_name = "Cosmo smasher"
def_font = "fonts/rostov.ttf"

key_control = "keyboard"
mouse_control = "mouse"
control = key_control

easy_diff = "easy"
medium_diff = "medium"
hard_diff = "hard"
difficulty = easy_diff

game_is_on = False
started = False
again = False

FPS = 300
dis_width = 1000
dis_height = 600
center_x = dis_width // 2
center_y = dis_height // 2

# Время для убийства
easy_mouse_kill_time = 1
medium_mouse_kill_time = 0.75
hard_mouse_kill_time = 0.5
easy_key_kill_time = 3
medium_key_kill_time = 2.5
hard_key_kill_time = 2
red_screen_delay = 0.1

# Значения переменных игрока
player_move_speed = 2
player_time_for_kill = easy_key_kill_time
player_score = 0
player_armor = 0
player_armor_got = 0
player_radius = 50
line_color = colors.WHITE
line_shot_color = colors.YELLOW

# Значения правил игры
plus_armor_border = 10
win_border = 25
arm_lose_border = 0
scr_lose_border = 0

# Координаты объектов игры
object_pos_x = dis_width // 2
object_pos_y = dis_height // 2

# Значения переменных врага
is_alive = False
begin_of_life = 0

# Значения переменных выстрела
nice_shot = False
nice_shot_start = 0
nice_shot_bonus = 2
shot_bonus = 1
miss_penalty = 1
overtime_penalty = 1
shot = " "
LMB_key = 1

# Значения переменных похвалы
praises = ["Bull eye!", "Nice shot!", "What an aim!", "Amazing!", "Perfect!"]
praise_chs = "Bull eye!"

# Значения переменных изображений
game_bg_img = "pics/game_bg.png"
menu_bg_img = "pics/menu_bg.jpg"
def_en_image = "pics/party_saucer.png"
cross_img = "pics/cross.png"
enemy_images = ["pics/party_creamer.png", "pics/party_saucer.png", "pics/wing_fish.png", "pics/skeleton.png"]
friends_images = ["pics/bear.png", "pics/bear1.png"]

# Значения переменных звуков
back_music = "music/back_music.wav"
shot_snd = "music/laser.wav"
dead_snd = "music/dead.wav"
game_over_snd = "music/game_over.wav"
win_snd = "music/you_win.wav"
mixer_frequency = 44100
mixer_size = -16
mixer_channels = 2
mixer_buffer = 4096
en_down_sound_volume = 0.2

# Значения переменных меткого выстрела
ns_time = 1
ns_x = dis_width // 2 - 65
ns_y = 10
ns_color = colors.WHITE
ns_coefficient = 1/3

# Значения переменных отображения очков
score_x = 10
score_y = 10
score_color = colors.WHITE

# Значения переменных отображения брони
armor_x = 10
armor_y = 50
armor_color = colors.WHITE

# Значения переменных отображения времени для убийства врага
t_for_k_x = dis_width - 250
t_for_k_y = 10
t_for_k_color = colors.WHITE

# Значения переменных отображения вопроса после выстрела в мишку
bear_ask_x = dis_width // 2 - 330
bear_ask_y = dis_height // 2 - 50
bear_ask_size = 40
bear_ask_color = colors.RED

# Значения переменных отображения очков после выстрела в мишку
bear_score_x = dis_width // 2 - 170
bear_score_y = dis_height // 2 + 25
bear_score_size = 30
bear_score_color = colors.WHITE

# Значения переменных отображения Game Over
over_x = dis_width // 2 - 170
over_y = dis_height // 2 - 50
over_size = 60
over_color = colors.RED

# Значения переменных отображения очков после Game Over
ov_score_x = dis_width // 2 - 125
ov_score_y = dis_height // 2 + 25
ov_score_size = 30
ov_score_color = colors.WHITE


# Значения переменных отображения You win
win_x = dis_width // 2 - 140
win_y = dis_height // 2 - 50
win_size = 60
win_color = colors.GREEN

# Значения переменных отображения кнопки Try again
try_again_tl = (421, 373)
try_again_br = (551, 393)
try_again_x = dis_width // 2 - 80
try_again_y = dis_height // 2 + 70
try_again_size = 30
try_again_color = colors.WHITE

# Значения переменных отображения кнопки Exit
exit_tl = (461, 418)
exit_br = (507, 439)
exit_x = center_x - 40
exit_y = center_y + 115
exit_size = 30
exit_color = colors.WHITE

# Значения переменных отображения кнопки Play in menu
play_tl = (431, 285)
play_br = (542, 320)
play_x = center_x - 70
play_y = center_y - 20
play_size = 50
play_color = colors.GREEN

# Значения переменных отображения кнопки Exit in menu
exit_menu_tl = (461, 508)
exit_menu_br = (522, 536)
exit_menu_x = center_x - 40
exit_menu_y = center_y + 205
exit_menu_size = 40
exit_menu_color = colors.BRICK_RED

# Значения переменных отображения кнопки mouse in menu
mouse_menu_tl = (552, 378)
mouse_menu_br = (638, 399)
mouse_menu_x = center_x + 50
mouse_menu_y = center_y + 75
mouse_menu_size = 30
mouse_menu_color = colors.WHITE

# Значения переменных отображения кнопки keyboard in menu
key_menu_tl = (301, 378)
key_menu_br = (437, 397)
key_menu_x = center_x - 200
key_menu_y = center_y + 75
key_menu_size = 30
key_menu_color = colors.WHITE

# Значения переменных отображения надписи control in menu
control_x = center_x - 80
control_y = center_y + 35
control_size = 30
control_color = colors.DODGER_BLUE

# Значения переменных отображения кнопки back to the main menu
back_tl = (357, 459)
back_br = (625, 478)
back_x = center_x - 145
back_y = center_y + 155
back_size = 30
back_color = colors.WHITE

# Значения переменных отображения названия игры in menu
caption_x = center_x - 340
caption_y = center_y - 190
caption_size = 90
caption_color = colors.WHITE

# Значения переменных отображения надписи difficulty in menu
difficulty_x = center_x - 80
difficulty_y = center_y + 110
difficulty_size = 30
difficulty_color = colors.DODGER_BLUE

# Значения переменных отображения кнопки easy
easy_tl = (321, 453)
easy_br = (381, 479)
easy_x = center_x - 180
easy_y = center_y + 150
easy_size = 30
easy_color = colors.WHITE

# Значения переменных отображения кнопки medium
medium_tl = (436, 453)
medium_br = (540, 473)
medium_x = center_x - 65
medium_y = center_y + 150
medium_size = 30
medium_color = colors.WHITE

# Значения переменных отображения кнопки hard
hard_tl = (582, 452)
hard_br = (640, 473)
hard_x = center_x + 80
hard_y = center_y + 150
hard_size = 30
hard_color = colors.WHITE
