from fpdf import FPDF


class Shirt:
    def __init__(self):
        self.text = self.get_name()

    # get User's name
    @classmethod
    def get_name(cls):
        cls.text = input("Name: ") + " took CS50"
        return (cls.text)

    @classmethod
    def make_pdf(cls):
        # create PDF file, add blank page, disable auto_page_break
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False)
        # add first text
        pdf.set_font("arial", "", 50)
        pdf.cell(40, 70, 'CS50 Shirtificate', align='C', center=True)
        # add external image
        pdf.image(name='shirtificate.png',
                  x=(210/2-180/2),
                  y=(297/2-180/2+20),
                  w=180,
                  h=180,
                  keep_aspect_ratio=True)
        # add second text
        pdf.set_font("arial", "", 25)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(40, 250, f'{cls.text}', align='C', center=True)
        # output PDF file
        pdf.output("shirtificate.pdf")

def main():
    shirtificate = Shirt()
    shirtificate.make_pdf()

if __name__ == "__main__":
    main()
