from pico2d import clear_canvas, get_events, load_image, update_canvas
from sdl2 import (SDL_KEYDOWN, SDL_QUIT, SDLK_0, SDLK_1, SDLK_2, SDLK_ESCAPE,
                  SDLK_KP_0, SDLK_KP_1, SDLK_KP_2, SDLK_i)
import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_i, SDLK_ESCAPE):
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_KP_0):
            play_mode.boy.set_item(None)
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_1, SDLK_KP_1):
            play_mode.boy.set_item('Ball')
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_2, SDLK_KP_2):
            play_mode.boy.set_item('BigBall')


def pause():
    pass


def resume():
    pass
