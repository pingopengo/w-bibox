import os
import img2pdf

path = '/Users/pingopengo/Code/PyCharm/w-bibox/output/ItBerufe1012'

def combine_images_to_pdf(directory, output_filename):
    # Get list of all PNG files in the directory
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    png_files = [f for f in all_files if f.lower().endswith('.png')]

    # Sort the files to ensure they are in order
    png_files.sort(
        key=lambda x: int(x.split("_")[1].split(".")[0]))  # Assuming filenames are of the format "page_X.png"

    # Create a list of full file paths for img2pdf
    full_file_paths = [os.path.join(directory, f) for f in png_files]

    # Convert PNGs to PDF
    try:
        with open(output_filename, "wb") as f:
            f.write(img2pdf.convert(full_file_paths))
    except Exception as e:
        print(f"Error generating PDF: {e}")

combine_images_to_pdf(path, "../output/IT Berufe LF 10-12.pdf")

