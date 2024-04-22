from fpdf import FPDF


class Shirtificate(FPDF):
	def __init__(self, name):
		super().__init__()
		self.add_page()
		self.set_margins(left=10, top=15, right=10)
		# Set font size and colour
		self.set_font("helvetica", style="B", size=40)
		self.set_font_size(25)
		self.set_text_color(255, 255, 255)
		# Align the text on the image
		self.cell(0, 60, text = "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="CENTER")
		self.image("shirtificate.png", w=self.epw)
		self.text(x=50, y=140, text=(f"{name} took CS50"))

# Ask for a name and output the image
shirtificate = Shirtificate(input("Name: "))
shirtificate.output("shirtificate.pdf")
