# ==================
# QR Code Generate
# ==================

import qrcode

data = input("Enter text/URL for QR Code : " )
img = qrcode.make(data)
img.save("qr.png")

print("QR Code saved as qr.png")