import pygame
import units


class Tank(units.Moving):

    def __init__(self, position, paths, groups, hp, speed, obstacles, visibles, ammunition):
        super().__init__(position, paths['hull'], groups, hp, speed, obstacles)
        
        self.ammunition = ammunition

        self.turret = Turret(
            position = position, 
            path = paths['turret'],     
            groups = visibles,
            vector = pygame.math.Vector2(0, -1),
            tank = self,
            damage = 50,
            shell_path = paths['shell']
        )

    def _shot(self):
        self.turret._shot()

    def _move_action(self):
        self.turret._move()

    def _draw(self, surface, position):
        surface.blit(self.image, position)

        offset = self.rect.topleft - position
        position_turret = self.turret.rect.topleft - offset
        self.turret._custom_draw(surface, position_turret)


class Turret(units.Sprite):

    def __init__(self, position, path, groups, vector, tank, damage, shell_path):
        super().__init__(position, path, groups)
        self.position = position
        self.vector = vector
        self.tank = tank

        self.shell_path = shell_path
        self.shell_damage = damage
        self.shell_speed = 20
        self.reloading_time = 1_000
        self.is_shot_ready = False
        self.cur_reloading_time = 0
        self.start_reloading = pygame.time.get_ticks()
        self._set_reloading()

        self._move()

    def _move(self):
        if self.vector == (0, -1):
            self.rect.centerx = self.tank.rect.centerx
            self.rect.centery = self.tank.rect.centery - 24
        elif self.vector == (0, 1):
            self.rect.centerx = self.tank.rect.centerx
            self.rect.centery = self.tank.rect.centery + 23
        elif self.vector == (-1, 0):
            self.rect.centerx = self.tank.rect.centerx - 49
            self.rect.centery = self.tank.rect.centery + 25
        elif self.vector == (1, 0):
            self.rect.centerx = self.tank.rect.centerx - 2
            self.rect.centery = self.tank.rect.centery + 25

    def _set_vector(self, degree):
        match degree:
            case 0:   self.vector = pygame.math.Vector2(0, -1)
            case 180: self.vector = pygame.math.Vector2(0, 1)
            case 90:  self.vector = pygame.math.Vector2(-1, 0)
            case -90: self.vector = pygame.math.Vector2(1, 0)

    def _rotate_action(self, degree):
        self._set_vector(degree)

    def _draw(self, surface, position): pass

    def _custom_draw(self, surface, position):
        surface.blit(self.image, position)

    def _shot(self):
        if self.is_shot_ready:
            if self.vector == (0, -1): 
                position = (self.rect.centerx, self.rect.top - 21)
            elif self.vector == (0, 1): 
                position = (self.rect.centerx, self.rect.bottom + 21)
            elif self.vector == (-1, 0): 
                position = (self.rect.left  - 21, self.rect.centery - 28)
            elif self.vector == (1, 0): 
                position = (self.rect.right + 70, self.rect.centery - 30)

            Shell(
                position = position, 
                path = self.shell_path, 
                groups = self.tank.groups(), 
                hp = 1,
                speed = self.shell_speed, 
                obstacles = self.tank.obstacles,
                vector = self.vector,
                damage = self.shell_damage
            )

            self.tank.ammunition -= 1
            self.is_shot_ready = False
            self.start_reloading = pygame.time.get_ticks()

    def _set_reloading(self):
        reloading = self.reloading_time - (self.cur_reloading_time - self.start_reloading)
        self.reloading = reloading if reloading > 0 else 0

    def _set_shot_ready(self):
        self.cur_reloading_time = pygame.time.get_ticks()
        self._set_reloading()
        if self.reloading <= 0 and self.tank.ammunition > 0: 
            self.is_shot_ready = True

    def _additional_update(self):
        self._set_shot_ready()


class Shell(units.Moving):
    def __init__(self, position, path, groups, hp, speed, obstacles, vector, damage):
        super().__init__(position, path, groups, hp, speed, obstacles, vector)
        self.damage = damage

    def _move(self, speed):
        self.rect.x += self.vector.x * speed
        self.rect.y += self.vector.y * speed
        self._collision()

        self.position = pygame.math.Vector2(self.rect.topleft)
        self._move_action()

    def _collision(self): 
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect) and self is not sprite:
                sprite.hit(self.damage)
                self._remove()

    def _additional_update(self):
        self._move(self.speed)