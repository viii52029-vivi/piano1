import pygame
from pygame import display, event, key, font
from settings import WHITE
from sounds import load_sounds
from keys import draw_keys, creat_keys_rect
from buttons import Button

# (предполагается, что KEYS определён где-то — например в settings.py)
KEYS = {
    "a": "do.wav",
    "s": "re.wav",
    "d": "mi.wav",
    # ... добавь свои клавиши
}

pygame.init()
screen = display.set_mode((800, 600))

sounds = load_sounds(KEYS)
key_rects = creat_keys_rect(len(KEYS))
keys_list = list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()

# Кнопки меню
def start_game(): pass
def open_settings(): pass
def exit_game(): quit()

buttons = [
    Button(60, 20, 120, 40, "Settings", open_settings)
]

running = True
while True:
    screen.fill(WHITE)
    for button in buttons:
        button.draw(screen, my_font)
    draw_keys(screen, key_rects, pressed_keys)

    display.update()

    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(e)

        if e.type == pygame.KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == pygame.KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)

        if e.type == pygame.MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)