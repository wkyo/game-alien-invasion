class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.fps = 30  # framerate

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.speed_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_limit = 3

        self.ship_speed = 10
        self.bullet_speed = 5
        self.fleet_drop_speed = 30  # alien drop speed
        self.fleet_speed_x = 2  # horizontal moving speed
        self.fleet_direction_x = 1  # 1: move right, -1: move left, 0: no moving

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.fleet_speed_x *= self.speed_scale

        self.alien_points = int(self.alien_points * self.speed_scale)