from fpdf import FPDF
import random
import string
import sqlite3


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            preco = seat.get_price()
            if card.validate(price=preco):
                seat.ocupy()
                ticket = Ticket(user=self, price=preco, seat_number=seat_id)
                ticket.to_pdf()
                return "Compra concluída com sucesso!"
            else:
                return "Ocorreu algum problema com as informações obtidas de seu cartão."
        else:
            return "O assento já está ocupado."


class Seat:

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT "price" FROM "Seat" WHERE "seat_id" = ?""",
                       [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT "taken" FROM "Seat" WHERE "seat_id" = ?""",
                       [self.seat_id])
        result = cursor.fetchall()[0][0]
        if result == 0:
            return True
        else:
            return False

    def ocupy(self):
        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "Seat_id"=?
            """, [1, self.seat_id])
            connection.commit()
            connection.close()


class Card:

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.holder = holder
        self.type = type
        self.number = number
        self.cvc = cvc

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance"=? WHERE "number"=? and "cvc"=?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
            else:
                return False
        else:
            return False


class Ticket:

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Seu bilhete digital", border=1, ln=1, align="C")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Nome: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="ID: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Preço: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Número do assento: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output(name="sample.pdf")


if __name__ == "__main__":
    name = input("Seu nome inteiro: ")
    seat_id = input("Assento preferido: ")
    card_type = input("Tipo do cartão: ")
    card_number = input("Número do cartão: ")
    card_cvc = input("CVC do cartão: ")
    card_holder = input("Nome do dono do cartão: ")

    user = User(name)
    seat = Seat(seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    print(user.buy(seat=seat, card=card))
