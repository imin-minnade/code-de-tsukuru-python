import pyxel

pyxel.init(128, 140, title="ドット絵エディタ")
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)

pyxel.run(update, draw)