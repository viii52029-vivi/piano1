import pygame
from buttons import Button
from ui.slider import Slider

class SettingsMenu:
    def __init__(self, screen_rect, initial_volume, initial_keys, min_keys, max_keys, on_change, on_back):
        self.screen_rect = screen_rect          # Розмір екрану для позиціювання елементів
        self.on_change = on_change              # Функція, що викликається при зміні налаштувань
        self.on_back = on_back                  # Функція, що викликається при натисканні кнопки назад
        cx = screen_rect.centerx               # Центр екрану по горизонталі
        top = 140                              # Верхня позиція для слайдерів
        # Завантаження зображень для кнопки "Назад"
        back_idle = pygame.transform.scale(
            pygame.image.load('assets/images/buttons/exit_unhover.png'), (48, 48)
        )
        back_hover = pygame.transform.scale(
            pygame.image.load('assets/images/buttons/exit_hover.png'), (48, 48)
        )
        # Кнопка "Назад"
        self.back_btn = Button(
            40, 30, 48, 48,
            "",
            self._back,                        # Дія при натисканні — виклик методу _back
            img_idle=back_idle,
            img_hover=back_hover
        )
        # Функція форматування значення гучності для відображення (0.75 -> "75%")
        def volume_to_text(v):
            return f"{int(v * 100)}%"
        # Слайдер гучності
        self.volume_slider = Slider(
            cx - 200, top, 400,                # Позиція і ширина слайдера
            0.0, 1.0, step=0.01, initial=initial_volume,
            label="Гучність",
            value_to_text=volume_to_text       # Форматування тексту
        )
        self.volume_slider.set_on_change(self._on_volume)  # Встановлюємо callback для гучності
        # Функція форматування значення кількості клавіш (просто цілі числа)
        def keys_to_text(v):
            return str(int(v))
        # Слайдер кількості клавіш
        self.keys_slider = Slider(
            cx - 200, top + 120, 400,
            min_keys, max_keys, step=1, initial=initial_keys,
            label="Кількість клавіш",
            value_to_text=keys_to_text
        )
        self.keys_slider.set_on_change(self._on_keys)  # Встановлюємо callback для кількості клавіш

    def _on_volume(self, v):
        # Викликається при зміні гучності
        if self.on_change:
            self.on_change(float(v), int(self.keys_slider.value))

    def _on_keys(self, v):
        # Викликається при зміні кількості клавіш
        if self.on_change:
            self.on_change(float(self.volume_slider.value), int(v))

    def _back(self):
        # Викликається при натисканні кнопки "Назад"
        if self.on_back:
            self.on_back()

    def draw(self, screen, font):
        # Малюємо заголовок меню
        title = font.render("Налаштування", True, (0, 0, 0))
        screen.blit(title, title.get_rect(center=(self.screen_rect.centerx, 80)))
        # Малюємо кнопку назад і слайдери
        self.back_btn.draw(screen, font)
        self.volume_slider.draw(screen, font)
        self.keys_slider.draw(screen, font)

    def handle_event(self, event):
        # Передаємо події всім елементам управління
        self.back_btn.handle_event(event)
        self.volume_slider.handle_event(event)
        self.keys_slider.handle_event(event)