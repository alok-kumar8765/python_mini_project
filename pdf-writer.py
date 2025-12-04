# =======================
# Mini PDF Text Writer 
# =======================

from reportlab.pdfgen import canvas

name = input("PDF name : ")
text = input("Enter text : ")

c = canvas.Canvas(name)
c.setFont("Helvetica", 14)
c.drawString(50, 780, "Your Text : ")
c.drawString(50, 750, text)
c.save()

print("PDF Saved!")