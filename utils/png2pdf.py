import os
from PIL import Image


def combine_images_to_pdf(directory, output_filename):
    from PIL import ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    # Get list of all PNG files in the directory
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    png_files = [f for f in all_files if f.lower().endswith('.png')]

    # Sort the files to ensure they are in order
    png_files.sort(
        key=lambda x: int(x.split("_")[1].split(".")[0]))  # Assuming filenames are of the format "page_X.png"

    # Open each image, handle errors, and append to a list
    images = []
    for f in png_files:
        try:
            img = Image.open(os.path.join(directory, f))
            images.append(img)
        except OSError:
            print(f"Error processing image: {f}")

    # Save all images as a single PDF
    if images:
        images[0].save(output_filename, save_all=True, append_images=images[1:])
    else:
        print("No valid images found to combine.")

# Combine images in /output/book1/ to a single PDF
combine_images_to_pdf("../output/book1/", "../output/book_combined.pdf")