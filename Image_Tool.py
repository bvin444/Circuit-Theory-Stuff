from PIL import Image

# Resize the image using Pillow
image_path = "/Users/benjaminevincent/Documents/Software/Images/Non-Inverting.png"
image = Image.open(image_path)
image = image.resize((200, 200))  # Adjust the size as needed
resized_image_path = "/Users/benjaminevincent/Documents/Software/Images/resized_Non-Inverting_image3.png"
image.save(resized_image_path)