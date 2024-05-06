import pygame

WIDTH = 960
HEIGHT = 720


def draw(screen, cookie_img, cookie_rect):
    screen.blit(cookie_img, cookie_rect)

def counter(screen, click_count):
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render(f"Clicks: {click_count[0]}", True, (19, 8, 74))
    screen.blit(text, (370,530))

def user_interaction(cookie_rect, cookie_img, cookie_clicked_img, screen, click_count, crunch):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()       
                if cookie_rect.collidepoint(mouse_pos):
                    click_count[0] += 1
                    screen.blit(cookie_clicked_img, cookie_rect)
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(cookie_img, cookie_rect)
                    pygame.display.flip()
                    crunch.play()
                    print("Cookie clicked!")

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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        screen.fill((184, 153, 204))
        draw(screen, cookie_img, cookie_rect)
        counter(screen, click_count)
        user_interaction(cookie_rect, cookie_img, cookie_clicked_img, screen, click_count, crunch)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
