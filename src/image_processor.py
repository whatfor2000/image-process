import os
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(width, height, output_path, format):
    """
    Creates an image with specified dimensions, a gray background, and centered text displaying the dimensions.
    
    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        output_path (str): Path to save the generated image.
        format (str): Format to save the image (e.g., "webp").
    """
    image = Image.new("RGB", (width, height), color=(169, 169, 169))
    draw = ImageDraw.Draw(image)
    text = f"{width} x {height}"
    font_size = min(width, height) // 10
    
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill="white")
    image.save(output_path, format=format.upper())

def process_images_in_folder(input_folder, output_folder, format):
    """
    Processes all images with the specified format in a folder, creating a new image with dimensions text.
    
    Args:
        input_folder (str): Folder with original images.
        output_folder (str): Folder to save generated images.
        format (str): Image format to process (e.g., "webp").
    """
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith("." + format.lower()):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                width, height = img.size
            output_path = os.path.join(output_folder, filename)
            create_image_with_text(width, height, output_path, format)
            print(f"Generated: {output_path}")
