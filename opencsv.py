#OCAMPO, EDBERT
#TIAMSIM, MARLENE
#FACE RECOGNITION SYSTEM

#openccsv.py file
from tkinter import Tk, Frame, TOP, Scrollbar, HORIZONTAL, VERTICAL, RIGHT, Y, BOTTOM, X, W, NO
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
root.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')
root.configure(bg='black')
width = 1000
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(root, width=550)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("ID", "Employee", "Time", "Clock", "Date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Employee', text="Employee", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.heading('Clock', text="Clock", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('Attendance.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        id = row['id']
        name = row['name']
        time  = row['time']
        clock = row['clock']
        date = row['date']
        tree.insert("", 0, values=(id, name, time, clock, date))

#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()
    root.title('Time-in Window')