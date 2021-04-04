import colors

FPS = 300
dis_width = 1000
dis_height = 600
player_move_speed = 2

player_time_for_kill = 2

object_pos_x = dis_width // 2
object_pos_y = dis_height // 2

player_radius = 50

player_score = 0
player_armor = 0
player_armor_got = 0

line_color = colors.WHITE

is_alive = False

begin_of_life = 0

started = False

nice_shot = False
nice_shot_start = 0

enemy_images = ["pics/party_creamer.png", "pics/party_saucer.png", "pics/wing_fish.png", "pics/skeleton.png"]
friends_images = ["pics/bear.png", "pics/bear1.png"]

praises = ["Bull eye!", "Nice shot!", "What an aim!", "Amazing!", "Perfect!"]
praise_chs = "Bull eye!"

shot = " "
