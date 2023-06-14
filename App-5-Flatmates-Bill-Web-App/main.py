from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat
app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        primeiro = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        segundo = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template("bill_form_page.html",
                               result=True
                               billform=billform,
                               name1=primeiro.name,
                               amount1=primeiro.pays(the_bill, segundo),
                               name2=segundo.name,
                               amount2=segundo.pays(the_bill, primeiro))


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data
        flat1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data
        flat2 = billform.name2.data
        days_in_house2 = billform.days_in_house2.data

        the_bill = flat.Bill(float(amount), period)
        primeiro = flat.Flatmate(flat1, float(days_in_house1))
        segundo = flat.Flatmate(flat2, float(days_in_house2))

        return render_template("results.html",
                               name1=primeiro.name,
                               amount1=primeiro.pays(the_bill, segundo),
                               name2=segundo.name,
                               amount2=segundo.pays(the_bill, primeiro))


class BillForm(Form):
    amount = StringField("Preço da conta: ", default=150)
    period = StringField("Período da conta: ", default="Dezembro")

    name1 = StringField("Nome: ", default="Francisco")
    days_in_house1 = StringField("Dias na casa: ", default=12)
    name2 = StringField("Nome: ", default="Felipe")
    days_in_house2 = StringField("Dias na casa: ", default=15)

    button = SubmitField("Enviar")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form/', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/bill_form/results', view_func=ResultsPage.as_view('results_page'))

app.run()
