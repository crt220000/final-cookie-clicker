import pygame

WIDTH = 960
HEIGHT = 720


def draw(screen, cookie_img, cookie_rect):
    screen.blit(cookie_img, cookie_rect)

def counter(screen, click_count):
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render(f"Clicks: {click_count[0]}", True, (19, 8, 74))
    screen.blit(text, (370,530))

def main():
    pygame.init()
    window_res = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(window_res)
    pygame.display.set_caption("Cookie Clicker")
    cookie_img = pygame.image.load('cookie.png')
    cookie_rect = cookie_img.get_rect(center=(WIDTH//2, HEIGHT//2))
    click_count = [0]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        screen.fill((184, 153, 204))
        draw(screen, cookie_img, cookie_rect)
        counter(screen, click_count)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
