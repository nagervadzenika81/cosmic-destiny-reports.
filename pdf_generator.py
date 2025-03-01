from fpdf import FPDF

def generate_pdf(name, report_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, report_text)

    filename = f"{name.replace(' ', '_')}_cosmic_report.pdf"
    pdf.output(filename)

    return filename
