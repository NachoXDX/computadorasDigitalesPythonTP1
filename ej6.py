import os
import sys
from datetime import datetime

d = datetime.today()

if d.minute >= 30:
    os.system("notepad")
    sys.exit()
else:
    sys.exit(1)
