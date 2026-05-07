import pyxel

WINDOW_WIDTH = 128
GRID_SIZE = 16
PIXEL_SIZE = WINDOW_WIDTH // GRID_SIZE

grid = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

selected_color = 8

colors = [-1] + list(range(16))
PALETTE_HEIGHT = 8
PALETTE_MARGIN = 2
PALETTE_Y = WINDOW_WIDTH + PALETTE_MARGIN  # キャンバス下にマージンを入れて配置
PALETTE_WIDTH = WINDOW_WIDTH // (len(colors) + 1)

# PNG書き出し用: Pyxelの色番号 → RGB値の対応表
pyxel_palette = [
    (0, 0, 0),        # 0: 黒
    (43, 51, 95),     # 1: ダークブルー
    (126, 32, 114),   # 2: ダークパープル
    (24, 149, 156),   # 3: ダークグリーン
    (139, 72, 82),    # 4: ブラウン
    (57, 92, 152),    # 5: ダークグレー
    (169, 193, 255),  # 6: ライトグレー
    (238, 238, 238),  # 7: 白
    (212, 24, 108),   # 8: 赤
    (211, 132, 65),   # 9: オレンジ
    (233, 195, 91),   # 10: 黄色
    (112, 198, 169),  # 11: 緑
    (118, 150, 222),  # 12: 青
    (163, 163, 163),  # 13: グレー
    (255, 151, 152),  # 14: ピンク
    (237, 199, 176),  # 15: ピーチ
]

pyxel.init(WINDOW_WIDTH, 140, title="ドット絵エディタ")
pyxel.mouse(True)

def update():
    global selected_color

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # パレット領域のクリック判定
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if pyxel.mouse_y >= PALETTE_Y and pyxel.mouse_y < PALETTE_Y + PALETTE_HEIGHT:
            index = pyxel.mouse_x // PALETTE_WIDTH
            if 0 <= index < len(colors):
                selected_color = colors[index]

    # グリッドへの描画（ドラッグ対応）
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        grid_x = pyxel.mouse_x // PIXEL_SIZE
        grid_y = pyxel.mouse_y // PIXEL_SIZE
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
            grid[grid_y][grid_x] = selected_color

def draw_canvas():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color_id = grid[y][x]
            x1 = x * PIXEL_SIZE
            y1 = y * PIXEL_SIZE
            if color_id == -1:
                # --- Step_07: ここを変更（透明をチェック柄で表現） ---
                # pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, 7)
                delta = 2
                for dy in range(0, PIXEL_SIZE, delta):
                    for dx in range(0, PIXEL_SIZE, delta):
                        c = 7 if (dx // delta + dy // delta) % 2 == 0 else 13
                        pyxel.rect(x1 + dx, y1 + dy, delta, delta, c)
                # --- Step_07: ここまで ---
            else:
                pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, color_id)

def draw_grid_lines():
    for i in range(GRID_SIZE + 1):
        pos = i * PIXEL_SIZE
        pyxel.line(pos, 0, pos, WINDOW_WIDTH, 1)
        pyxel.line(0, pos, WINDOW_WIDTH, pos, 1)

def draw_palette():
    for i, color in enumerate(colors):
        x = i * PALETTE_WIDTH
        if color == -1:
            for dy in range(0, PALETTE_HEIGHT, 2):
                for dx in range(0, PALETTE_WIDTH, 2):
                    c = 7 if (dx // 2 + dy // 2) % 2 == 0 else 13
                    pyxel.rect(x + dx, PALETTE_Y + dy, 2, 2, c)
        else:
            pyxel.rect(x, PALETTE_Y, PALETTE_WIDTH, PALETTE_HEIGHT, color)
        if color == selected_color:
            border = 13 if color == 7 else 7
            pyxel.rectb(x, PALETTE_Y, PALETTE_WIDTH, PALETTE_HEIGHT, border)

def draw():
    pyxel.cls(0)
    draw_canvas()
    draw_grid_lines()
    draw_palette()

pyxel.run(update, draw)