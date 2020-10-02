# https://techwithtim.net/tutorials/kivy-tutorial/object-properties/
# https://expobrain.net/2010/07/31/simple-event-dispatcher-in-python/
from kiv.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput


class MainLayout(GridLayout):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cols = 1

		self.grid = GridLayout()
		self.grid.cols = 2

		self.add_widget(Label(text="First Name"))
		self.first_name = TextInput(multiline = False)
		self.grid.add_widget(self.first_name)

		self.add_widget(Label(text="Last Name"))
		self.last_name = TextInput(multiline = False)
		self.grid.add_widget(self.last_name)

		self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.grid.add_widget(self.email)
        self.add_widget(self.grid)

        self.btn_submit = Button(text="Submit", font_size = 36)
        self.btnSubmit.bind(on_press = pressed)
        self.add_widget(self.btn_submit)


    def pressed(self, instance):
    	name = self.first_name.text
        last = self.last_name.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MainAcitivity(App):
	def build(self):
		return MainLayout()


if __name__ =="__main__":
	MainAcitivity().run()








