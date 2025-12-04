# =============================================
# Generate Wi-Fi QR Code Instantly with Python
# =============================================

# ==================================
# pip install wifi_qrcode_generator
# ==================================

import wifi_qrcode_generator.generator 
from PIL import Image

ssid =  "CODING_WIFI"
password = "supersecret123"
security = "WPA"

from wifi_qrcode_generator.generator import wifi_qrcode

qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save("wifi_qr.png")
Image.open("wifi_qr.png")