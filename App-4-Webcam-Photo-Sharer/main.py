from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

import time
import webbrowser

from filesharer import FileSharer

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    # Botão de "ligar" a camera, alterando a sua opacidade para 1, o play
    # para Verdadeiro, o texto do botão para "Parar camera" e para pegar
    # a textura da camera de novo.
    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        # Botão de "desligar" a camera, alterando a sua opacidade para 0, o
        # play para Falso, o texto do botão para "Ligar camera" e parar
        # de pegar a textura da camera.
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        # Pega o último frame da camera e transforma em um png com o nome da
        # data atual junto ao horário e, simultaneamente, enviando a imagem
        # e o usuario para a outra tela.
        filename = time.strftime('%d_%m_%Y-%H_%M_%S')
        self.filepath = f".\\files\\{filename}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        # Diferente do self.ids.(id).(oque mudar) que altera da atual
        # classe(CameraScreen) o self.manager.current_screen.ids.(id).(oque mudar)
        # altera onde o usuário está olhando.
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = "Create a Link First!"

    def create_link(self):
        # Pega o caminho da imagem da outra tela(camera_screen) na variável
        # filepath, após isso utiliza a classe FileSharer para enviar o caminho
        # e criar uma url com a imagem na núvem e por fim alterando o texto da
        # label para a url criada.
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        # Tenta copiar a url, se ainda não tenha sido criada através do
        # criar url, ele irá trocar o texto da label para "Crie uma URL primeiro"
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        # Tenta abrir a url, se ainda não tenha sido criada através do
        # criar url, ele irá trocar o texto da label para "Crie uma URL primeiro"
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
