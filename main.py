import tkinter
window=tkinter.Tk()
window.minsize(width=300,height=200)
window.title("Miles to km converter")
label=tkinter.Label(text="Miles to km converter")
label.grid(column=2,row=0)
entry=tkinter.Entry(width=10)
entry.grid(column=2,row=2)
label_miles=tkinter.Label(text="Miles")
label_miles.grid(column=3,row=2)
label3=tkinter.Label(text="Answer is :")
label_answer=tkinter.Label(text="0")
label_answer.grid(column=2,row=3)
label3.grid(column=1,row=3)

def calculate():
	miles=float(entry.get())
	km=miles*float(1.609344)
	label_answer.config(text=round(km))
	

button=tkinter.Button(text="Calculate", command=calculate)
button.grid(column=2,row=4)
