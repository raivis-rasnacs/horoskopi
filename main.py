import fpdf
import random
import datetime

zimes = ["Auns", "Vērsis", "Dvīņi", "Vēzis", "Lauva", "Jaunava", "Svari", "Skorpions", "Strēlnieks", "Mežāzis", "Ūdensvīrs", "Zivis"]
apgalvojumi = []
rikojumi = []

fails = open("apgalvojumi.txt", "r")
elements = 0
for rinda in fails:
  apgalvojumi.append(rinda.strip())
  elements += 1
fails.close()

fails = open("rikojumi.txt", "r")
elements = 0
for rinda in fails:
  rikojumi.append(rinda.strip())
  elements += 1
fails.close()

pdf = fpdf.FPDF()
pdf.add_page()
pdf.add_font("Arial", "", "Arial.ttf", uni=True)
pdf.set_font("Arial", size = 14)
pdf.cell(0, 10, ln=2, txt = str(datetime.date.today()))

for zime in zimes:
  pdf.cell(0, 10, ln=2, txt = zime)
  pdf.multi_cell(0, 10, txt = random.choice(apgalvojumi)+" "+random.choice(apgalvojumi)+" "+random.choice(apgalvojumi)+" "+random.choice(rikojumi))

pdf.output("horoskopi.pdf", "F")