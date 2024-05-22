import pyqrcode

# Ask user to input the URL
s = input("Enter the URL: ")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the SVG file named "myQr.svg"
url.svg("myQr.svg", scale=8)
