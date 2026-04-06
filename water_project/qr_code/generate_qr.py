import qrcode

# This URL should be your Django server URL
url = "http://127.0.0.1:8000/"

# Create QR code
img = qrcode.make(url)

# Save QR code image
img.save("qr.png")

print("QR Code Generated Successfully!")