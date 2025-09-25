import pyglet
from pyglet.window import mouse
from pyglet import shapes as sh


wind = pyglet.window.Window(720, 600)
aa = sh.Circle(0, 0, 5)
ab = sh.Circle(0, 0, 5)
XY1 = [0, 0]
XY2 = [0, 0]
lab = pyglet.graphics.Batch() 

@wind.event
def on_mouse_press(x, y, button, modifiers):
    # Первая точка
    global line
    if button == mouse.LEFT:
        global aa
        aa = sh.Circle(x, y, 5, color=(255, 255, 255))
        XY1[0] = x
        XY1[1] = y

        Y = XY1[0] - XY2[0]
        X = XY1[1] - XY2[1]
        line = sh.Line(XY1[0], XY1[1], XY2[0], XY2[1], 
                        color=(255, 255, 255), thickness=10, batch=lab)

    # Вторая точка
    elif button == mouse.RIGHT:
        global ab
        ab = sh.Circle(x, y, 5, color=(255, 255, 255))
        XY2[0] = x
        XY2[1] = y

        Y = XY1[0] - XY2[0]
        X = XY1[1] - XY2[1]
        line = sh.Line(XY1[0], XY1[1], XY2[0], XY2[1],
                            color=(255, 255, 255), thickness=10, batch=lab)


    otv = (X ** 2 + Y ** 2) ** 0.5
    print(otv, XY1, XY2)
    

    global label
    global label_aa
    global label_ab
    str_aa = f'x:{XY1[0]}  y:{XY1[1]}'
    str_ab = f'x:{XY2[0]}  y:{XY2[1]}'

    label = pyglet.text.Label(
        str(otv),
        x=25, y=570,
        font_size=16,
        font_name='Arial',
        color=(255, 255, 255), batch=lab)
    
    # Показывает координаты точки аа
    label_aa = pyglet.text.Label(
        str_aa,
        x=25, y=550,
        font_size=16,
        font_name='Arial',
        color=(255, 255, 255), batch=lab)
    
    # Показывает координаты точки аb
    label_ab = pyglet.text.Label(
        str_ab,
        x=25, y=530,
        font_size=16,
        font_name='Arial',
        color=(255, 255, 255), batch=lab)


@wind.event
def on_draw():
    wind.clear()
    aa.draw()
    ab.draw()
    lab.draw()
    
pyglet.app.run() 
