import pyglet
from pyglet.window import mouse
from pyglet import shapes as sh


wind = pyglet.window.Window(720, 600)
pak = pyglet.graphics.Batch() 
A_XY = [0, 0] # Координаты точки А
B_XY = [0, 0] # Координаты точки В

@wind.event
def on_mouse_press(x, y, button, modifiers):
    # Первая точка
    if button == mouse.LEFT:
        global A
        global point_A
        A = sh.Circle(x, y, 5, color=(255, 255, 255), batch=pak)
        A_XY[0] = x
        A_XY[1] = y
        point_A = pyglet.text.Label(
            'A', x=(x - 5), y=(y + 15),
            font_size=14, font_name='Arial',
            color=(255, 255, 255), batch=pak)
        
    # Вторая точка
    elif button == mouse.RIGHT:
        global B
        global point_B
        B = sh.Circle(x, y, 5, color=(255, 255, 255), batch=pak)
        B_XY[0] = x
        B_XY[1] = y
        point_B = pyglet.text.Label(
            'B', x=(x - 5), y=(y + 15),
            font_size=14, font_name='Arial',
            color=(255, 255, 255), batch=pak)

    line_Y = A_XY[0] - B_XY[0] # Растояние от A.x до B.x
    line_X = A_XY[1] - B_XY[1] # Растояние от A.y до B.y

    # Отрезок соеденяющий А и В
    global line
    line = sh.Line(
        A_XY[0], A_XY[1], B_XY[0], B_XY[1],
        color=(255, 255, 255), thickness=10,
        batch=pak)

    # Текст с растоянием от A до В и координатами этих точек
    str_A = f'A [x:{A_XY[0]}  y:{A_XY[1]}]'
    str_B = f'B [x:{B_XY[0]}  y:{B_XY[1]}]'
    otv = str((line_X ** 2 + line_Y ** 2) ** 0.5)
    
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

    tabl_text[str_B].x -= 1  # В размером 16px на 1px больше чем A


@wind.event
def on_draw():
    wind.clear()
    pak.draw()

pyglet.app.run()
