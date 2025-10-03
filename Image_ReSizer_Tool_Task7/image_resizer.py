import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), output_format='JPEG'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img = img.convert('RGB')
                img = img.resize(size, Image.Resampling.LANCZOS)
                base, _ = os.path.splitext(filename)
                out_file = os.path.join(output_folder, f"{base}.{output_format.lower()}")
                img.save(out_file, output_format)
                print(f"Saved: {out_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Batch resize and convert images.")
    parser.add_argument('input_folder', help='Folder with original images')
    parser.add_argument('output_folder', help='Folder to save resized images')
    parser.add_argument('--width', type=int, default=800, help='Width of resized images')
    parser.add_argument('--height', type=int, default=800, help='Height of resized images')
    parser.add_argument('--format', type=str, default='JPEG', help='Output image format (JPEG, PNG, etc.)')
    args = parser.parse_args()
    resize_images(args.input_folder, args.output_folder, (args.width, args.height), args.format)
