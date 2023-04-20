import pygame
import time
class Player():
    def __init__(self, x, y, width, height, color, win_width, win_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = [win_width, win_height]
        self.rect = (x,y,width,height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 4
        self.speed_up_start_time = 0
        self.speed_up_charges = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    speed_up_start_time = None
    def move(self):
        keys = pygame.key.get_pressed()
        speed_up_duration = 1

        if keys[pygame.K_SPACE] and self.speed_up_charges < 5:
            self.vel = 7
            if self.speed_up_start_time == 0:
                self.speed_up_start_time = time.time()
                self.speed_up_charges += 1 
        if time.time() - self.speed_up_start_time > speed_up_duration:
            self.speed_up_start_time = 0
            self.vel = 4

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            if self.x < 0:
                self.x = self.win[0] 

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            if self.x > self.win[0]:
                self.x = self.width

        if keys[pygame.K_UP]:
            self.y -= self.vel
            if self.y < 0:
                self.y = self.win[1] 

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            if self.y > self.win[1]:
                self.y = self.height 
        
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update()

    def toque(self, hitbox):
        if self.hitbox.colliderect(hitbox):
            return True

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)