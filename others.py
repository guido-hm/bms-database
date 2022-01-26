import tkinter as tk

class OtherTab:
	def __init__(self, tabFrame, cursor):

		self.cur_main = cursor
		self.tabFrame = tabFrame

		#Create Labels
		self.firstName = tk.Label(tabFrame, text="First Name:")
		self.lastName = tk.Label(tabFrame, text="Last Name:")
		self.phone = tk.Label(tabFrame, text="Phone:")
		self.email = tk.Label(tabFrame, text="Email:")
		self.occupation = tk.Label(tabFrame, text="Occupation:")
		self.gender = tk.Label(tabFrame, text="Gender:")
		self.hospital = tk.Label(tabFrame, text="Hospital:")
		self.company = tk.Label(tabFrame, text="Company:")

		#Create Entrys
		self.firstNameEntry = tk.Entry(tabFrame)
		self.lastNameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.occupationEntry = tk.Entry(tabFrame)
		self.genderEntry = tk.Entry(tabFrame)

		# Creates company and hospital optionmenu
		self.createOptionMenu()

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH", command=self.searchDatabase)
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ", command = lambda: self.addItem(self.firstNameEntry, self.lastNameEntry, self.phoneEntry, self.emailEntry, self.occupationEntry, self.genderEntry, self.hospitalVar, self.companyVar))
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

		self.occupation.grid(row=4, column=0, padx=5, pady=5)
		self.occupationEntry.grid(row=4, column=1, padx=15, pady=5)

		self.gender.grid(row=5, column=0, padx=5, pady=5)
		self.genderEntry.grid(row=5, column=1, padx=5, pady=5)

		# self.hospital.grid(row=6, column=0, padx=5, pady=5)
		# self.hospitalOptionMenu.grid(row=6, column=1, padx=15, pady=5)

		# self.company.grid(row=7, column=0, padx=5, pady=5)
		# self.companyOptionMenu.grid(row=7, column=1, padx=5, pady=5)

		self.buttonSearch.grid(row=8, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=8, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=8, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = OtherInfoViewer(tabFrame, self.cur_main)

		# Fills listbox with info

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
		self.company.grid(row=7, column=0, padx=5, pady=5)
		self.companyOptionMenu.grid(row=7, column=1, padx=5, pady=5)



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
		self.hospital.grid(row=6, column=0, padx=5, pady=5)
		self.hospitalOptionMenu.grid(row=6, column=1, padx=15, pady=5)



	def deleteOptionMenu(self):
		self.hospitalOptionMenu.destroy()
		self.companyOptionMenu.destroy()

	def refreshOptionMenu(self):
		self.deleteOptionMenu()
		self.createOptionMenu()


	def addItem(self, first_name, last_name, phone, email, occupation, gender, hospital, company):
			print("ADDING ITEM...")

			# Checks if user included hospital for doctor
			if hospital.get() == "None":
				processed_hospital_id = None
			else:
				processed_hospital_id = hospital.get().split()[0]


			# Checks if user included company for doctor
			if company.get() == "None":
				processed_company_id = None
			else:
				processed_company_id = company.get().split()[0]

			# Query statement and data to insert hospital info if there is no company on file for it
			insert_query = "INSERT INTO other (first_name, last_name, phone, email, occupation, gender, hospital_id, company_id, prefix, notes, verified, do_not_call) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			insert_data = (first_name.get(), last_name.get(), phone.get(), email.get(), occupation.get(), gender.get(), processed_hospital_id, processed_company_id, "", "", True, False)

			# Execute querty statement with data
			self.cur_main.execute(insert_query, insert_data)

			# Deletes the entry field input to allow new entry
			first_name.delete(0, "end")
			last_name.delete(0, "end")
			phone.delete(0, "end")
			email.delete(0, "end")
			occupation.delete(0, "end")
			gender.delete(0, "end")

			# Sets hospital and company Optionmenu to None to allow new entry
			hospital.set(None)
			company.set(None)

			# Updates the infoViewer with new data
			self.infoViewer.updateListbox("")


	def searchDatabase(self):
		field_data = []
		field_names = ["first_name", "last_name", "phone", "email", "occupation", "gender", "hospital_id", "company_id"]

		# Adds user-inputted info to a list. This will be used to create query used to search for records with given parameters
		field_data.append(self.firstNameEntry.get())
		field_data.append(self.lastNameEntry.get())
		field_data.append(self.phoneEntry.get())
		field_data.append(self.emailEntry.get())
		field_data.append(self.occupationEntry.get())
		field_data.append(self.genderEntry.get())
		field_data.append(self.hospitalVar.get().split()[0])
		field_data.append(self.companyVar.get().split()[0])

		# Clears entry fields after searching
		self.firstNameEntry.delete(0,'end')
		self.lastNameEntry.delete(0,'end')
		self.phoneEntry.delete(0,'end')
		self.emailEntry.delete(0,'end')
		self.occupationEntry.delete(0,'end')
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

		# self.firstNameEntry, self.lastNameEntry, self.phoneEntry, self.emailEntry, self.specialtyEntry, self.genderEntry, self.hospitalVar, self.companyVar

		return


class OtherInfoViewer:
	def __init__(self, frame, cursor):

		self.cur_main = cursor

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light blue')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<10}|{:<14}|{:<16}|{:<16}|{:<28}|{:<24}|{:<40}'.format("ID", "First Name", "Last Name", "Phone #", "Email", "Occupation", "Hospital"))
		self.titleLabel.place(relwidth=1, relheight=1)

		self.infoFrame = tk.Frame(self.viewerFrame, bg='pink')
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

		self.populateListbox("")

	def populateListbox(self, conditions):

		if conditions:
			populate_query = "SELECT * FROM other WHERE " + conditions
		else:
			populate_query = "SELECT * FROM other"

		self.cur_main.execute(populate_query)
		other_list = self.cur_main.fetchall()

		for other in other_list:
			id = other[0]
			first = self.shortenDisplay(other[1], 14)
			last = self.shortenDisplay(other[2], 16)
			phone = self.shortenDisplay(other[3], 16)
			email = self.shortenDisplay(other[4], 28)
			occupation = self.shortenDisplay(other[5], 24)
			hospital_tuple = self.getHospitalByID(other[7])
			if hospital_tuple is None:
				hospital = "None"
			else:
				hospital = self.shortenDisplay(hospital_tuple[1], 40) 

			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<14} {:<16} {:<16} {:<28} {:<24} {:<40}'.format(id, first, last, phone, email, occupation, hospital))

		return

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
		select_query = f"SELECT * FROM other WHERE id={ID}"
		self.cur_main.execute(select_query)
		selected_item_data = self.cur_main.fetchone()
		
		return selected_item_data

	def selectItem(self, item):

		# Gets Index of selected cell
		current_line_index = self.infoListbox.curselection()
		print("Cur Line: ", current_line_index[0])
		
		# Gets text of cell in index given by current_line_index
		item_text = self.infoListbox.get(current_line_index)

		# Gets ID of item
		ID = self.getSelectedItemsID(item_text)

		# Gets data of selected item using ID
		selected_item_data = self.getSelectedItemData(ID)

		# Creates Toplevel window using data of item selected
		self.data_window = DataWindow(selected_item_data, self.cur_main)


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



	def shortenDisplay(self, string, length):
		'''Given a string and a length, it shortens the word to length,
		   with last three characters being dots (...)'''

		string = str(string)

		if len(string) <= length:
			return string.upper()

		string = string[:length-3]
		string += '...'
		return string.upper()