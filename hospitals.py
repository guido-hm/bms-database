import tkinter as tk

class HospitalTab:
	def __init__(self, tabFrame, cursor):

		self.cur_main = cursor
		self.tabFrame = tabFrame

		#Create Labels
		self.name = tk.Label(tabFrame, text="Name:")
		self.phone = tk.Label(tabFrame, text="Phone:")
		self.email = tk.Label(tabFrame, text="Email:")
		self.city = tk.Label(tabFrame, text="City:")
		self.state = tk.Label(tabFrame, text="State:")
		self.zipcode = tk.Label(tabFrame, text="Zipcode:")
		self.company = tk.Label(tabFrame, text="Company:")

		#Create Entrys
		self.nameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.cityEntry = tk.Entry(tabFrame)
		self.stateEntry = tk.Entry(tabFrame)
		self.zipcodeEntry = tk.Entry(tabFrame)

		# Creates company optionmenu
		self.createOptionMenu()

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH", command=self.searchDatabase)
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ", command=lambda: self.addItem(self.nameEntry, self.phoneEntry, self.emailEntry, self.cityEntry, self.stateEntry, self.zipcodeEntry, self.companyVar))
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.name.grid(row=0, column=0, padx=5, pady=5)
		self.nameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.phone.grid(row=1, column=0, padx=5, pady=5)
		self.phoneEntry.grid(row=1, column=1, padx=15, pady=5)

		self.email.grid(row=2, column=0, padx=5, pady=5)
		self.emailEntry.grid(row=2, column=1, padx=15, pady=5)

		self.city.grid(row=3, column=0, padx=5, pady=5)
		self.cityEntry.grid(row=3, column=1, padx=15, pady=5)

		self.state.grid(row=4, column=0, padx=5, pady=5)
		self.stateEntry.grid(row=4, column=1, padx=15, pady=5)

		self.zipcode.grid(row=5, column=0, padx=1, pady=5)
		self.zipcodeEntry.grid(row=5, column=1, padx=1, pady=5)
		
		# self.company.grid(row=6, column=0, padx=1, pady=5)
		# self.companyOptionMenu.grid(row=6, column=1, padx=1, pady=5)
		
		self.buttonSearch.grid(row=7, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=7, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=7, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = HospitalInfoViewer(tabFrame, self.cur_main)

	def createOptionMenu(self):

		# Create list of hospitals for Optionmenu
		companyList = [None]
		self.cur_main.execute("SELECT id || ' ' || name FROM company")
		id_company_pair = self.cur_main.fetchall()
		for id_company in id_company_pair:
			companyList.append(id_company[0])

		# Creates company Optionmenu Variable
		self.companyVar = tk.StringVar(self.tabFrame)
		self.companyVar.set(None)
		print(type(self.companyVar.get()))
		self.companyOptionMenu = tk.OptionMenu(self.tabFrame, self.companyVar, *companyList)

		# Places company Optionmenu
		self.company.grid(row=6, column=0, padx=1, pady=5)
		self.companyOptionMenu.grid(row=6, column=1, padx=1, pady=5)

	def deleteOptionMenu(self):
		self.companyOptionMenu.destroy()

	def refreshOptionMenu(self):
		self.deleteOptionMenu()
		self.createOptionMenu()

	def addItem(self, name, phone, email, city, state, zipcode, company_id):
		print("ADDING ITEM...")
		# If Company_id is not chosen, it is written as Null in the database.
		# Otherwise, corresponding company_id is written in database.
		if company_id.get() == "None":
			processed_company_id = None
		else:
			processed_company_id = company_id.get().split()[0]
		
		# Query statement and data to insert hospital info if there is no company on file for it
		insert_query = "INSERT INTO hospital (name, phone, email, city, state, zipcode, company_id, notes, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		insert_data = (name.get(), phone.get(), email.get(), city.get(), state.get(), zipcode.get(), processed_company_id, "", True)

		print("DATA TYPES BELOW")

		# Execute querty statement with data
		self.cur_main.execute(insert_query, insert_data)
		

		print("COMPANY ID: ", company_id)
		name.delete(0, "end")
		phone.delete(0, "end")
		email.delete(0, "end")
		city.delete(0, "end")
		state.delete(0, "end")
		zipcode.delete(0, "end")
		company_id.set(None)

		self.cur_main.execute("SELECT * FROM hospital")
		print("Hospitals\n", self.cur_main.fetchall())

		self.infoViewer.updateListbox("")


	def searchDatabase(self):
		field_data = []
		field_names = ["name", "phone", "email", "city", "state", "zipcode", "company_id"]

		# Adds user-inputted info to a list. This will be used to create query used to search for records with given parameters
		field_data.append(self.nameEntry.get())
		field_data.append(self.phoneEntry.get())
		field_data.append(self.emailEntry.get())
		field_data.append(self.cityEntry.get())
		field_data.append(self.stateEntry.get())
		field_data.append(self.zipcodeEntry.get())
		field_data.append(self.companyVar.get().split()[0])

		# Clears entry fields after searching
		self.nameEntry.delete(0,'end')
		self.phoneEntry.delete(0,'end')
		self.emailEntry.delete(0,'end')
		self.cityEntry.delete(0,'end')
		self.stateEntry.delete(0,'end')
		self.zipcodeEntry.delete(0,'end')
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


class HospitalInfoViewer:
	def __init__(self, frame, cursor):

		self.cur_main = cursor

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		# Creates label for titles
		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<10}|{:<40}|{:<16}|{:<28}|{:<24}|{:<16}|{:<12}'.format("ID", "Name", "Phone # ", "Email", "City ", "State", "Zipcode"))
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

		# TODO: Write function to fill in listbox with hospitals data
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, speciality, hospital))
		if conditions:
			populate_query = "SELECT * FROM hospital WHERE " + conditions
		else:
			populate_query = "SELECT * FROM hospital"
		print("POPU QUERY", populate_query)
		self.cur_main.execute(populate_query)
		hospital_list = self.cur_main.fetchall()

		for hospital in hospital_list:
			id = hospital[0]
			name = self.shortenDisplay(hospital[1], 44)
			phone = self.shortenDisplay(hospital[2], 16)
			email = self.shortenDisplay(hospital[3], 28)
			city = self.shortenDisplay(hospital[4], 24)
			state = self.shortenDisplay(hospital[5], 16)
			zipcode = self.shortenDisplay(hospital[6], 12)
		
			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<40} {:<16} {:<28} {:<24} {:<16} {:<12}'.format(id, name, phone, email, city, state, zipcode))

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
		select_query = f"SELECT * FROM hospital WHERE id={ID}"
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

	def getCompanyByID(self, ID):
		if ID is None:
			return None
		get_company_query = f"SELECT * FROM company WHERE id={ID}"
		self.cur_main.execute(get_company_query)
		company = self.cur_main.fetchone()
		print("GETTING HOSPITAL BY ID")
		print(company)
		print(type(company))
		return company


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

# Test 2 (On Master Branch)
=======
# Test Comment for GIT commit and push. Delete afterwards

