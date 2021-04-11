import colors

# Значения игры
game_name = "Cosmo smasher"
started = False
again = False
FPS = 300
dis_width = 1000
dis_height = 600

# Значения переменных игрока
player_move_speed = 2
player_time_for_kill = 2
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
shot = " "

# Значения переменных похвалы
praises = ["Bull eye!", "Nice shot!", "What an aim!", "Amazing!", "Perfect!"]
praise_chs = "Bull eye!"

# Значения переменных изображений
bg_img = "pics/bg.png"
def_en_image = "pics/party_saucer.png"
cross_img = "pics/cross1.png"
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
exit_x = dis_width // 2 - 40
exit_y = dis_height // 2 + 115
exit_size = 30
exit_color = colors.WHITE
