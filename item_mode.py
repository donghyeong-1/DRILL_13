from pico2d import clear_canvas, load_image, update_canvas

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
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    pass


def pause():
    pass


def resume():
    pass
