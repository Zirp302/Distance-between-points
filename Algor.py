import pyglet
from pyglet.window import mouse
from pyglet import shapes as sh
import keyboard


wind = pyglet.window.Window(720, 600)
aa = sh.Circle(0, 0, 5)
ab = sh.Circle(0, 0, 5)
XY1 = [0, 0]
XY2 = [0, 0]
otv = ''
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

        if len(XY2) >= 2:
            Y = XY1[0] - XY2[0]
            X = XY1[1] - XY2[1]
            line = sh.Line(XY1[0], XY1[1], XY2[0], XY2[1], color=(255, 255, 255), thickness=10 ,batch=lab)

    # Вторая точка
    elif button == mouse.RIGHT:
        global ab
        ab = sh.Circle(x, y, 5, color=(255, 255, 255))
        XY2[0] = x
        XY2[1] = y

        if len(XY1) >= 2:
            Y = XY1[0] - XY2[0]
            X = XY1[1] - XY2[1]
            line = sh.Line(XY1[0], XY1[1], XY2[0], XY2[1], color=(255, 255, 255), thickness=10 ,batch=lab)


    otv = (X ** 2 + Y ** 2) ** 0.5
    print(otv, XY1, XY2)
    

    global label
    label = pyglet.text.Label(
        str(otv),
        font_name='Arial',
        font_size=16,
        x=111, y=570,
        anchor_x='center', anchor_y='center', 
        color=(255, 255, 255), batch=lab
    )
    


@wind.event
def on_draw():
    wind.clear()
    aa.draw()
    ab.draw()
    lab.draw()
    
pyglet.app.run() 