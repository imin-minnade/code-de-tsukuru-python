import pyxel

# --- Step_02: ここから追加（定数でサイズを管理） ---
WINDOW_WIDTH = 128   # ウィンドウの幅
GRID_SIZE = 16       # グリッドの分割数（16×16マス）
PIXEL_SIZE = WINDOW_WIDTH // GRID_SIZE  # 1マスの大きさ（8ピクセル）
# --- Step_02: ここまで ---

pyxel.init(WINDOW_WIDTH, WINDOW_WIDTH + GRID_SIZE, title="ドット絵エディタ")  # 変数を修正
pyxel.mouse(True)
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)

    # --- Step_02: ここから追加（背景＋グリッド表示） ---
    # キャンバス背景を白（色番号7）で塗る
    pyxel.rect(0, 0, WINDOW_WIDTH, WINDOW_WIDTH, 7)

    # グリッド線を引く
    for i in range(GRID_SIZE + 1):
        pos = i * PIXEL_SIZE
        pyxel.line(pos, 0, pos, WINDOW_WIDTH, 1)      # 縦線
        pyxel.line(0, pos, WINDOW_WIDTH, pos, 1)      # 横線
    # --- Step_02: ここまで ---

pyxel.run(update, draw)