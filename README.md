# Image Processor

This project processes images in a folder by generating new images with a gray background and text at the center displaying the dimensions of each image.

## Features
- Processes all images of a specified format in a folder.
- Generates a new image with a gray background and centered white text showing dimensions.
- Supports formats supported by Pillow.

## Requirements
- Python 3.x
- `Pillow` library for image processing.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
- Place original images in a folder (e.g., input_folder).
- Use the example_usage.py script or integrate src/image_processor.py functions in your own code.

## Example
Run the example script:
```bash
python example_usage.py
```
This script will process all .webp images in the input_folder folder and save the generated images in the Result folder.

## Project Structure
```bash
project-root/
├── src/
│   ├── image_processor.py   # Core image processing functions
├── README.md                # Project documentation
├── requirements.txt         # List of dependencies
├── .gitignore               # Git ignore file
└── example_usage.py         # Example script to demonstrate usage
```

## Contributing
- Fork the repository.
- Create a feature branch.
- Commit your changes.
- Open a pull request.

