import pygame

WIDTH = 960
HEIGHT = 720


def draw(screen, cookie_img, cookie_rect):
    screen.blit(cookie_img, cookie_rect)

def main():
    pygame.init()
    window_res = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(window_res)
    pygame.display.set_caption("Cookie Clicker")
    cookie_img = pygame.image.load('cookie.png')
    cookie_rect = cookie_img.get_rect(center=(WIDTH//2, HEIGHT//2))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        screen.fill((184, 153, 204))
        draw(screen, cookie_img, cookie_rect)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
