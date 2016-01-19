from tkinter import *
import time, random

timer = 0
i = 0

def results(self):
	global btnOne, btnTwo, timer, buttons, size, i
	if i == 5:
		return 0
	if timer != 0:
		newTime = time.time() - timer
		yValue = random.randint(0, 720-190)
		btnOne.place(x=0, y=yValue)
		btnTwo.place(x=660, y=yValue)
		print(newTime)
		timer = 0
		i = i+1
	else:
		timer = time.time()

		

if __name__=="__main__":
	gui = Tk()
	gui.geometry('720x720')
	gui.title('Fitts\' Law Test')

	buttons = ['control.png', '80.png', '110.png', '140.png', '190.png']
	size = [50, 80, 110, 140, 190]

	yValue = random.randint(0, 720-190)

	btnPhoto = PhotoImage(file = buttons[1])
	btnOne = Label(gui, image=btnPhoto)
	btnTwo = Label(gui, image=btnPhoto)
	btnOne.bind('<Button-1>', results)
	btnTwo.bind('<Button-1>', results)
	btnOne.place(x=0, y=yValue)
	btnTwo.place(x=660, y=yValue)

	gui.mainloop()