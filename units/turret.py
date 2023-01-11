class Turret:
    
    def __init__(self, pos, image_origin):
        self.image_origin = image_origin
        self.image = self.image_origin
        self.rect = self.image.get_rect(topleft = pos)

        self.vector = pygame.math.Vector2()

        self.reload = RELOAD
        self.cur_reload = RELOAD
        self.shot_speed = SHOT_SPEED

    def rotate_head(self, vector):
        direction = (int(vector.x), int(vector.y))

        match direction: 
            case (0, -1):
                deg = 0
                self.rect_head.centerx = self.rect.centerx
                self.rect_head.centery = self.rect.centery - 24
            case (0, 1):
                deg = 180
                self.rect_head.centerx = self.rect.centerx
                self.rect_head.centery = self.rect.centery + 23
            case (-1, 0):
                deg = 90
                self.rect_head.centerx = self.rect.centerx - 49
                self.rect_head.centery = self.rect.centery + 25
            case (1, 0):
                deg = -90
                self.rect_head.centerx = self.rect.centerx - 2
                self.rect_head.centery = self.rect.centery + 25
            case _:
                deg = 0
        
        self.image_head = pygame.transform.rotate(self.image_head_origin, deg)

    def shot(self):
        if self.cur_reload >= self.reload:
            pos = (self.rect_head.centerx, self.rect_head.centery)
            Shell(pos, self.vector_head, self.image_shell_origin, self.groups, self.obstacle_sprites)
            self.cur_reload = 0
        else:
            self.cur_reload += 0.09