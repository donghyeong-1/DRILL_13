from pico2d import load_image

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    pass


def render():
    pass


def handle_events():
    pass


def pause():
    pass


def resume():
    pass
