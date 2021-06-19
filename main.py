import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

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
	def __init__(self, master):
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


	# TODO: Add info-viewer for every tab
	#	- Scrollable widget

	# TODO: Figure out if each tab can be its own class or function

	# Doctors Tab

		self.doctorsTab = ttk.Frame(self.tabControl)
		self.tabControl.add(self.doctorsTab, text="Doctors")

		#Create Labels
		doctorFirstName = tk.Label(self.doctorsTab, text="First Name:")
		doctorLastName = tk.Label(self.doctorsTab, text="Last Name:")
		doctorPhone = tk.Label(self.doctorsTab, text="Phone:")
		doctorEmail = tk.Label(self.doctorsTab, text="Email:")
		doctorSpecialty = tk.Label(self.doctorsTab, text="Specialty:")
		doctorHospital = tk.Label(self.doctorsTab, text="Hospital:")

		#Create Entrys
		doctorFirstNameEntry = tk.Entry(self.doctorsTab)
		doctorLastNameEntry = tk.Entry(self.doctorsTab)
		doctorPhoneEntry = tk.Entry(self.doctorsTab)
		doctorEmailEntry = tk.Entry(self.doctorsTab)
		doctorSpecialtyEntry = tk.Entry(self.doctorsTab)

		# TODO: Change Hospital Entry to a Drop Down Menu
		doctorHospitalEntry = tk.Entry(self.doctorsTab)

		#Create Buttons
		buttonSearch = tk.Button(self.doctorsTab, font="Calibri 12", text="SEARCH")
		buttonAdd = tk.Button(self.doctorsTab, font="Calibri 12", text="  ADD  ")
		buttonImport = tk.Button(self.doctorsTab, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		doctorFirstName.grid(row=0, column=0, padx=5, pady=5)
		doctorFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		doctorLastName.grid(row=1, column=0, padx=5, pady=5)
		doctorLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		doctorPhone.grid(row=2, column=0, padx=5, pady=5)
		doctorPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		doctorEmail.grid(row=3, column=0, padx=5, pady=5)
		doctorEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		doctorSpecialty.grid(row=4, column=0, padx=5, pady=5)
		doctorSpecialtyEntry.grid(row=4, column=1, padx=15, pady=5)

		doctorHospital.grid(row=5, column=0, padx=5, pady=5)
		doctorHospitalEntry.grid(row=5, column=1, padx=15, pady=5)

		buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		buttonImport.grid(row=6, column=2, padx=1, pady=5)



	# Hospitals Tab

		self.hospitalsTab = ttk.Frame(self.tabControl)
		self.tabControl.add(self.hospitalsTab, text="Hospitals")


		#Create Labels
		hospitalName = tk.Label(self.hospitalsTab, text="Name:")
		hospitalPhone = tk.Label(self.hospitalsTab, text="Phone:")
		hospitalEmail = tk.Label(self.hospitalsTab, text="Email:")
		hospitalCity = tk.Label(self.hospitalsTab, text="City:")
		hospitalState = tk.Label(self.hospitalsTab, text="State:")
		hospitalZip = tk.Label(self.hospitalsTab, text="Zip:")

		#Create Entrys
		hospitalNameEntry = tk.Entry(self.hospitalsTab)
		hospitalPhoneEntry = tk.Entry(self.hospitalsTab)
		hospitalEmailEntry = tk.Entry(self.hospitalsTab)
		hospitalCityEntry = tk.Entry(self.hospitalsTab)
		hospitalStateEntry = tk.Entry(self.hospitalsTab)
		hospitalZipEntry = tk.Entry(self.hospitalsTab)

		#Create Buttons
		buttonSearch = tk.Button(self.hospitalsTab, font="Calibri 12", text="SEARCH")
		buttonAdd = tk.Button(self.hospitalsTab, font="Calibri 12", text="  ADD  ")
		buttonImport = tk.Button(self.hospitalsTab, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		hospitalName.grid(row=0, column=0, padx=5, pady=5)
		hospitalNameEntry.grid(row=0, column=1, padx=15, pady=5)

		hospitalPhone.grid(row=1, column=0, padx=5, pady=5)
		hospitalPhoneEntry.grid(row=1, column=1, padx=15, pady=5)

		hospitalEmail.grid(row=2, column=0, padx=5, pady=5)
		hospitalEmailEntry.grid(row=2, column=1, padx=15, pady=5)

		hospitalCity.grid(row=3, column=0, padx=5, pady=5)
		hospitalCityEntry.grid(row=3, column=1, padx=15, pady=5)

		hospitalState.grid(row=4, column=0, padx=5, pady=5)
		hospitalStateEntry.grid(row=4, column=1, padx=15, pady=5)

		hospitalZip.grid(row=5, column=0, padx=1, pady=5)
		hospitalZipEntry.grid(row=5, column=1, padx=1, pady=5)
		

		buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		buttonImport.grid(row=6, column=2, padx=1, pady=5)

	# Others Tab

		self.othersTab = ttk.Frame(self.tabControl)
		self.tabControl.add(self.othersTab, text="Others")

		otherFirstName = tk.Label(self.othersTab, text="First Name:")
		otherLastName = tk.Label(self.othersTab, text="Last Name:")
		otherPhone = tk.Label(self.othersTab, text="Phone:")
		otherEmail = tk.Label(self.othersTab, text="Email:")
		otherOccupation = tk.Label(self.othersTab, text="Specialty:")
		otherHospital = tk.Label(self.othersTab, text="Hospital:")

		#Create Entrys
		otherFirstNameEntry = tk.Entry(self.othersTab)
		otherLastNameEntry = tk.Entry(self.othersTab)
		otherPhoneEntry = tk.Entry(self.othersTab)
		otherEmailEntry = tk.Entry(self.othersTab)
		otherOccupationEntry = tk.Entry(self.othersTab)

		# TODO: Change Hospital Entry to a Drop Down Menu
		otherHospitalEntry = tk.Entry(self.othersTab)

		#Create Buttons
		buttonSearch = tk.Button(self.othersTab, font="Calibri 12", text="SEARCH")
		buttonAdd = tk.Button(self.othersTab, font="Calibri 12", text="  ADD  ")
		buttonImport = tk.Button(self.othersTab, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		otherFirstName.grid(row=0, column=0, padx=5, pady=5)
		otherFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		otherLastName.grid(row=1, column=0, padx=5, pady=5)
		otherLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		otherPhone.grid(row=2, column=0, padx=5, pady=5)
		otherPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		otherEmail.grid(row=3, column=0, padx=5, pady=5)
		otherEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		otherOccupation.grid(row=4, column=0, padx=5, pady=5)
		otherOccupationEntry.grid(row=4, column=1, padx=15, pady=5)

		otherHospital.grid(row=5, column=0, padx=5, pady=5)
		otherHospitalEntry.grid(row=5, column=1, padx=15, pady=5)

		buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		buttonImport.grid(row=6, column=2, padx=1, pady=5)


	# Resellers Tab

		self.resellersTab = ttk.Frame(self.tabControl)
		self.tabControl.add(self.resellersTab, text="Resellers")

		resellerFirstName = tk.Label(self.resellersTab, text="First Name:")
		resellerLastName = tk.Label(self.resellersTab, text="Last Name:")
		resellerPhone = tk.Label(self.resellersTab, text="Phone:")
		resellerEmail = tk.Label(self.resellersTab, text="Email:")

		#Create Entrys
		resellerFirstNameEntry = tk.Entry(self.resellersTab)
		resellerLastNameEntry = tk.Entry(self.resellersTab)
		resellerPhoneEntry = tk.Entry(self.resellersTab)
		resellerEmailEntry = tk.Entry(self.resellersTab)

		#Create Buttons
		buttonSearch = tk.Button(self.resellersTab, font="Calibri 12", text="SEARCH")
		buttonAdd = tk.Button(self.resellersTab, font="Calibri 12", text="  ADD  ")
		buttonImport = tk.Button(self.resellersTab, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		resellerFirstName.grid(row=0, column=0, padx=5, pady=5)
		resellerFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		resellerLastName.grid(row=1, column=0, padx=5, pady=5)
		resellerLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		resellerPhone.grid(row=2, column=0, padx=5, pady=5)
		resellerPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		resellerEmail.grid(row=3, column=0, padx=5, pady=5)
		resellerEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		buttonSearch.grid(row=4, column=0, padx=1, pady=5)
		buttonAdd.grid(row=4, column=1, padx=1, pady=5)
		buttonImport.grid(row=4, column=2, padx=1, pady=5)


		# New frame for database created
		# self.databaseFrame = tk.Frame(self.master)
		# self.databaseFrame.place(relwidth=1, relheight=1)




window = MainWindow(root)
root.mainloop()
