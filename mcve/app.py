from tkinter import *
from one import One
from two import Two
from widgets import Widgets
from mainmenu import MainMenu


class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		


		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.resizable(False, False)

		self.frames = {}



		for gui_class in (MainMenu, One, Two, Widgets):
			frame = gui_class(container, self)

			self.frames[gui_class.__name__] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("MainMenu")

	# MIGHT BE PART OF THE ISSUE		
	# def check_is_resizable(self):
	# 	# Check debug state to see if app should be resizable
	# 	if self.debug.get():
	# 		self.resizable(True, True)
	# 	else:
	# 		self.resizable(False, False)



	def show_frame(self, gui_class):
		# self.check_is_resizable()
		frame = self.frames[gui_class]
		# self.change_bindings(gui_class, frame)
		frame.reset()
		frame.tkraise()





def main():
	app = App()
	app.mainloop()

if __name__ == '__main__':
	main()
