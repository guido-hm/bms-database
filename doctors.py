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
			hospital_tuple = self.getHospitalByID(doctor[7])
			if hospital_tuple is None:
				hospital = "None"
			else:
				hospital = self.shortenDisplay(hospital_tuple[1], 40)

			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<14} {:<16} {:<16} {:<28} {:<24} {:<40}'.format(id, first, last, phone, email, speciality, hospital))

	
	def deleteListbox(self):
		self.infoListbox.delete(0,'end')
		return

	def updateListbox(self, conditions):
		self.deleteListbox()
		self.populateListbox(conditions)
		return

	def getSelectedItemsID(self, text):
		selected_id = text.split()[0]
		return selected_id
	
	def getSelectedItemData(self, ID):
		select_query = f"SELECT * FROM doctor WHERE id={ID}"
		self.cur_main.execute(select_query)
		selected_item_data = self.cur_main.fetchone()
		
		return selected_item_data

	def selectItem(self, item):

		# Gets Index of selected cell
		current_line_index = self.infoListbox.curselection()
		
		# Gets text of cell in index given by current_line_index
		item_text = self.infoListbox.get(current_line_index)

		# Gets ID of item
		ID = self.getSelectedItemsID(item_text)

		# Gets data of selected item using ID
		selected_item_data = self.getSelectedItemData(ID)

		# Creates Toplevel window using data of item selected
		self.data_window = DataWindow(selected_item_data, self.cur_main, self)


	def getHospitalByID(self, ID):
		if ID is None:
			return None
		get_hospital_query = f"SELECT * FROM hospital WHERE id={ID}"
		self.cur_main.execute(get_hospital_query)
		hospital = self.cur_main.fetchone()

		return hospital

	def getCompanyByID(self, ID):
		if ID is None:
			return None
		get_company_query = f"SELECT * FROM company WHERE id={ID}"
		self.cur_main.execute(get_company_query)
		company = self.cur_main.fetchone()
		return company

	def shortenDisplay(self, string, length):
		'''Given a string and a length, it shortens the word to length,
		   with last three characters being dots (...)'''

		string = str(string)

		if len(string) <= length:
			return string.upper()

		string = string[:length-3]
		string += '...'
		return string.upper()

	
