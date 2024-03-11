import calendar
import tkinter as tk

c = calendar.TextCalendar()
m = c.formatmonth(2021, 2)
# help(c)
# print(m)

s = "Life is short\nUse python"
root = tk.Tk()
t = tk.Text(root, height=10, width=30)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
