import tkinter as tk

class ResellerTab:
	def __init__(self, tabFrame, cursor):

		self.cur_main = cursor
		self.tabFrame = tabFrame

		# Create Labels
		self.firstName = tk.Label(tabFrame, text="First Name:")
		self.lastName = tk.Label(tabFrame, text="Last Name:")
		self.phone = tk.Label(tabFrame, text="Phone:")
		self.email = tk.Label(tabFrame, text="Email:")
		self.gender = tk.Label(tabFrame, text="Gender:")
		self.company = tk.Label(tabFrame, text="Company:")

		#Create Entrys
		self.firstNameEntry = tk.Entry(tabFrame)
		self.lastNameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.genderEntry = tk.Entry(tabFrame)

		# Creates company optionmenu
		self.createOptionMenu()

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH", command=self.searchDatabase)
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ", command=lambda: self.addItem(self.firstNameEntry, self.lastNameEntry, self.phoneEntry, self.emailEntry, self.genderEntry, self.companyVar))
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

		self.gender.grid(row=4, column=0, padx=1, pady=5)
		self.genderEntry.grid(row=4, column=1, padx=1, pady=5)

		# self.company.grid(row=5, column=0, padx=1, pady=5)
		# self.companyOptionMenu.grid(row=5, column=1, padx=1, pady=5)

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = ResellerInfoViewer(tabFrame, self.cur_main)

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
		self.company.grid(row=5, column=0, padx=1, pady=5)
		self.companyOptionMenu.grid(row=5, column=1, padx=1, pady=5)

	def deleteOptionMenu(self):
		self.companyOptionMenu.destroy()

	def refreshOptionMenu(self):
		self.deleteOptionMenu()
		self.createOptionMenu()

	def addItem(self, first_name, last_name, phone, email, gender, company):
			print("ADDING ITEM...")

			# Checks if user included company for doctor
			if company.get() == "None":
				processed_company_id = None
			else:
				processed_company_id = company.get().split()[0]

			# Query statement and data to insert hospital info if there is no company on file for it
			insert_query = "INSERT INTO reseller (first_name, last_name, phone, email, gender, company_id, prefix, notes, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			insert_data = (first_name.get(), last_name.get(), phone.get(), email.get(), gender.get(), processed_company_id, "", "", True)

			# Execute querty statement with data
			self.cur_main.execute(insert_query, insert_data)

			# Deletes the entry field input to allow new entry
			first_name.delete(0, "end")
			last_name.delete(0, "end")
			phone.delete(0, "end")
			email.delete(0, "end")
			gender.delete(0, "end")

			# Sets company Optionmenu to None to allow new entry
			company.set(None)

			# Updates the infoViewer with new data
			self.infoViewer.updateListbox("")


	def searchDatabase(self):
		field_data = []
		field_names = ["first_name", "last_name", "phone", "email", "gender", "company_id"]

		# Adds user-inputted info to a list. This will be used to create query used to search for records with given parameters
		field_data.append(self.firstNameEntry.get())
		field_data.append(self.lastNameEntry.get())
		field_data.append(self.phoneEntry.get())
		field_data.append(self.emailEntry.get())
		field_data.append(self.genderEntry.get())
		field_data.append(self.companyVar.get().split()[0])

		# Clears entry fields after searching
		self.firstNameEntry.delete(0,'end')
		self.lastNameEntry.delete(0,'end')
		self.phoneEntry.delete(0,'end')
		self.emailEntry.delete(0,'end')
		self.genderEntry.delete(0,'end')
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


class ResellerInfoViewer:
	def __init__(self, frame, cursor):

		self.cur_main = cursor

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<10}|{:<14}|{:<16}|{:<16}|{:<28}|{:<62}'.format("ID", "First Name", "Last Name", "Phone #", "Email", "Company"))
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

		# Fills listbox with info
		self.populateListbox("")

	def populateListbox(self, conditions):

		if conditions:
			populate_query = "SELECT * FROM reseller WHERE " + conditions
		else:
			populate_query = "SELECT * FROM reseller"

		self.cur_main.execute(populate_query)
		reseller_list = self.cur_main.fetchall()

		print("THIS IS THE LIST\n\n\n")
		print(reseller_list)

		for reseller in reseller_list:
			id = reseller[0]
			first = self.shortenDisplay(reseller[1], 14)
			last = self.shortenDisplay(reseller[2], 16)
			phone = self.shortenDisplay(reseller[3], 16)
			email = self.shortenDisplay(reseller[4], 28)
			company = self.shortenDisplay(reseller[6], 62)

			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<14} {:<16} {:<16} {:<28} {:<62}'.format(id, first, last, phone, email, company))

		return
	
	def deleteListbox(self):
		self.infoListbox.delete(0,'end')
		return

	def updateListbox(self, condiitons):
		self.deleteListbox()
		self.populateListbox(condiitons)
		return
	

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying resellers data (name, email, catalogs, etc...)

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