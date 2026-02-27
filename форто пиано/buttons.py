import pygame

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.color = (200, 200, 200)
        self.hover_color = (170, 220, 255)
        self.border_color = (0, 0, 0)
        self.is_hovered = False

    def draw(self, screen, my_font):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, self.border_color, self.rect, 2, border_radius=8)

        text_surface = my_font.render(self.text, True, self.border_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, e):
        if e.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(e.pos)

        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(e.pos):
                self.callback()
