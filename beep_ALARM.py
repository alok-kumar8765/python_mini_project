# =========================
# Interactive Beep Alarm
# =========================

import winsound, time

t = int(input("Seconds to wait :"))
time.spleep(t)

for i in range(3):
    winsound.Beep(1000, 300)

print("Alarm Finished!")

# =========
# Output
# =========

Seconds to wait : 15
Alarm Finished!
























