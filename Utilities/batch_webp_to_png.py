import os
import argparse
from PIL import Image

def convert_webp_to_png(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    # Iterate through each file in the directory
    for file in files:
        if file.endswith('.webp'):
            # Open the WebP file
            with Image.open(os.path.join(input_dir, file)) as img:
                # Convert the image to PNG format
                png_filename = os.path.splitext(file)[0] + '.png'
                # Save the PNG file to the output directory
                img.save(os.path.join(output_dir, png_filename), 'PNG')

def main():
    parser = argparse.ArgumentParser(description='Convert WebP files to PNG files')
    parser.add_argument('input_dir', help='Input directory containing WebP files')
    parser.add_argument('output_dir', help='Output directory to save PNG files')

    args = parser.parse_args()

    convert_webp_to_png(args.input_dir, args.output_dir)
    print("Conversion completed!")

if __name__ == "__main__":
    main()
