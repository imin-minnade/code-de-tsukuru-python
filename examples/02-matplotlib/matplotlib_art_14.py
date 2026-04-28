import matplotlib.pyplot as plt
import matplotlib

# 日本語フォントの設定
import platform
if platform.system() == "Darwin":      # macOS
    matplotlib.rc("font", family="Hiragino Sans")
elif platform.system() == "Windows":   # Windows
    matplotlib.rc("font", family="MS Gothic")

months = ["1月", "2月", "3月", "4月", "5月", "6月"]
visitors = [1200, 1350, 1800, 2200, 2800, 3100]

plt.plot(months, visitors, marker="o", color="green", linewidth=2)
plt.title("月別サイト訪問者数")
plt.ylabel("訪問者数")
plt.grid(True)
plt.show()