from tkinter import *

class Two(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		btn_back = Button(self, text="Back", command=self.back_clicked)
		btn_back.grid(row=0, column=0)
		Label(self, text="This is two").grid(row=1, column=0)

	def back_clicked(self):
		self.master.show_frame("MainMenu")

	def reset(self):
		self.controller.geometry("300x300")
