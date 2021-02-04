# Some working with tkinter, create a calculator which can add numbers devision
# and more



from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

root = Tk()
root.title("Calculate")

# логика калькулятора 
def calc(key):
	global memory
	if key == "=":
		# excluding letter writing
		str1 = "-+0123456789,*/"
		if calc_entry.get()[0] not in str1:
			calc_entry.insert(END, "Первый символ не число!")
			messagebox.showerror("Ошибка, Введено не число")
 
		try:
			result = eval(calc_entry.get())
			calc_entry.insert(END, "=" + str(result))
			#or
			# calc_entry.delete(0, END)
			# calc_entry.insert(END, result)

		except: 
			calc_entry.insert(END, "Ошибка!")
			messagebox.showerror("Ошибка, Проверь правильность данных!")
			calc_entry.delete(0, END)

#clear field
	elif key == "AC":
		calc_entry.delete(0, END)		

# replace
	elif key == "-/+":
		if "=" in calc_entry.get():
			calc_entry.delete(0, END)
		try: 
			if calc_entry.get()[0] == "-":
				calc_entry.delete(0)
			else:
				calc_entry.insert(0, "-")
		except IndexError:
			pass
	else:
		if "=" in calc_entry.get():
			calc_entry.delete(0, END)
		calc_entry.insert(END, key)


# create buttoms of calculate
bttn_list = [

	"AC", "+/-", "%", "/",
	"7", "8",  "9", "*",
	"4", "5", "6", "-",
	"1", "2", "3", "+",
	"0", ",", " ", "="

]

r = 1
c = 0

for i in bttn_list:
	rel = ""
	cmd = lambda x=i: calc(x)
	ttk.Button(root, text=i, command = cmd).grid(row=r, column=c)
	c += 1
	if c > 3:
		c = 0
		r += 1

#entry
calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan = 5)



root.mainloop()