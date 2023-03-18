import pandas as pd
import glob as gl
from fpdf import FPDF
from pathlib import Path


filepaths = gl.glob("resources/*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_fn = filename.capitalize()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=invoice_fn, ln=1)

pdf.output("output.pdf")






