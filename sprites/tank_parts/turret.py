import pygame
import units



class Turret(units.Moving):
    
    def __init__(self, position, path, groups, hp, speed, obstacles):
        super().__init__(position, path, groups, hp, speed, obstacles)

    # reloading = 1
        # shot_speed = 20
        # damage = 50



# self.shot_speed = shot_speed
# self.damage = damage
# self.ammunition = ammunition
# self.reloading = reloading * 1000
# self.is_shot_ready = False
# self.cur_reloading = 0
# self.start_reloading = pygame.time.get_ticks()
# self.left_time_reloading = self.get_left_time_reloading()

    # def move(self):
    #     if self.vector == (0, -1):
    #         self.rect.centerx = self.tank.rect.centerx
    #         self.rect.centery = self.tank.rect.centery - 24
    #     elif self.vector == (0, 1):
    #         self.rect.centerx = self.tank.rect.centerx
    #         self.rect.centery = self.tank.rect.centery + 23
    #     elif self.vector == (-1, 0):
    #         self.rect.centerx = self.tank.rect.centerx - 49
    #         self.rect.centery = self.tank.rect.centery + 25
    #     elif self.vector == (1, 0):
    #         self.rect.centerx = self.tank.rect.centerx - 2
    #         self.rect.centery = self.tank.rect.centery + 25


    # def shot(self):
#         if self.is_shot_ready and self.ammunition:
            
#             if self.turret.vector == (0, -1): pos = (self.rect.centerx, self.turret.rect.top - self.shell_size[1] * 3)
#             elif self.turret.vector == (0, 1): pos = (self.rect.centerx, self.turret.rect.bottom + self.shell_size[1] * 3)
#             elif self.turret.vector == (-1, 0): pos = (self.turret.rect.left - self.shell_size[0] * 3, self.rect.centery)
#             elif self.turret.vector == (1, 0): pos = (self.turret.rect.right + self.shell_size[0] * 10, self.rect.centery)

#             Shell(pos, self.turret.vector, self.shot_speed, self.damage, self.image_shell_origin, self.sprites)

#             self.ammunition -= 1
#             self.is_shot_ready = False
#             self.start_reloading = pygame.time.get_ticks()

# def set_shot_ready(self):
#     self.cur_reloading = pygame.time.get_ticks()
#     self.left_time_reloading = self.get_left_time_reloading()

#     if self.left_time_reloading <= 0:
#         self.is_shot_ready = True

# def get_left_time_reloading(self):
#     left_time_reloading = self.reloading - (self.cur_reloading - self.start_reloading)
#     return left_time_reloading if left_time_reloading > 0 else 0

# def hit(self, damage):
#     self.hp -= damage
#     if self.hp <= 0:
#         self.remove_self()

# def input(self):
#     self.vector.x = 0
#     self.vector.y = 0

# def update(self):
#     self.input()
#     self.move(self.speed)
#     self.turret.update()
#     self.set_shot_ready()