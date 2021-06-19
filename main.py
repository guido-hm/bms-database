import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import doctors, hospitals, others, resellers

#connecting to SQLite Database using DB Browser for SQLite
con = sql.connect("./data.db")
cur = con.cursor()
statement = "SELECT username, password FROM users"
cur.execute(statement)
print("Usernames and passwords used for testing:")
#remove this print eventually
print(cur.fetchall())

root = tk.Tk()
root.title("Login")
root.geometry("300x400")

class MainWindow:
	def __init__(self, master): # Initializes to the login page

		self.master = master

		self.loginFrame = tk.Frame(master)
		self.loginFrame.place(relwidth=1, relheight=1)

		self.loginLabel = tk.Label(self.loginFrame, font="Calibri 24", text="Login")
		self.loginLabel.pack()

		# Username
		self.usernameLabel = tk.Label(self.loginFrame, font="Calibri 14", text="Username: ")
		self.usernameLabel.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.05)

		self.usernameEntry = tk.Entry(self.loginFrame)
		self.usernameEntry.place(relx=0.4, rely=0.6, relwidth=0.5, relheight=0.05)

		# Password
		self.passwordLabel = tk.Label(self.loginFrame, font="Calibri 14", text="Password: ")
		self.passwordLabel.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.05)

		self.passwordEntry = tk.Entry(self.loginFrame, show="*")
		self.passwordEntry.place(relx=0.4, rely=0.65, relwidth=0.5, relheight=0.05)

		#Login Button
		self.loginButton = tk.Button(self.loginFrame, font="Calibri 14", text="Login", command = lambda: self.Login(self.usernameEntry.get(), self.passwordEntry.get()))
		self.loginButton.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

		#Error Message
		self.ErrorLabel = tk.Label(self.loginFrame, font="Calibri 14", text="")
		self.ErrorLabel.place(relx=0.1, rely=0.9)


	def Login(self, username, password):
		""" Compares the entered password hash to the hash stored in the database.
		If it matches, login is successful."""

		# TODO: Build Function
		#	- Figure out where usernames and passwords will be stored
			#ANSWER: SQLite, I used DBBrowswer for SQLite
			#Followed this tutorial: 
			#https://compucademy.net/user-login-with-python-and-sqlite/
		#	- Add if else statement. If login is successful, DatabaseWindow() is called.
			#DONE
		#	- Else, error window is displayed.
			#DONE

		# Calling DatabaseWindow with no conditional temporarily

		#Verifies user input with stored usernames in Database
		#Not encrypted but should be safe if only used locally

		username = self.usernameEntry.get()
		password = self.passwordEntry.get()
		print(username)
		con = sql.connect("data.db")
		cur = con.cursor()
		statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
		cur.execute(statement)
		if not cur.fetchone():  # An empty result evaluates to False.
		    print("Login failed")
		    self.ErrorLabel.config(text='Wrong Login Information, Try Again.', fg="red")
		else:
		    print("Welcome")
		    self.DatabaseWindow()

	def DatabaseWindow(self):

		self.loginFrame.destroy()

		# Changes the window size
		root.geometry("900x500")

		# Tab Control
		self.tabControl = ttk.Notebook(self.master)
		self.tabControl.pack(expand=1, fill="both")


		# Doctors Tab
		self.doctorsTabFrame = ttk.Frame(self.tabControl)
		self.tabControl.add(self.doctorsTabFrame, text="Doctors")
		self.doctorsTabInfo = doctors.doctorsTab(self.doctorsTabFrame)

		# Hospitals Tab
		self.hospitalsTabFrame = ttk.Frame(self.tabControl)
		self.tabControl.add(self.hospitalsTabFrame, text="Hospitals")
		self.hospitalsTabInfo = hospitals.hospitalsTab(self.hospitalsTabFrame)

		# Others Tab
		self.othersTabFrame = ttk.Frame(self.tabControl)
		self.tabControl.add(self.othersTabFrame, text="Others")
		self.othersTabInfo = others.othersTab(self.othersTabFrame)


		# Resellers Tab
		self.resellersTabFrame = ttk.Frame(self.tabControl)
		self.tabControl.add(self.resellersTabFrame, text="Resellers")
		self.resellersTabInfo = resellers.resellersTab(self.resellersTabFrame)





window = MainWindow(root)
root.mainloop()
