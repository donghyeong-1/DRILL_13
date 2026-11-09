from pico2d import clear_canvas, get_events, update_canvas
from sdl2 import SDL_KEYDOWN, SDL_QUIT, SDLK_p
import game_framework
import game_world


def init():
    pass


def finish():
    pass


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def pause():
    pass


def resume():
    pass

