import io
import textwrap
from reportlab.lib.pagesizes import landscape, A6
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import qrcode

def generate_ticket_pdf(registration):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=landscape(A6))

    width, height = landscape(A6)

    # Background color
    p.setFillColorRGB(0.15, 0.17, 0.2)  # Dark background
    p.rect(0, 0, width, height, fill=1)

    # Draw a rounded white rectangle for the center panel
    p.setFillColor(colors.white)
    p.roundRect(55*mm, 7*mm, 85*mm, 42*mm, 5*mm, fill=1)

    # Event image on left
    if registration.event.image:
        try:
            event_img = ImageReader(registration.event.image.path)
            p.drawImage(event_img, 7*mm, 7*mm, width=45*mm, height=42*mm, preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Image load error: {e}")

    # Event info in middle (text wrapping + bold fonts)
    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 10)

    title_lines = textwrap.wrap(registration.event.title, width=25)
    y = 45*mm
    for line in title_lines[:2]:  # Only show first 2 lines
        p.drawString(58*mm, y, line)
        y -= 5*mm

    p.setFont("Helvetica", 9)
    p.drawString(58*mm, y, f"Date: {registration.event.event_date.strftime('%Y-%m-%d')}")
    y -= 5*mm
    full_name = f"{registration.user.first_name} {registration.user.last_name}".strip() or registration.user.username
    p.drawString(58*mm, y, f"User: {full_name}")
    y -= 5*mm
    p.drawString(58*mm, y, f"Ticket ID: {str(registration.ticket_id)[:10]}...")

    # Generate QR Code
    qr = qrcode.make(str(registration.ticket_id))
    qr_img = ImageReader(qr._img)
    p.drawImage(qr_img, 143*mm, 14*mm, width=25*mm, height=25*mm, mask='auto')

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
