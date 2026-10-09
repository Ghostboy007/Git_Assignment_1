from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont

# Function to create PDF
def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height - 100, "Git Assignment 1")

    # Student details
    c.setFont("Helvetica", 14)
    c.drawString(100, height - 150, "Name: Utkarsh Vinayak")
    c.drawString(100, height - 180, "Roll No.: 26A129")
    c.drawString(100, height - 210, "Course: MBA (TAPMI, Manipal)")

    # Footer
    c.setFont("Helvetica-Oblique", 12)
    c.drawCentredString(width/2, 50, "Generated using Python ReportLab")

    c.save()
    print(f"{filename} created successfully!")

# Function to create Image
def create_image(filename):
    img = Image.new("RGB", (600, 400), color=(173, 216, 230))  # light blue background
    draw = ImageDraw.Draw(img)

    font_title = ImageFont.load_default()

    # Title
    draw.text((200, 50), "Git Assignment 1", font=font_title, fill="black")

    # Student details
    draw.text((50, 150), "Name: Utkarsh Vinayak", font=font_title, fill="darkblue")
    draw.text((50, 200), "Roll No.: 26A129", font=font_title, fill="darkblue")
    draw.text((50, 250), "Course: MBA (TAPMI, Manipal)", font=font_title, fill="darkblue")

    img.save(filename)
    print(f"{filename} created successfully!")

# Run both functions
create_pdf("report.pdf")
create_image("image.png")




