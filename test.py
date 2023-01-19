self.view_point = self.rect.center

obstacle_points = {}
for sprite in self.obstacles:
    if sprite is not self:
        obstacle_points[sprite] = [
            sprite.rect.topleft, 
            sprite.rect.topright, 
            sprite.rect.bottomleft, 
            sprite.rect.bottomright
        ]

for sprite in self.objects:
    if sprite is not self:
        points = [
            sprite.rect.topleft, 
            sprite.rect.topright, 
            sprite.rect.bottomleft, 
            sprite.rect.bottomright
        ]
        for point in points:
            diff = (point[0] - self.view_point[0], point[1] - self.view_point[1])
            diff = (abs(diff[0]), abs(diff[1]))

            if diff[0] <= self.view_range and diff[1] <= self.view_range:
                pygame.draw.aaline(surface, (0, 0, 0), point - offset, self.view_point - offset)