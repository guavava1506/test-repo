from datetime import datetime
from zoneinfo import ZoneInfo

print("你好！")
print("Hello!")
print("こんにちは!")

weekday_map = ["一", "二", "三", "四", "五", "六", "日"]

now = datetime.now(ZoneInfo("Asia/Taipei"))
weekday = weekday_map[now.weekday()]

print(f"西元{now.year}.{now.month:02d}.{now.day:02d} 星期{weekday}")
