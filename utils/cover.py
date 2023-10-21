import PyPDF2
import img2pdf


def add_cover_to_pdf(cover_path, existing_pdf_path, output_pdf_path):
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Convert the cover image to PDF using img2pdf
    cover_pdf_path = cover_path.replace('.png', '.pdf')
    with open(cover_pdf_path, 'wb') as f:
        f.write(img2pdf.convert([cover_path]))

    # Add the cover to the PDF writer
    with open(cover_pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        pdf_writer.add_page(pdf_reader.pages[0])  # Updated method

    # Add the pages from the existing PDF to the PDF writer
    with open(existing_pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:  # Updated loop
            pdf_writer.add_page(page)  # Updated method

    # Save the combined PDF
    with open(output_pdf_path, 'wb') as f:
        pdf_writer.write(f)


# Usage example
add_cover_to_pdf("/Users/pingopengo/Code/PyCharm/w-bibox/output/book1/page_1.png",
                 "/Users/pingopengo/Code/PyCharm/w-bibox/output/IT Berufe LF6-9.pdf",
                 "/Users/pingopengo/Code/PyCharm/w-bibox/output/IT Berufe LF6-9_neu.pdf")
