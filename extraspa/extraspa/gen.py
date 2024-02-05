import qrcode
from PIL import Image
from io import BytesIO
from base64 import b64encode

# Define the QR code URL
qr_code_url = r"C:\Users\Collins\Desktop\jobs\Extraspa\extraspa\extraspa\static\mysite\images\qr_code.png"

# Define the pizza image path
pizza_image_path = r"C:\Users\Collins\Desktop\cardd.jpg"

# Open the pizza image
pizza_image = Image.open(pizza_image_path)

# Get the image dimensions
pizza_width, pizza_height = pizza_image.size

# Calculate the center coordinates
center_x = pizza_width * 0.5
center_y = pizza_height * 0.5

# Calculate the right offset
right_offset = pizza_width * 0.25

# Generate the QR code image
qr_code = qrcode.make(qr_code_url)
qr_code = qr_code.resize((200, 200))

# Create a blank image for the combined image
combined_image = Image.new("RGB", (pizza_width, pizza_height))

# Paste the pizza image onto the combined image
combined_image.paste(pizza_image, (0, 0))

# Adjust the position of the QR code
qr_x_offset = int(center_x + right_offset - qr_code.size[0] / 2) +40  # Adjusted x-coordinate
qr_y_offset = int(center_y - qr_code.size[1] / 0.8)

# Paste the QR code image onto the combined image
combined_image.paste(qr_code, (qr_x_offset, qr_y_offset))

# Save the combined image
combined_image.save("combined_image.png")

# Convert the combined image to base64 encoded string
with open("combined_image.png", "rb") as image_file:
    combined_image_bytes = image_file.read()
    combined_image_base64 = b64encode(combined_image_bytes).decode("utf-8")

# Display the combined image to the user
image = Image.open(BytesIO(combined_image_bytes))
image.show()

print("Combined image base64 encoded string:")
