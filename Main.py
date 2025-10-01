import pyglet
from pyglet.window import mouse
from pyglet import shapes as sh


wind = pyglet.window.Window(720, 600)
A = sh.Circle(0, 0, 5)
B = sh.Circle(0, 0, 5)
XY1 = [0, 0]
XY2 = [0, 0]
pak = pyglet.graphics.Batch() 

@wind.event
def on_mouse_press(x, y, button, modifiers):
    # Первая точка
    if button == mouse.LEFT:
        global A
        global point_A
        A = sh.Circle(x, y, 5, color=(255, 255, 255), batch=pak)
        XY1[0] = x
        XY1[1] = y
        point_A = pyglet.text.Label(
            'A',
            x=XY1[0] - 5, y=XY1[1] + 15,
            font_size=14, font_name='Arial',
            color=(255, 255, 255), batch=pak)
        
    # Вторая точка
    elif button == mouse.RIGHT:
        global B
        global point_B
        B = sh.Circle(x, y, 5, color=(255, 255, 255), batch=pak)
        XY2[0] = x
        XY2[1] = y
        point_B = pyglet.text.Label(
            'B',
            x=XY2[0] - 5, y=XY2[1] + 15,
            font_size=14, font_name='Arial',
            color=(255, 255, 255), batch=pak)

    Y = XY1[0] - XY2[0]
    X = XY1[1] - XY2[1]

    # Отрезок соеденяющий А и В
    global line
    line = sh.Line(
        XY1[0], XY1[1], XY2[0], XY2[1],
        color=(255, 255, 255), thickness=10,
        batch=pak)

    str_A = f'A [x:{XY1[0]}  y:{XY1[1]}]'
    str_B = f'B [x:{XY2[0]}  y:{XY2[1]}]'
    otv = str((X ** 2 + Y ** 2) ** 0.5)
    
    global tabl_text
    tabl_text = {
        otv: None,
        str_A: None,
        str_B: None}

    y0 = 570
    for text in tabl_text.keys():
        tabl_text[text] = pyglet.text.Label(
            text, x=25, y=y0,
            font_size=16, font_name='Arial',
            color=(255, 255, 255), batch=pak)
        y0 -= 20


            # Перенеси ЭТО в for
    # Растоянние между А и В

    


@wind.event
def on_draw():
    wind.clear()
    pak.draw()

pyglet.app.run()
