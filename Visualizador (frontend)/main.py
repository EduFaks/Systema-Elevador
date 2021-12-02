from tkinter import *
from random import randint

root = Tk()
root.title("Elevator Visualizer")
root.geometry("610x585")

#mylabel = Label(root, text="Hello World!")
#mylabel.pack()

elevators = {
    "A": randint(0, 40) * 10,
    "B": randint(0, 40) * 10,
    "C": randint(0, 40) * 10,
    "D": randint(0, 40) * 10,
    "E": randint(0, 40) * 10,
    "F": randint(0, 40) * 10,
    "G": randint(0, 40) * 10,
    "H": randint(0, 40) * 10,
    "I": randint(0, 40) * 10,
    "J": randint(0, 40) * 10
}

def update():
    elevators_update = {
        "A": randint(0, 40) * 10,
        "B": randint(0, 40) * 10,
        "C": randint(0, 40) * 10,
        "D": randint(0, 40) * 10,
        "E": randint(0, 40) * 10,
        "F": randint(0, 40) * 10,
        "G": randint(0, 40) * 10,
        "H": randint(0, 40) * 10,
        "I": randint(0, 40) * 10,
        "J": randint(0, 40) * 10
    }
    count = 0
    for e, h in sorted(elevators_update.items()):
        count += 1
        canvas.move(elevators_rectangle[e], 0, (430 - h) - (430 - elevators[e]))
        elevators[e] = elevators_update[e]
    root.after(1000, update)
    root.update()


def on_click(event):
    floor_input.configure(state=NORMAL)
    floor_input.delete(0, END)


control_frame = LabelFrame(root, text="Controls", padx=5, pady=5)
control_frame.pack(padx=10, pady=10)
floor_input = Entry(control_frame)
floor_input.insert(0, 'andar')
floor_input.bind('<Button-1>', on_click)
floor_input.grid(row=0, column=0)
call_button = Button(control_frame, text="Chamar")
call_button.grid(row=0, column=1)
elevator_answer = Label(control_frame, text="Elevador: ")
elevator_answer.grid(row=1)

elevators_frame = LabelFrame(root, text="Elevators")
elevators_frame.pack(padx=10, pady=10)
canvas = Canvas(elevators_frame, width=590, height=500)
canvas.pack()
count = 0
elevators_rectangle = {}
for e, h in sorted(elevators.items()):
    count += 1
    elevators_rectangle[e] = canvas.create_rectangle((55 * count) + 0,
                                               430 - h, (55 * count) + 10,
                                               440 - h,
                                               fill="purple")
    canvas.create_line((55 * (count-1)) + 33,
                       10,
                       (55 * (count-1)) + 33,
                       600,
                       fill="black")
    canvas.create_text((55 * count) + 5, 18, text=e, font=("Purisa", 14))

for f in range(0, 410, 10):
    canvas.create_line(10, 430 - f, 600, 430 - f, fill="black")
    canvas.create_text(20, 435 - f, text=f / 10, font=("Purisa", 9))

root.after(1000, update)
root.mainloop()
