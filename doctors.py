import tkinter as tk
from tkinter.constants import FIRST

class DoctorTab:
	def __init__(self, tabFrame, cursor):

		self.cur_main = cursor
		self.tabFrame = tabFrame

		#Create Labels
		self.firstName = tk.Label(tabFrame, text="First Name:")
		self.lastName = tk.Label(tabFrame, text="Last Name:")
		self.phone = tk.Label(tabFrame, text="Phone:")
		self.email = tk.Label(tabFrame, text="Email:")
		self.specialty = tk.Label(tabFrame, text="Specialty:")
		self.gender = tk.Label(tabFrame, text="Gender:")
		self.hospital = tk.Label(tabFrame, text="Hospital:")
		self.company = tk.Label(tabFrame, text="Company:")

		#Create Entrys
		self.firstNameEntry = tk.Entry(tabFrame)
		self.lastNameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.specialtyEntry = tk.Entry(tabFrame)
		self.genderEntry = tk.Entry(tabFrame)

		# Creates hospital and company optionmenu
		self.createOptionMenu()

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH", command = self.searchDatabase)
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ", command = lambda: self.addItem(self.firstNameEntry, self.lastNameEntry, self.phoneEntry, self.emailEntry, self.specialtyEntry, self.genderEntry, self.hospitalVar, self.companyVar))
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.firstName.grid(row=0, column=0, padx=5, pady=5)
		self.firstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.lastName.grid(row=1, column=0, padx=5, pady=5)
		self.lastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		self.phone.grid(row=2, column=0, padx=5, pady=5)
		self.phoneEntry.grid(row=2, column=1, padx=15, pady=5)

		self.email.grid(row=3, column=0, padx=5, pady=5)
		self.emailEntry.grid(row=3, column=1, padx=15, pady=5)

		self.specialty.grid(row=4, column=0, padx=5, pady=5)
		self.specialtyEntry.grid(row=4, column=1, padx=15, pady=5)

		self.gender.grid(row=5, column=0, padx=5, pady=5)
		self.genderEntry.grid(row=5, column=1, padx=15, pady=5)

		self.hospital.grid(row=6, column=0, padx=5, pady=5)

		self.company.grid(row=7, column=0, padx=15, pady=5)

		self.buttonSearch.grid(row=8, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=8, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=8, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = DoctorInfoViewer(tabFrame, self.cur_main)

	def createOptionMenu(self):
		print("We are creating things!!!!")
		# Creates list of companies for Optionmenu
		companyList = [None]
		self.cur_main.execute("SELECT id || ' ' || name FROM company")
		id_company_pair = self.cur_main.fetchall()
		for id_company in id_company_pair:
			companyList.append(id_company[0])

		# Creates company Optionmenu Variable
		self.companyVar = tk.StringVar(self.tabFrame)
		self.companyVar.set(None)
		self.companyOptionMenu = tk.OptionMenu(self.tabFrame, self.companyVar, *companyList)

		# Places company Optionmenu
		self.companyOptionMenu.grid(row=7, column=1, padx=15, pady=5)



		# Create list of hospitals for Optionmenu
		hospitalList = [None]
		self.cur_main.execute("SELECT id || ' ' || name FROM hospital")
		id_hospital_pair = self.cur_main.fetchall()
		for id_hospital in id_hospital_pair:
			hospitalList.append(id_hospital[0])

		# Creates hospital Optionmenu Variable
		self.hospitalVar = tk.StringVar(self.tabFrame)
		self.hospitalVar.set(None)
		self.hospitalOptionMenu = tk.OptionMenu(self.tabFrame, self.hospitalVar, *hospitalList)

		# Places hospital Optionmenu
		self.hospitalOptionMenu.grid(row=6, column=1, padx=15, pady=5)

	def deleteOptionMenu(self):
		self.hospitalOptionMenu.destroy()
		self.companyOptionMenu.destroy()

	def refreshOptionMenu(self):
		self.deleteOptionMenu()
		self.createOptionMenu()


	def addItem(self, first_name, last_name, phone, email, speciality, gender, hospital, company):
			print("ADDING ITEM...")

			# Checks if user included hospital for doctor
			if hospital.get() == "None":
				processed_hospital_id = None
			else:
				processed_hospital_id = hospital.get().split()[0]
				print("This is my type")
				print(type(processed_hospital_id))
			# Checks if user included company for docotr
			if company.get() == "None":
				processed_company_id = None
			else:
				processed_company_id = company.get().split()[0]


			# Query statement and data to insert hospital info if there is no company on file for it
			insert_query = "INSERT INTO doctor (first_name, last_name, phone, email, speciality, gender, hospital_id, company_id, prefix, notes, verified, do_not_call) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			insert_data = (first_name.get(), last_name.get(), phone.get(), email.get(), speciality.get(), gender.get(), processed_hospital_id, processed_company_id, "Dr.", "", True, False)

			# Execute querty statement with data
			self.cur_main.execute(insert_query, insert_data)

			# Deletes the entry field input to allow new entry
			first_name.delete(0, "end")
			last_name.delete(0, "end")
			phone.delete(0, "end")
			email.delete(0, "end")
			speciality.delete(0, "end")
			gender.delete(0, "end")

			# Sets hospital and company Optionmenu to None to allow new entry
			hospital.set(None)
			company.set(None)

			# Updates the infoViewer with new data
			self.infoViewer.updateListbox("")

	def searchDatabase(self):
		field_data = []
		field_names = ["first_name", "last_name", "phone", "email", "speciality", "gender", "hospital_id", "company_id"]

		# Adds user-inputted info to a list. This will be used to create query used to search for records with given parameters
		field_data.append(self.firstNameEntry.get())
		field_data.append(self.lastNameEntry.get())
		field_data.append(self.phoneEntry.get())
		field_data.append(self.emailEntry.get())
		field_data.append(self.specialtyEntry.get())
		field_data.append(self.genderEntry.get())
		field_data.append(self.hospitalVar.get().split()[0])
		field_data.append(self.companyVar.get().split()[0])

		# Clears entry fields after searching
		self.firstNameEntry.delete(0,'end')
		self.lastNameEntry.delete(0,'end')
		self.phoneEntry.delete(0,'end')
		self.emailEntry.delete(0,'end')
		self.specialtyEntry.delete(0,'end')
		self.genderEntry.delete(0,'end')
		self.hospitalVar.set(None)
		self.companyVar.set(None)

		query_conditions_list = []
		for index in range(len(field_data)):
			if field_data[index] and field_data[index] != "None":
				# If search parameter is a digit (hospital, company ID or any other digit data), it does not user "UPPER" in query"
				if field_data[index].isdigit():
					query_conditions_list.append( f"{field_names[index]} = '{field_data[index]}'")
				else:
					query_conditions_list.append( f"UPPER({field_names[index]}) = UPPER('{field_data[index]}')")
		
		query_conditions_string = " AND ".join(query_conditions_list)
		print(query_conditions_string)

		if query_conditions_string:
			self.infoViewer.updateListbox(query_conditions_string)
		else:
			self.infoViewer.updateListbox("")

		return

	
	def importData():
		return



class DoctorInfoViewer:
	def __init__(self, frame, cursor):

		self.cur_main = cursor

		## Each character of font "consolas 12" takes up 9 pixels. 
		## This info can be used to later create a window that works on any screen size by getting ratios

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)
		
		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		# Creates label for titles
		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<10}|{:<14}|{:<16}|{:<16}|{:<28}|{:<24}|{:<40}'.format("ID", "First Name", "Last Name", "Phone #", "Email", "Specialty", "Hospital"))
		self.titleLabel.place(relwidth=1, relheight=1)

		# Creates frame for info
		self.infoFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.infoFrame.place(rely=0.06, relwidth=1, relheight=0.94)

		# Creates scrollbar
		self.infoScrollbar = tk.Scrollbar(self.infoFrame, orient='vertical')

		# Creates listbox
		self.infoListbox = tk.Listbox(self.infoFrame, font='consolas 12',yscrollcommand = self.infoScrollbar.set)

		# Configures scrollbar
		self.infoScrollbar.config(command=self.infoListbox.yview)

		# Places listbox and scrollbar on screen
		self.infoListbox.place(relwidth=1, relheight=1)
		self.infoScrollbar.pack(side='right', fill='y')

		# Allow double-click and Enter to select
		self.infoListbox.bind('<Double-Button>', lambda x:self.selectItem(self.infoListbox.get('anchor')))
		self.infoListbox.bind('<Return>', lambda x:self.selectItem(self.infoListbox.get('anchor')))

		# Fills infoViewer with info
		self.populateListbox("")

	def populateListbox(self, conditions):

		# TODO: Write function to fill in listbox with doctors data. Everything currently in here is temporary.
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, specialty, hospital))
		
		if conditions:
			populate_query = "SELECT * FROM doctor WHERE " + conditions
		else:
			populate_query = "SELECT * FROM doctor"

		self.cur_main.execute(populate_query)
		doctor_list = self.cur_main.fetchall()

		for doctor in doctor_list:
			id = doctor[0]
			first = self.shortenDisplay(doctor[1], 14)
			last = self.shortenDisplay(doctor[2], 16)
			phone = self.shortenDisplay(doctor[3], 16)
			email = self.shortenDisplay(doctor[4], 28)
			speciality = self.shortenDisplay(doctor[5], 24)
			hospital = self.shortenDisplay(doctor[7], 40)

			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<14} {:<16} {:<16} {:<28} {:<24} {:<40}'.format(id, first, last, phone, email, speciality, hospital))

	
	def deleteListbox(self):
		self.infoListbox.delete(0,'end')
		return

	def updateListbox(self, conditions):
		self.deleteListbox()
		self.populateListbox(conditions)
		return
	

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying doctors data (name, email, notes, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 



	def shortenDisplay(self, string, length):
		'''Given a string and a length, it shortens the word to length,
		   with last three characters being dots (...)'''

		string = str(string)

		if len(string) <= length:
			return string.upper()

		string = string[:length-3]
		string += '...'
		print(string)
		return string.upper()

	