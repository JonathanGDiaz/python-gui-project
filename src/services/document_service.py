from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm, letter, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


class Document():
    def __init__(self) -> None:
        pdfmetrics.registerFont(TTFont("Bold", "fonts/LexendDeca-Bold.ttf"))
        pdfmetrics.registerFont(
            TTFont("Regular", "fonts/LexendDeca-Regular.ttf"))
        pass

    def createTicket(self, contender):
        names = self.__createNameString(contender)
        c = canvas.Canvas(
            f'documents/tickets/{names[1]}', pagesize=(90 * mm, 150*mm))

        image = ImageReader("assets/whiteLogo.png")
        c.drawImage(image, 15, 325, 75, 75)
        c.setFont("Bold", 18)
        c.drawString(90, 335, "Payment ticket")
        c.setFont("Bold", 12)
        c.drawString(20, 300, "Contender name")
        c.drawString(20, 260, "Contender CURP")
        c.drawString(20, 220, "Contender address")
        c.drawString(20, 180, "Tourney category")
        c.drawString(60, 140, "Total amount to pay")

        c.setFont("Regular", 12)
        c.drawString(20, 280, names[0])
        c.drawString(20, 240, contender["curp"])
        c.drawString(20, 200, contender["address"])
        c.drawString(20, 160, contender["category"])
        c.drawString(80, 120, f'{contender["payment"]}')

        c.save()
        return

    def createAppreciationCertificate(self, contender):
        names = self.__createNameString(contender)
        c = canvas.Canvas(
            f'documents/certificates/{names[1]}', pagesize=landscape(letter))

        image = ImageReader("assets/whiteLogo.png")
        c.drawImage(image, 300, 350, 200, 200)
        c.setFont("Bold", 45)
        c.drawString(150, 300, "Appreciation certificate")
        c.setFont("Bold", 25)
        c.drawString(self.__centerX("Thank you for participating!", "Bold", 25, c),
                     250, "Thank you for participating!")

        c.setFont("Regular", 22)
        c.drawString(self.__centerX(names[0],
                                    "Regular", 22, c), 210, names[0])
        c.drawString(self.__centerX("In the intermediate tourney", "Regular",
                                    22, c), 170, "In the intermediate tourney")

        c.rect(50, 50, landscape(letter)[0] - 100, landscape(letter)[1] - 100)
        c.rect(25, 25, landscape(letter)[0] - 50, landscape(letter)[1] - 50)
        c.save()
        return

    def createWinnerCertificate(self, contender, place):
        names = self.__createNameString(contender)
        c = canvas.Canvas(
            f'documents/winners/{names[1]}', pagesize=landscape(letter))

        image = ImageReader("assets/whiteLogo.png")
        c.drawImage(image, 300, 350, 200, 200)

        c.setFont("Bold", 45)
        c.drawString(self.__centerX("Winner certificate",
                     "Bold", 45, c), 300, "Winner certificate")

        c.setFont("Bold", 25)
        c.drawString(self.__centerX(f'Congratulations in obtaining {place}', "Bold", 25, c),
                     250, f'Congratulations in obtaining {place}')

        c.setFont("Regular", 22)
        c.drawString(self.__centerX("In the intermediate tourney", "Regular",
                                    22, c), 210, "In the intermediate tourney")
        c.drawString(self.__centerX(names[0],
                                    "Regular", 22, c), 170, names[0])

        c.rect(50, 50, landscape(letter)[0] - 100, landscape(letter)[1] - 100)
        c.rect(25, 25, landscape(letter)[0] - 50, landscape(letter)[1] - 50)
        c.save()
        return

    def __centerX(self, text, font, size, canvas):
        w = canvas.stringWidth(text, font, size)
        return round((landscape(letter)[0] - w) / 2)

    def __createNameString(self, contender):
        fName = contender["name"]
        fLastName = contender["firstLastName"]
        sLastName = contender["secondLastName"]
        name = f'{fName} {fLastName} {sLastName}'
        pdfName = f'{fName[0].upper()}{fLastName[0].upper()}{sLastName[0].upper()}_{contender["category"]}.pdf'
        return (name, pdfName)
