import pyxel

WINDOW_WIDTH = 128
GRID_SIZE = 16
PIXEL_SIZE = WINDOW_WIDTH // GRID_SIZE

grid = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# まだ「パレットをクリックして色変更」が未実装なので、ひとまず赤を初期値にしておきます（次のステップでクリック選択できるようにします）
selected_color = 8

# --- Step_05: ここから追加（パレット用の変数定義） ---
# 色リスト: -1（透明）+ Pyxel標準16色（0〜15）
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
# --- Step_05: ここまで ---

pyxel.init(WINDOW_WIDTH, WINDOW_WIDTH + GRID_SIZE, title="ドット絵エディタ")
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # クリック/ドラッグで描画（まだ赤固定）
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        grid_x = pyxel.mouse_x // PIXEL_SIZE
        grid_y = pyxel.mouse_y // PIXEL_SIZE
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
            grid[grid_y][grid_x] = selected_color

def draw_canvas():
    """gridの中身に従ってキャンバスを描く"""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color_id = grid[y][x]
            x1 = x * PIXEL_SIZE
            y1 = y * PIXEL_SIZE
            if color_id == -1:
                pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, 7)
            else:
                pyxel.rect(x1, y1, PIXEL_SIZE, PIXEL_SIZE, color_id)

def draw_grid_lines():
    """グリッド線を引く"""
    for i in range(GRID_SIZE + 1):
        pos = i * PIXEL_SIZE
        pyxel.line(pos, 0, pos, WINDOW_WIDTH, 1)
        pyxel.line(0, pos, WINDOW_WIDTH, pos, 1)

# --- Step_05: ここから追加（パレット描画） ---
def draw_palette():
    """画面下部にカラーパレットを描画"""
    for i, color in enumerate(colors):
        x = i * PALETTE_WIDTH

        if color == -1:
            # 透明色はチェック柄で表現（Photoshopと同じ慣習）
            for dy in range(0, PALETTE_HEIGHT, 2):
                for dx in range(0, PALETTE_WIDTH, 2):
                    c = 7 if (dx // 2 + dy // 2) % 2 == 0 else 13
                    pyxel.rect(x + dx, PALETTE_Y + dy, 2, 2, c)
        else:
            pyxel.rect(x, PALETTE_Y, PALETTE_WIDTH, PALETTE_HEIGHT, color)

        # 選択中の色を枠で強調
        if color == selected_color:
            border = 13 if color == 7 else 7
            pyxel.rectb(x, PALETTE_Y, PALETTE_WIDTH, PALETTE_HEIGHT, border)
# --- Step_05: ここまで ---

def draw():
    pyxel.cls(0)
    draw_canvas()
    draw_grid_lines()

    # --- Step_05: ここから追加 ---
    draw_palette()
    # --- Step_05: ここまで ---

pyxel.run(update, draw)