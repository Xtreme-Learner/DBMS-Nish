import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_YEAR = "student_year"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
MEM_DUR = "membership_duration"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_YEAR + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER, " + MEM_DUR + "INTEGER);")

appLabel = tk.Label(root, text="Student Club Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Student:
    studentName = ""
    studentYear = ""
    phoneNumber = 0
    address = ""
    member_duration = 0

    def __init__(self, studentName, studentYear, phoneNumber, address):
        self.studentName = studentName
        self.studentYear = studentYear
        self.phoneNumber = phoneNumber
        self.address = address
        membership_duration = membership_duration

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
yearLabel = tk.Label(root, text="Enter your year", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

membershipLabel = tk.Label(root, text="Enter your membership duration", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
yearEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)
membershipEntry = tk.Entry(root,width=30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
yearEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
membershipEntry.grid(row=5,column=1, padx=(0,10), pady=20)


def takeNameInput():
    global nameEntry, yearEntry, phoneEntry, addressEntry, membershipEntry
    # global username, studentYear, phone, address, membership
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_YEAR, STUDENT_ADDRESS, STUDENT_PHONE, MEM_DUR
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    studentYear = yearEntry.get()
    yearEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    membership = int(membershipEntry.get())
    membershipEntry.delete(0,tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_YEAR + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + "," +
                       MEM_DUR + " ) VALUES ( '"
                       + username + "', '" + studentYear + "', '" +
                       address + "', " + str(phone) + "," + str(membership) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Club Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Sudent Year")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    tree.heading("five",text="Membership Duration")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2], row[3], row[4], row[5]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()



button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
button.grid(row=6, column=0, pady=30)

displayButton = tk.Button(root, text="Display result", command=lambda :destroyRootWindow())
displayButton.grid(row=6, column=1)

root.mainloop()