#this is the interface for selecting fastq files and metafile, using kivy3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from functools import partial


from kivy.lang import Builder


class Main(FloatLayout):
    pass

class MyButton(FloatLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print (f.read())

    def selected(self, filename):
        print ("selected: %s" % filename[0])


Builder.load_file("main.kv")

class Complex(App):

    def build(self):
        return Main()


if __name__ == "__main__":
    Complex().run()
