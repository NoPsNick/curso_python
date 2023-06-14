from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file("frontend.kv")


class FirstScreen(Screen):

    def search_image(self):
        # Pegando o que foi escrito no TextInput
        query = self.manager.current_screen.ids.user_query.text

        # Pesquisando a página no wikipedia pesquisada e transformando a primeira imagem
        page = wikipedia.page(query)
        image_link = page.images[0]
        req = requests.get(image_link)
        link = ".\\images\\image.jpg"
        with open(link, 'wb') as file:
            file.write(req.content)

        # Adicionando a imagem na tela atual com o id img manager.current_screen.ids.(ids).(oq mudar)...
        self.manager.current_screen.ids.img.source = link


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
