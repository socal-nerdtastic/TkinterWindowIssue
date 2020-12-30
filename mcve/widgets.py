from tkinter import *


# JUST SET THE GEOMETRY SIMILAR TO THE TIMERAPP


class Widgets(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		


		btn_back = Button(self, text="Back", command=self.back_clicked)
		Label(self, text="This is the widgets frame").grid(row=0,column=1)
		btn_back.grid(row=0, column=0)

		self.frame_data = Frame(self)
		self.frame_data.grid(row=1, column=0)

		self.rows = []

		self.random_widgets()


	def back_clicked(self):
		self.controller.show_frame("MainMenu")

	def random_widgets(self):
		for i in range(5):
			row = self.create_row()
			self.draw_row(row)
			self.rows.append(row)

	def create_row(self):
		frame = Frame(self.frame_data)
		e_name = Entry(frame)
		e_goal_time = Entry(frame)
		e_time_completed = Entry(frame)
		e_time_remaining = Entry(frame)

		e_name.grid(row=0, column=0)
		e_goal_time.grid(row=0, column=1)
		e_time_completed.grid(row=0, column=2)
		e_time_remaining.grid(row=0, column=3)

		return frame


	def draw_row(self, row):
		row.grid(row=len(self.rows), column=0)


	def reset(self):
		# self.controller.geometry("")
		pass
		

