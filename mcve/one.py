from tkinter import *

class One(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		btn_back = Button(self, text="Back", command=self.back_clicked)
		btn_back.grid(row=0, column=0)
		Label(self, text="This is one").grid(row=1, column=0)

	def back_clicked(self):
		self.master.show_frame("MainMenu")
