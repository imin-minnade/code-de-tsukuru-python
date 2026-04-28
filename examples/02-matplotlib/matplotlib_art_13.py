import matplotlib.pyplot as plt
import matplotlib

# 日本語フォントの設定
import platform
if platform.system() == "Darwin":      # macOS
    matplotlib.rc("font", family="Hiragino Sans")
elif platform.system() == "Windows":   # Windows
    matplotlib.rc("font", family="MS Gothic")

temperature = [15, 18, 22, 25, 28, 30, 33, 35]
ice_cream_sales = [20, 30, 45, 55, 70, 80, 95, 110]

plt.scatter(temperature, ice_cream_sales, color="coral", s=100)
plt.title("気温とアイスの売上")
plt.xlabel("気温（℃）")
plt.ylabel("アイスの売上（個）")
plt.show()