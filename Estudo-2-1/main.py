from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

from scraps import Scrap
from noticias import Noticias

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html',
                               beaultifulsoup=Scrap.beaultifulsoup_tipos[0],
                               extractor=Scrap.extractor_tipos[0],
                               scrapy=Scrap.scrapy_tipos[0],
                               bs=Scrap.beaultifulsoup_tipos[1],
                               ext=Scrap.extractor_tipos[1],
                               scr=Scrap.scrapy_tipos[1])


class CaloriesFormPage(MethodView):

    def get(self):
        scrap_form = ScrapForm()

        return render_template('scrap_form_page.html',
                               beaultifulsoup=Scrap.beaultifulsoup_tipos[0],
                               extractor=Scrap.extractor_tipos[0],
                               scrapy=Scrap.scrapy_tipos[0],
                               bs=Scrap.beaultifulsoup_tipos[1],
                               ext=Scrap.extractor_tipos[1],
                               scr=Scrap.scrapy_tipos[1],
                               scrapform=scrap_form)

    def post(self):
        scrap_form = ScrapForm(request.form)
        noticias = Scrap(str(scrap_form.tipo.data)).get()

        return render_template('scrap_form_page.html',
                               result=True,
                               noticias=noticias,
                               beaultifulsoup=Scrap.beaultifulsoup_tipos[0],
                               extractor=Scrap.extractor_tipos[0],
                               scrapy=Scrap.scrapy_tipos[0],
                               bs=Scrap.beaultifulsoup_tipos[1],
                               ext=Scrap.extractor_tipos[1],
                               scr=Scrap.scrapy_tipos[1],
                               scrapform=scrap_form
                               )


class ScrapForm(Form):
    tipo = StringField("Forma de busca: ", default=Scrap.beaultifulsoup_tipos[0])
    button = SubmitField("Buscar")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/scrap_form',
                 view_func=CaloriesFormPage.as_view('scrap_form_page'))

app.run(debug=True)