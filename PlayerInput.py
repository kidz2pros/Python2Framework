import pygame

keys_pressed = dict()


def key_input_listener(event):
    if event.type == pygame.KEYDOWN and event.key not in keys_pressed:
        keys_pressed[event.key] = True
    elif event.type == pygame.KEYDOWN and not keys_pressed[event.key] :
        keys_pressed[event.key] = True
    elif event.type == pygame.KEYUP and keys_pressed[event.key]:
        keys_pressed[event.key] = False


def is_key_down(input_key):
    if input_key in keys_pressed:
        return keys_pressed[input_key]
    else:
        return False


def is_key_pressed(input_key):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == input_key:
                return True
    return False


def is_key_released(input_key):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == input_key:
                return True
    return False




