import sys
from datetime import datetime

d = datetime.today()
print(f"{d.day:02}/{d.month:02}/{d.year}")
print(f"{d.hour:02}:{d.minute:02}:{d.second:02}")
sys.exit()