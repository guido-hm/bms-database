import tkinter as tk

class CompanyTab:
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

		#Create Entrys
		self.nameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.cityEntry = tk.Entry(tabFrame)
		self.stateEntry = tk.Entry(tabFrame)
		self.zipcodeEntry = tk.Entry(tabFrame)


		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ", command=lambda: self.addItem(self.nameEntry, self.phoneEntry, self.emailEntry, self.cityEntry, self.stateEntry, self.zipcodeEntry))
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
		

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = CompanyInfoViewer(tabFrame, self.cur_main)



	def addItem(self, name, phone, email, city, state, zipcode):
		print("ADDING ITEM...")
		self.cur_main.execute("INSERT INTO company (name, phone, email, city, state, zipcode, notes, verified) VALUES ('{name}', '{phone}', '{email}', '{city}', '{state}', '{zipcode}', '{notes}', '{verified}')".format(name=name.get(), phone=phone.get(), email=email.get(), city=city.get(), state=state.get(), zipcode=zipcode.get(), notes="", verified=True))
		print("ITEM ADDED")

		name.delete(0, "end")
		phone.delete(0, "end")
		email.delete(0, "end")
		city.delete(0, "end")
		state.delete(0, "end")
		zipcode.delete(0, "end")

		self.cur_main.execute("SELECT * FROM company")

		self.infoViewer.updateListbox()



class CompanyInfoViewer:
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

		self.populateListbox()

	def populateListbox(self):

		self.cur_main.execute("SELECT * FROM company")
		company_list = self.cur_main.fetchall()

		for company in company_list:
			id = company[0]
			name = self.shortenDisplay(company[1], 44)
			phone = self.shortenDisplay(company[2], 16)
			email = self.shortenDisplay(company[3], 28)
			city = self.shortenDisplay(company[4], 24)
			state = self.shortenDisplay(company[5], 16)
			zipcode = self.shortenDisplay(company[6], 12)
		
			# Inserts Info into ListBox
			self.infoListbox.insert('end', '{:<10} {:<40} {:<16} {:<28} {:<24} {:<16} {:<12}'.format(id, name, phone, email, city, state, zipcode))

		return

	def deleteListbox(self):
		self.infoListbox.delete(0,'end')
		return
	
	def updateListbox(self):
		self.deleteListbox()
		self.populateListbox()
		return
	


	def selectItem(self, item):
		"""This function takes in the information of selected listbox entry, gets the ID of
			info and uses the ID to find database Entry. Toplevel is created to display info"""

		# TODO: Write function that opens new Toplevel displaying hospitals data (name, email, affiliated people, etc...)

		# Splits Listbox Info and gets only the ID
		selected_id = item.split()[0]

		# Fetches requested data based on ID
		self.cur_main.execute("SELECT * FROM company WHERE id={id}".format(id=int(selected_id)))


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
	