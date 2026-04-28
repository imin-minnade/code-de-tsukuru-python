import matplotlib.pyplot as plt
import matplotlib

# 日本語フォントの設定
import platform
if platform.system() == "Darwin":      # macOS
    matplotlib.rc("font", family="Hiragino Sans")
elif platform.system() == "Windows":   # Windows
    matplotlib.rc("font", family="MS Gothic")

days = ["月", "火", "水", "木", "金", "土", "日"]
sleep_hours = [6, 7, 5, 6, 7, 9, 8]

plt.bar(days, sleep_hours, color="steelblue")
plt.title("今週の睡眠時間")
plt.ylabel("時間")
plt.ylim(0, 12)
plt.show()