class DataWindow:
	def __init__(self, data, cursor, main_tab):
		
		self.data = data
		self.cur_main = cursor

		self.main_tab = main_tab

		self.window = tk.Toplevel()
		self.window.state("zoomed")

		self.buttonFrame = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)
		self.infoFrame = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)
		self.notesFrame = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)
		self.callLogFrame = tk.Frame(self.window, highlightbackground="black", highlightthickness=1)

		self.buttonFrame.place(relx=0.025, rely=0.85, relwidth=0.95, relheight=0.1)
		self.infoFrame.place(relx=0.025, rely=0.1, relwidth=0.25, relheight=0.7)
		self.notesFrame.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.7)
		self.callLogFrame.place(relx=0.725, rely=0.1, relwidth=0.25, relheight=0.7)

		##############
		# INFO FRAME #
		##############

		#Create Labels
		self.firstName = tk.Label(self.infoFrame, text="First Name:", font="Calibri 16")
		self.lastName = tk.Label(self.infoFrame, text="Last Name:", font="Calibri 16")
		self.prefix = tk.Label(self.infoFrame, text="Prefix:", font="Calibri 16")
		self.phone = tk.Label(self.infoFrame, text="Phone:", font="Calibri 16")
		self.email = tk.Label(self.infoFrame, text="Email:", font="Calibri 16")
		self.specialty = tk.Label(self.infoFrame, text="Specialty:", font="Calibri 16")
		self.gender = tk.Label(self.infoFrame, text="Gender:", font="Calibri 16")
		self.hospital = tk.Label(self.infoFrame, text="Hospital:", font="Calibri 16")
		self.company = tk.Label(self.infoFrame, text="Company:", font="Calibri 16")

		#Create Entrys
		self.firstNameEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.lastNameEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.prefixEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.phoneEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.emailEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.specialtyEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.genderEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.hospitalEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")
		self.companyEntry = tk.Entry(self.infoFrame, width=20, font="Calibri 16", readonlybackground="#CBCBCB")

		# Fill in Entryboxes
		self.firstNameEntry.insert(0, self.data[1])
		self.lastNameEntry.insert(0, self.data[2])
		self.prefixEntry.insert(0, self.data[9])
		self.phoneEntry.insert(0, self.data[3])
		self.emailEntry.insert(0, self.data[4])
		self.specialtyEntry.insert(0, self.data[5])
		self.genderEntry.insert(0, self.data[6])

		hospital_tuple = self.getHospitalByID(self.data[7])
		if hospital_tuple is None:
			self.hospitalName = "None"
			self.hospitalEntry.insert(0, self.hospitalName)
		else:
			self.hospitalName = hospital_tuple[1]
			self.hospitalEntry.insert(0,self.hospitalName)

		company_tuple = self.getCompanyByID(self.data[8])
		if company_tuple is None:
			self.companyName = "None"
			self.companyEntry.insert(0, self.companyName)
		else:
			self.companyName = company_tuple[1]
			self.companyEntry.insert(0, self.companyName)


		# This variable is used to determine which state all entryboxes are currently in
		# 0 means they are in readonly. 1 means they are editable
		self.stateInfo = 0
		# Set Entries to readonly
		self.firstNameEntry.config(state="readonly")
		self.lastNameEntry.config(state="readonly")
		self.prefixEntry.config(state="readonly")
		self.phoneEntry.config(state="readonly")
		self.emailEntry.config(state="readonly")
		self.specialtyEntry.config(state="readonly")
		self.genderEntry.config(state="readonly")
		self.hospitalEntry.config(state="readonly")
		self.companyEntry.config(state="readonly")

		# Hospital and Company use Entry when in "readonly" mode, but use an Optionmenu when editing. Both are created, but only one is shown at a time
		# When one is placed, the other is hidden. Then they switch when "Toggle Edit" Button is pressed

		# Hospital Optionmenu created
		hospitalList = [None]
		self.cur_main.execute("SELECT id || ' ' || name FROM hospital")
		self.id_hospital_pair = self.cur_main.fetchall()
		for id_hospital in self.id_hospital_pair:
			hospitalList.append(id_hospital[0])

		self.hospitalVar = tk.StringVar(self.infoFrame)
		self.hospitalVar.set(self.hospitalName)
		self.hospitalOptionmenu = tk.OptionMenu(self.infoFrame, self.hospitalVar, *hospitalList)
		self.hospitalOptionmenu.config(width=18)
		self.hospitalOptionmenu.config(font='Calibri 14')


		# Company Optionmenu created
		companyList = [None]
		self.cur_main.execute("SELECT id || ' ' || name FROM company")
		self.id_company_pair = self.cur_main.fetchall()
		for id_company in self.id_company_pair:
			companyList.append(id_company[0])

		self.companyVar = tk.StringVar(self.infoFrame)
		self.companyVar.set(self.companyName)
		self.companyOptionmenu = tk.OptionMenu(self.infoFrame, self.companyVar, *companyList)
		self.companyOptionmenu.config(width=18)
		self.companyOptionmenu.config(font='Calibri 14')


		# Places labels and entries
		self.firstName.grid(row=0, column=0, padx=5, pady=11, sticky="E",)
		self.firstNameEntry.grid(row=0, column=1, padx=5, pady=11)

		self.lastName.grid(row=1, column=0, padx=5, pady=11, sticky="E")
		self.lastNameEntry.grid(row=1, column=1, padx=5, pady=11)

		self.prefix.grid(row=2, column=0, padx=5, pady=11, sticky="E")
		self.prefixEntry.grid(row=2, column=1, padx=5, pady=11, sticky="E")

		self.phone.grid(row=3, column=0, padx=5, pady=11, sticky="E")
		self.phoneEntry.grid(row=3, column=1, padx=5, pady=11)

		self.email.grid(row=4, column=0, padx=5, pady=11, sticky="E")
		self.emailEntry.grid(row=4, column=1, padx=5, pady=11)

		self.specialty.grid(row=5, column=0, padx=5, pady=11, sticky="E")
		self.specialtyEntry.grid(row=5, column=1, padx=5, pady=11)

		self.gender.grid(row=6, column=0, padx=5, pady=11, sticky="E")
		self.genderEntry.grid(row=6, column=1, padx=5, pady=11)

		self.hospital.grid(row=7, column=0, padx=5, pady=11, sticky="E")
		self.hospitalEntry.grid(row=7, column=1, padx=5, pady=11, sticky="E")

		self.company.grid(row=8, column=0, padx=5, pady=11, sticky="E")
		self.companyEntry.grid(row=8, column=1, padx=5, pady=11, sticky="E")

		# Create Buttons
		self.toggleEditInfoButton = tk.Button(self.infoFrame, text="Toggle Edit", font="Calibri 16", bg="light yellow", command=self.toggleInfoEdit)
		# Place Buttons
		self.toggleEditInfoButton.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.08)


		# BUTTON FRAME
		self.closeButton = tk.Button(self.buttonFrame, text="Close", font="Calibri 16", bg="light gray", command=self.closeWindow)
		self.closeButton.place(relx=0, rely=0.05, relwidth=1, relheight=0.9)

		###############
		# NOTES FRAME #
		###############

		# Creates note TextBox and configures it
		self.notesTextBox = tk.Text(self.notesFrame, bg="#CBCBCB")
		self.notesTextBox.insert("end", self.data[10])
		self.stateNotes = 0
		self.notesTextBox.configure(state="disabled")
		self.notesTextBox.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.86)

		# Creates Save Button for Notes
		self.toggleEditNotesButton = tk.Button(self.notesFrame, text="Toggle Edit", font="Calibri 16", bg="light yellow", command = self.toggleNotesEdit)
		self.toggleEditNotesButton.place(relx=0.40, rely=0.9, relwidth=0.2, relheight=0.08)

		# CALL LOG FRAME

	def toggleInfoEdit(self):
		"""This function changes the state of some Entryboxes from 'readonly' to 'normal' and others from 'readonly' to Dropmenues. """
		
		if self.stateInfo == 0:
			self.firstNameEntry.config(state="normal")
			self.lastNameEntry.config(state="normal")
			self.prefixEntry.config(state="normal")
			self.phoneEntry.config(state="normal")
			self.emailEntry.config(state="normal")
			self.specialtyEntry.config(state="normal")
			self.genderEntry.config(state="normal")
			self.hospitalEntry.config(state="normal")
			self.companyEntry.config(state="normal")
			
			self.hospitalEntry.grid_forget()
			self.companyEntry.grid_forget()

			self.hospitalOptionmenu.grid(row=7, column=1, padx=5, pady=11, sticky="E")
			self.companyOptionmenu.grid(row=8, column=1, padx=5, pady=11, sticky="E")

			self.stateInfo = 1
		elif self.stateInfo == 1:

			# Fills company and hospital Entrybox with dropdown menu option chosen

			self.hospitalEntry.delete(0, 'end')
			self.hospitalEntry.insert(0, self.hospitalVar.get())

			self.companyEntry.delete(0, 'end')
			self.companyEntry.insert(0, self.companyVar.get())

			self.firstNameEntry.config(state="readonly")
			self.lastNameEntry.config(state="readonly")
			self.prefixEntry.config(state="readonly")
			self.phoneEntry.config(state="readonly")
			self.emailEntry.config(state="readonly")
			self.specialtyEntry.config(state="readonly")
			self.genderEntry.config(state="readonly")
			self.hospitalEntry.config(state="readonly")
			self.companyEntry.config(state="readonly")

			self.hospitalOptionmenu.grid_forget()
			self.companyOptionmenu.grid_forget()

			self.hospitalEntry.grid(row=7, column=1, padx=5, pady=11, sticky="E")
			self.companyEntry.grid(row=8, column=1, padx=5, pady=11, sticky="E")

			self.stateInfo = 0

		return


	def toggleNotesEdit(self):
		if self.stateNotes == 0:
			self.notesTextBox.config(state = "normal")
			self.notesTextBox.config(bg="white")
			self.stateNotes = 1
		elif self.stateNotes == 1:
			self.notesTextBox.config(state = "disabled")
			self.notesTextBox.config(bg = "#CBCBCB")
			self.stateNotes = 0

		return
	
	def closeWindow(self):
		print("Closing Window")
		self.saveData()
		self.main_tab.updateListbox("")
		self.window.destroy()
		
		return

	def saveData(self):
		"""Checks if any changes were made and saves data if there were changes."""
		print("Testing TESTING:")
		print(self.hospitalVar.get())
		print(type(self.hospitalVar.get()))
		print(self.hospitalName)
		print(type(self.hospitalName))
		
		ID = self.data[0]

		if self.data[1] != self.firstNameEntry.get():
			print("First Name Changed")
			newName = self.firstNameEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET first_name = '{newName}' WHERE id={ID}")
		if self.data[2] != self.lastNameEntry.get():
			print("Last Name Changed")
			newLastName = self.lastNameEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET last_name = '{newLastName}' WHERE id={ID}")
		if self.data[9] != self.prefixEntry.get():
			print("Prefix Changed")
			newPrefix = self.prefixEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET prefix = '{newPrefix}' WHERE id={ID}")
		if self.data[3] != self.phoneEntry.get():
			print("Phone Changed")
			newPhone = self.phoneEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET phone = '{newPhone}' WHERE id={ID}")
		if self.data[4] != self.emailEntry.get():
			print("Email Changed")
			newEmail = self.emailEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET email = '{newEmail}' WHERE id={ID}")
		if self.data[5] != self.specialtyEntry.get():
			print("Specialty Changed")
			newSpecialty = self.specialtyEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET speciality = '{newSpecialty}' WHERE id={ID}")
		if self.data[6] != self.genderEntry.get():
			print("Gender Changed")
			newGender = self.genderEntry.get()
			self.cur_main.execute(f"UPDATE doctor SET gender = '{newGender}' WHERE id={ID}")
		if self.hospitalVar.get() != self.hospitalName:
			print("Hospital Changed")
			if self.hospitalVar.get() == "None":
				newHospital = "None"
			else:
				newHospital = self.hospitalVar.get().split()[0]

			self.cur_main.execute(f"UPDATE doctor SET hospital_id = '{newHospital}' WHERE id={ID}")
		if self.companyVar.get() != self.companyName:
			print("Company Changed")
			if self.companyVar.get() == "None":
				newCompany = "None"
			else:
				newCompany = self.companyVar.get().split()[0]
			
			self.cur_main.execute(f"UPDATE doctor SET company_id = '{newCompany}' WHERE id={ID}")

		if self.data[10] != self.notesTextBox.get("1.0", "end-1c"):
			print("Notes Changed")
			newNotes = self.notesTextBox.get("1.0", "end-1c")
			self.cur_main.execute(f"UPDATE doctor SET notes = '{newNotes}' WHERE id ={ID}")

	def getHospitalByID(self, ID):
		print("ID: ", type(ID))
		if ID is None:
			return None
		get_hospital_query = f"SELECT * FROM hospital WHERE id={ID}"
		self.cur_main.execute(get_hospital_query)
		hospital = self.cur_main.fetchone()
		return hospital

	def getCompanyByID(self, ID):
		if ID is None:
			return None
		get_company_query = f"SELECT * FROM company WHERE id={ID}"
		self.cur_main.execute(get_company_query)
		company = self.cur_main.fetchone()
		return company
