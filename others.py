import tkinter as tk

class OtherTab:
	def __init__(self, tabFrame):

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


		

		# Temporary List(DELETE LATER)
		hospitalList = ['Texas General Hospital', 'Northwest Hospital', 'Baylor Medical Center of Irving', 'Medical Center of Lewisville', 'Methodist Richardson Medical Center']

		companyList = ["Company 1", "Company 2", "Company 3", "Company 4"]

		#Create OptionMenu
		
		# TODO: Fix problem
		#	- Every time a hospital is selected, the OptionMenu takes on its size.
		#	  This changes the width of the whole grid's column, moving all elements on that column
		# SOLUTION IDEA: Put OptionMenu on screen using .place() rather than .grid()

		self.hospitalVar = tk.StringVar(tabFrame)
		self.hospitalVar.set("N/A")
		self.hospitalOptionMenu = tk.OptionMenu(tabFrame, self.hospitalVar, *hospitalList)

		self.companyVar = tk.StringVar(tabFrame)
		self.companyVar.set("N/A")
		self.companyOptionMenu = tk.OptionMenu(tabFrame, self.companyVar, *companyList)

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
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

		self.hospital.grid(row=6, column=0, padx=5, pady=5)
		self.hospitalOptionMenu.grid(row=6, column=1, padx=15, pady=5)

		self.company.grid(row=7, column=0, padx=5, pady=5)
		self.companyOptionMenu.grid(row=7, column=1, padx=5, pady=5)

		self.buttonSearch.grid(row=8, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=8, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=8, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = OtherInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class OtherInfoViewer:
	def __init__(self, frame):

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light blue')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<16}|{:<24}|{:<16}|{:<28}|{:<24}|{:<44}'.format("First Name", "Last Name", "Phone #", "Email", "Occupation", "Hospital"))
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

	def populateListbox(self):

		# TODO: Write function to fill in listbox with peoples(others) data
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, speciality, hospital))


		# Test to fills listbox with numbers 300-399. Delete later
		for i in range(100):
			self.infoListbox.insert('end', i+300)

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying peoples(others) data (name, email, notes, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 