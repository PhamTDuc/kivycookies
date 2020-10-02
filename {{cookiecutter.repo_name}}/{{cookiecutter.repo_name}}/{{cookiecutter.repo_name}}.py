from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image


class MyGrid(Widget):
    pass


class MyImage(Image):
    pass


class {{cookiecutter.app_class_name}}(App):
    def build(self):
        return MyGrid()
