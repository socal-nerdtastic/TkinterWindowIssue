from tkinter import *


class MainMenu(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		btn1 = Button(self, text="One", command=self.one_clicked)
		btn2 = Button(self, text="Two", command=self.two_clicked)
		btnw = Button(self, text="Widgets", command=self.widgets_clicked)


		btn1.grid(row=0, column=0)
		btn2.grid(row=1, column=0)
		btnw.grid(row=2, column=0)


	def one_clicked(self):
		self.controller.show_frame("One")


	def two_clicked(self):
		self.controller.show_frame("Two")

	def widgets_clicked(self):
		self.controller.show_frame("Widgets")


	def reset(self):
		self.controller.geometry("200x400")



