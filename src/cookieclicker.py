import pygame
import sys
import random
import time


WIDTH = 960
HEIGHT = 720


class Particle:
    def __init__(self, pos):
        self.pos = list(pos)
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(2, 5)
        self.life = 20

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size)

def draw(screen, cookie_img, cookie_rect):
    screen.blit(cookie_img, cookie_rect)

def counter(screen, click_count):
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render(f"Clicks: {click_count[0]}", True, (19, 8, 74))
    screen.blit(text, (370,530))

def user_interaction(cookie_rect, cookie_img, cookie_clicked_img, screen, click_count, crunch, particles):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()       
                if cookie_rect.collidepoint(mouse_pos):
                    click_count[0] += 1
                    clicked = True
                    screen.blit(cookie_clicked_img, cookie_rect)
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(cookie_img, cookie_rect)
                    pygame.display.flip()
                    crunch.play()
                    print("Cookie clicked!")
                    for _ in range(10):
                        particles.append(Particle(mouse_pos))

        elif event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()


def win_condition(screen, click_count):
    font = pygame.font.SysFont("Comic Sans MS", 40)
    if click_count[0] >= 100:
        text = font.render("Cookie Eating Champion!!", True, (115, 255, 134))
    else:
        text = font.render("Your too slow!", True, (161, 6, 6))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)

def instructions(screen):
    font = pygame.font.SysFont("Comic Sans MS", 38)
    text = font.render("Eat 100 cookies under 15 seconds to win!", True, (19, 8, 74))
    screen.blit(text, (100, 120))


def main():
    pygame.init()
    window_res = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(window_res)
    pygame.display.set_caption("Cookie Clicker")
    cookie_img = pygame.image.load('cookie.png')
    cookie_clicked_img = pygame.image.load('cookie-clicked.png')
    cookie_rect = cookie_img.get_rect(center=(WIDTH//2, HEIGHT//2))
    click_count = [0]
    crunch = pygame.mixer.Sound('crunch.wav')
    pygame.mixer.music.load("Background Music.mp3")
    pygame.mixer.music.play(-1)
    particles = []
    start_time = time.time()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        screen.fill((184, 153, 204))
        draw(screen, cookie_img, cookie_rect)
        counter(screen, click_count)
        instructions(screen)
        user_interaction(cookie_rect, cookie_img, cookie_clicked_img, screen, click_count, crunch, particles)


        if time.time() - start_time >= 15:
            win_condition(screen, click_count)
            running = False
        
        for particle in particles[:]:
            particle.update()
            particle.draw(screen)
            if particle.life <= 0:
                particles.remove(particle)
        

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
