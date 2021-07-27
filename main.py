import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
import hashlib
# import os.path
from PIL import ImageTk, Image
import doctors, hospitals, others, resellers, companies
import psycopg2

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

		# Login Button
		self.loginButton = tk.Button(self.loginFrame, font="Calibri 14", text="Login", command = lambda: self.Login(self.usernameEntry.get(), self.passwordEntry.get()))
		self.loginButton.place(relx=0.28, rely=0.75, relwidth=0.44, relheight=0.1)

		self.CreateAccountButton = tk.Button(self.loginFrame, font="Calibri 14", text="Create Account", command = self.CreateAccountWindow)
		self.CreateAccountButton.place(relx=0.28, rely=0.86, relwidth=0.44, relheight=0.1)

		# Images 
		self.image1 = Image.open("logo2.png")
		self.resized_image = self.image1.resize((150, 150))
		self.test = ImageTk.PhotoImage(self.resized_image)

		self.label1 = tk.Label(image=self.test)
		self.label1.place(relx=0.25, rely=0.15)

		# Calls function to connect to login database
		print("Heyo")
		self.ConnectToLoginDatabase()
		print("Heyo2")

	def Login(self, username, password):
		""" Compares the entered password hash to the hash stored in the database.
		If it matches, login is successful."""

		#Verifies user input with stored usernames in Database
		#Not encrypted but should be safe if only used locally

		# Gets username from entrybox
		username = self.usernameEntry.get()

		# Gets password from entrybox and hashes it before saving it to a variable
		password = hashlib.sha256(self.passwordEntry.get().encode()).hexdigest()

		# Gets if there is any DB with given username and given password (hashed, of course)
		statement = f"SELECT username from DBuser WHERE username='{username}' AND password = '{password}'"
		self.cur_login.execute(statement)

		if self.cur_login.fetchone():
			print("Welcome")
			self.cur_login.close()
			self.conn_login.close()
			self.DatabaseMainWindow()
		else:
			print("Login failed")
			self.usernameEntry.delete(0, "end")
			self.passwordEntry.delete(0, "end")

	def CreateAccountWindow(self):
		self.newAccountWindow = tk.Toplevel()
		self.newAccountWindow.title("New Account")
		self.newAccountWindow.geometry("300x200")

		# Username
		newUsernameLabel = tk.Label(self.newAccountWindow, font="Calibri 14", text="Username: ")
		newUsernameLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

		newUsernameEntry = tk.Entry(self.newAccountWindow)
		newUsernameEntry.place(relx=0.4, rely=0.4, relwidth=0.5, relheight=0.1)

		# Password
		newPasswordLabel = tk.Label(self.newAccountWindow, font="Calibri 14", text="Password: ")
		newPasswordLabel.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1)

		newPasswordEntry = tk.Entry(self.newAccountWindow, show="*")
		newPasswordEntry.place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.1)

		secondNewPasswordLabel = tk.Label(self.newAccountWindow, font="Calibri 14", text="Password: ")
		secondNewPasswordLabel.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)

		secondNewPasswordEntry = tk.Entry(self.newAccountWindow, show="*")
		secondNewPasswordEntry.place(relx=0.4, rely=0.6, relwidth=0.5, relheight=0.1)

		finalizeCreateAccountButton = tk.Button(self.newAccountWindow, text="Create", font="Calibri 14", command=lambda: self.CreateAccount(newUsernameEntry.get(), newPasswordEntry.get(), secondNewPasswordEntry.get()))
		finalizeCreateAccountButton.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.2)

	def CreateAccount(self, username, password, reenteredPassword):
		if password == reenteredPassword:
			password = hashlib.sha256(password.encode()).hexdigest()
			self.cur_login.execute("INSERT INTO DBuser (username, password) VALUES ('{username}', '{password}')".format(username=username, password=password))
			self.conn_login.commit()
			self.newAccountWindow.destroy()
		else:
			print("Passwords do not match")
			password.delete(0, "end")
			reenteredPassword.delete(0, "end")

	def refreshOptionMenu(self, event):
		
		selected_tab = event.widget.select()
		tab_text = event.widget.tab(selected_tab, "text")
		print("Selected Tab: ", selected_tab, "     ", tab_text)

		if tab_text == "Doctors":
			self.doctorsTabInfo.refreshOptionMenu()
			print("docs")
		elif tab_text == "Hospitals":
			self.hospitalsTabInfo.refreshOptionMenu()
			print("hospitals")
		elif tab_text == "Others":
			self.othersTabInfo.refreshOptionMenu()
			print("others")
		elif tab_text == "Resellers":
			self.resellersTabInfo.refreshOptionMenu()
			print("resellers")
		
		return

	def DatabaseMainWindow(self):

		# Calls function to connect to Main Database
		self.ConnectToMainDatabase()

		self.loginFrame.destroy()

		# Changes the window size
		root.state("zoomed")

		## UNCOMMENT
		# self.ConnectToDatabase()

		# Tab Control
		self.tabControl = ttk.Notebook(self.master)
		self.tabControl.pack(expand=1, fill="both")

		self.tabControl.bind("<<NotebookTabChanged>>", self.refreshOptionMenu)

		# Doctors Tab
		self.doctorsTabFrame = tk.Frame(self.tabControl)
		self.tabControl.add(self.doctorsTabFrame, text="Doctors")
		self.doctorsTabInfo = doctors.DoctorTab(self.doctorsTabFrame, self.cur_main)

		# Hospitals Tab
		self.hospitalsTabFrame = tk.Frame(self.tabControl)
		self.tabControl.add(self.hospitalsTabFrame, text="Hospitals")
		self.hospitalsTabInfo = hospitals.HospitalTab(self.hospitalsTabFrame, self.cur_main)

		# Others Tab
		self.othersTabFrame = tk.Frame(self.tabControl)
		self.tabControl.add(self.othersTabFrame, text="Others")
		self.othersTabInfo = others.OtherTab(self.othersTabFrame, self.cur_main)

		# Resellers Tab
		self.resellersTabFrame = tk.Frame(self.tabControl)
		self.tabControl.add(self.resellersTabFrame, text="Resellers")
		self.resellersTabInfo = resellers.ResellerTab(self.resellersTabFrame, self.cur_main)

		# Companies Tab
		self.companiesTabFrame = tk.Frame(self.tabControl)
		self.tabControl.add(self.companiesTabFrame, text="Companies")
		self.companiesTabInfo = companies.CompanyTab(self.companiesTabFrame, self.cur_main)

	def ConnectToLoginDatabase(self):
		self.conn_login = None

		# In PostgreSQL, default username is 'postgres' and password is 'postgres'.
		# And also there is a default database exist named as 'postgres'.
		# Default host is 'localhost' or '127.0.0.1'
		# And default port is '54322'.
		try:
			self.conn_login = psycopg2.connect(
				user="postgres",
				host="localhost",
				password="hF8$!nfshGAgxPch",
				port=5432)
			self.conn_login.autocommit = True

			print('Default Database connected.')
		except:
			print("Could not connect to Default Database")

		# If default Database Connected
		if self.conn_login != None:
			self.cur_login = self.conn_login.cursor()

			# Check if login database exists
			self.cur_login.execute("SELECT datname FROM pg_database;")

			list_database = self.cur_login.fetchall()
			print(list_database)

			login_database_name = "daddysdata_login"

			if (login_database_name,) in list_database:
				print("SUCCESS: '{}' database already exist".format(login_database_name))
				database_exists = True
			else:
				print("WARNING: '{}' Database does not exist.".format(login_database_name))
				database_exists = False

			# If Login Database did not exist...
			if database_exists == False:
				print("Creating daddysdata login database...")

				# Create Login Database
				self.cur_login.execute("CREATE DATABASE daddysdata_login")

				# Closes Cursor and Login for default database
				self.cur_login.close()
				self.conn_login.close()

				# Connects to daddysdata_login database
				self.conn_login = psycopg2.connect(
					host="localhost",
					user="guido",
					database = "daddysdata_login",
					password ="hF8$!nfshGAgxPch",
					port=5432)
				self.conn_login.autocommit = True

				
				print("Connected to daddysdata_login.")

				# Creates cursor for daddysdata_login database
				self.cur_login = self.conn_login.cursor()


				# Creates DBuser table
				self.cur_login.execute("""CREATE TABLE DBuser (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					username VARCHAR UNIQUE,
					password VARCHAR);""")


			elif database_exists == True:
				# Close cursor and connection of default database
				self.cur_login.close()
				self.conn_login.close()
				
				# Connects to daddysdata_login database
				self.conn_login = psycopg2.connect(
					host="localhost",
					user="guido",
					database = "daddysdata_login",
					password ="hF8$!nfshGAgxPch",
					port=5432)
				self.conn_login.autocommit = True

				print("Connected to daddysdata_login.")
				
				# Creates cursor for daddysdata_login database
				self.cur_login = self.conn_login.cursor()


		return
	def ConnectToMainDatabase(self):
		self.conn_main = None

		# In PostgreSQL, default username is 'postgres' and password is 'postgres'.
		# And also there is a default database exist named as 'postgres'.
		# Default host is 'localhost' or '127.0.0.1'
		# And default port is '54322'.
		try:
			self.conn_main = psycopg2.connect(
				user="postgres",
				host="localhost",
				password="hF8$!nfshGAgxPch",
				port=5432)
			self.conn_main.autocommit = True

			print('2. Default database connected.')
		except:
			print("Could not connect to default database")

		# If connected to default database
		if self.conn_main != None:
			self.cur_main = self.conn_main.cursor()

			self.cur_main.execute("SELECT datname FROM pg_database;")

			list_database = self.cur_main.fetchall()
			print(list_database)

			main_database_name = "daddysdata"

			if (main_database_name,) in list_database:
				print("SUCCESS: '{}' database already exist".format(main_database_name))
				database_exists = True
			else:
				print("WARNING: '{}' Database not exist.".format(main_database_name))
				database_exists = False

			if database_exists == False:
				print("Creating daddysdata database...")

				self.cur_main.execute("CREATE DATABASE daddysdata;")

				# Closes Cursor and Login from default database
				self.cur_main.close()
				self.conn_main.close()

				# Connects to main database
				self.conn_main = psycopg2.connect(
					host="localhost",
					user="guido",
					database = "daddysdata",
					password ="hF8$!nfshGAgxPch",
					port=5432)
				self.conn_main.autocommit = True

				print("Connected to daddysdata.")

				# Creates cursor for main database
				self.cur_main = self.conn_main.cursor()

				self.cur_main.execute("""CREATE TABLE company (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					name VARCHAR,
					phone VARCHAR,
					email VARCHAR,
					city VARCHAR,
					state VARCHAR,
					zipcode VARCHAR,
					notes VARCHAR,
					verified BOOLEAN);""")

				self.cur_main.execute("""CREATE TABLE call_log_company (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					other_id INTEGER,
					caller VARCHAR,
					answerer VARCHAR,
					notes VARCHAR);""")

				self.cur_main.execute("""CREATE TABLE hospital (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					name VARCHAR,
					phone VARCHAR,
					email VARCHAR,
					city VARCHAR,
					state VARCHAR,
					zipcode VARCHAR,
					company_id INTEGER,
					notes VARCHAR,
					verified BOOLEAN,
					CONSTRAINT fk_company FOREIGN KEY(company_id) REFERENCES company(id));""")

				self.cur_main.execute("""CREATE TABLE call_log_hospital (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					other_id INTEGER,
					caller VARCHAR,
					answerer VARCHAR,
					notes VARCHAR);""")

				self.cur_main.execute("""CREATE TABLE doctor (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					first_name VARCHAR,
					last_name VARCHAR,
					phone VARCHAR,
					email VARCHAR,
					speciality VARCHAR,
					gender VARCHAR,
					hospital_id INTEGER,
					company_id INTEGER,
					prefix VARCHAR,
					notes VARCHAR,
					verified BOOLEAN,
					do_not_call BOOLEAN,
					CONSTRAINT fk_hospital FOREIGN KEY(hospital_id) REFERENCES hospital(id),
					CONSTRAINT fk_company FOREIGN KEY(company_id) REFERENCES company(id));""")

				self.cur_main.execute("""CREATE TABLE call_log_doctor (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					other_id INTEGER,
					caller VARCHAR,
					notes VARCHAR);""")

				self.cur_main.execute("""CREATE TABLE other (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					first_name VARCHAR,
					last_name VARCHAR,
					phone VARCHAR,
					email VARCHAR,
					occupation VARCHAR,
					gender VARCHAR,
					hospital_id INTEGER,
					company_id INTEGER,
					prefix VARCHAR,
					notes VARCHAR,
					verified BOOLEAN,
					do_not_call BOOLEAN,
					CONSTRAINT fk_hospital FOREIGN KEY(hospital_id) REFERENCES hospital(id),
					CONSTRAINT fk_company FOREIGN KEY(company_id) REFERENCES company(id));""")
				
				self.cur_main.execute("""CREATE TABLE call_log_other (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					other_id INTEGER,
					caller VARCHAR,
					notes VARCHAR);""")

				self.cur_main.execute("""CREATE TABLE company_hospital (
					hospital_id INTEGER,
					company_id INTEGER,
					CONSTRAINT fk_hospital FOREIGN KEY(hospital_id) REFERENCES hospital(id),
					CONSTRAINT fk_company FOREIGN KEY(company_id) REFERENCES company(id));""")

				self.cur_main.execute("""CREATE TABLE reseller (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					first_name VARCHAR,
					last_name VARCHAR,
					phone VARCHAR,
					email VARCHAR,
					gender VARCHAR,
					company_id INTEGER,
					prefix VARCHAR, 
					notes VARCHAR,
					verified BOOLEAN,
					CONSTRAINT fk_company FOREIGN KEY(company_id) REFERENCES company(id));""")

				self.cur_main.execute("""CREATE TABLE call_log_reseller (
					id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
					other_id INTEGER,
					caller VARCHAR,
					notes VARCHAR);""")

				print("daddysdata database created.")

			else:
				self.cur_main.close()
				self.conn_main.close()

				# Connects to main database
				self.conn_main = psycopg2.connect(
					host="localhost",
					user="guido",
					database = "daddysdata",
					password ="hF8$!nfshGAgxPch",
					port=5432)
				self.conn_main.autocommit = True

				print("Connected to daddysdata.")

				# Creates cursor for main database
				self.cur_main = self.conn_main.cursor()


root = tk.Tk()
root.title("Login")
root.geometry("300x400")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window = MainWindow(root)
root.mainloop()


# Filter for Speciality
# Add a call log
# Email Blast