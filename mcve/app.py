from tkinter import *
from one import One
from two import Two
from widgets import Widgets
from mainmenu import MainMenu

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		self.resizable(False, False)
		self.frames = {}
		self.current_frame = None

		for gui_class in (MainMenu, One, Two, Widgets):
			frame = gui_class(self)
			self.frames[gui_class.__name__] = frame
		self.show_frame("MainMenu")

	def show_frame(self, gui_class):
		if self.current_frame: self.current_frame.grid_forget()
		self.current_frame = self.frames[gui_class]
		self.current_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

def main():
	app = App()
	app.mainloop()

if __name__ == '__main__':
	main()
