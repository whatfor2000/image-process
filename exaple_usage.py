from src.image_processor import process_images_in_folder

# Example usage
input_folder = "input_folder"         # Folder with original images
output_folder = "Result"    # Folder for generated images
format = "webp"             # Format of images to process

process_images_in_folder(input_folder, output_folder, format)
