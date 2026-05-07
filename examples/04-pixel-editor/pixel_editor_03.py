import pyxel

WINDOW_WIDTH = 128
GRID_SIZE = 16
PIXEL_SIZE = WINDOW_WIDTH // GRID_SIZE

# --- Step_03: ここから追加（ピクセルデータを2次元配列で持つ） ---
# グリッドデータを初期化（-1 = 透明）
grid = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
# --- Step_03: ここまで ---

pyxel.init(WINDOW_WIDTH, WINDOW_WIDTH + GRID_SIZE, title="ドット絵エディタ")
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

# --- Step_03: ここから追加（データと表示を分離） ---
def draw_canvas():
    """gridの中身に従ってキャンバスを描く"""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color_id = grid[y][x]
            x1 = x * PIXEL_SIZE
            y1 = y * PIXEL_SIZE
            if color_id == -1:
                # 透明: 白で表示（後で改良します）
                pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, 7)
            else:
                pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, color_id)

def draw_grid_lines():
    """グリッド線を引く"""
    for i in range(GRID_SIZE + 1):
        pos = i * PIXEL_SIZE
        pyxel.line(pos, 0, pos, WINDOW_WIDTH, 1)
        pyxel.line(0, pos, WINDOW_WIDTH, pos, 1)
# --- Step_03: ここまで ---

def draw():
    pyxel.cls(0)
    draw_canvas()
    draw_grid_lines()

pyxel.run(update, draw)