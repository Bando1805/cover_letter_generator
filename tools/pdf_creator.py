from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

def create_pdf_from_text(text, filename, font_size=12, line_spacing=14, margin=50):
    # Create a new PDF canvas
    c = canvas.Canvas(filename, pagesize=letter)

    # Set the font and size
    c.setFont("Helvetica", font_size)

    # Define the starting position on the page
    x, y = margin, letter[1] - margin

    # Split the text into lines
    lines = text.split('\n')

    # Calculate the available width for text
    available_width = letter[0] - 2 * margin

    # Draw each line on the PDF
    for line in lines:
        # Wrap the line if it's too long to fit within the available width
        wrapped_lines = simpleSplit(line, "Helvetica", font_size, available_width)

        for wrapped_line in wrapped_lines:
            c.drawString(x, y, wrapped_line)
            y -= line_spacing

            # Move to a new page if the current page is full
            if y < margin:
                c.showPage()
                y = letter[1] - margin

    # Save the PDF
    c.save()