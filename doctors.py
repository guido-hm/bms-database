import tkinter as tk

class DoctorTab:
	def __init__(self, tabFrame):

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

		# Temporary List(DELETE LATER)
		hospitalList = ['Texas General Hospital', 'Northwest Hospital', 'Baylor Medical Center of Irving', 'Medical Center of Lewisville', 'Methodist Richardson Medical Center']
		companyList = ["Company 1", "Company 2", "Company 3", "Company 4"]

		# TODO: Fix problem
		#	- Every time a hospital is selected, the OptionMenu takes on its size.
		#	  This changes the width of the whole grid's column, moving all elements on that column
		# SOLUTION IDEA: Put OptionMenu on screen using .place() rather than .grid()

		self.hospitalVar = tk.StringVar(tabFrame)
		self.hospitalVar.set(hospitalList[0])
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

		self.specialty.grid(row=4, column=0, padx=5, pady=5)
		self.specialtyEntry.grid(row=4, column=1, padx=15, pady=5)

		self.gender.grid(row=5, column=0, padx=5, pady=5)
		self.genderEntry.grid(row=5, column=1, padx=15, pady=5)

		self.hospital.grid(row=6, column=0, padx=5, pady=5)
		self.hospitalOptionMenu.grid(row=6, column=1, padx=15, pady=5)

		self.company.grid(row=7, column=0, padx=15, pady=5)
		self.companyOptionMenu.grid(row=7, column=1, padx=15, pady=5)

		self.buttonSearch.grid(row=8, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=8, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=8, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = DoctorInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class DoctorInfoViewer:
	def __init__(self, frame):

		## Each character of font "consolas 12" takes up 9 pixels. 
		## This info can be used to later create a window that works on any screen size by getting ratios

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)
		
		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		# Creates label for titles
		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<16}|{:<24}|{:<16}|{:<28}|{:<24}|{:<44}'.format("First Name", "Last Name", "Phone #", "Email", "Specialty", "Hospital"))
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

	def populateListbox(self):

		# TODO: Write function to fill in listbox with doctors data. Everything currently in here is temporary.
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, specialty, hospital))
		listFirst = ['Alberto', 'Roman', 'Guido', 'Joe', 'Alejandro Roberto', 'Guidwardo', 'Gabriel', 'Garbanzo', 'Araseli', 'Maria Jose']
		listLast = ['Gonzalez', "Martinez", "Herrera", "Trejo", "Feroz", 'Herraduramistico', 'Trejo', 'De La Ensalada', 'La Mera Mera', 'La Chava']
		listPhone = ["9565344764", "9565385939", "8999345781", "1234567890", "2439046372", "7783923453", "1528992847168", "3944630432", "0987654321", "9345743453"]
		listEmail = ["gonzalberto@gmail.com", "romanisgay@yahoo.com", "guidohm@tamu.edu", "joe@hotmail.com", "alerob123@gmail.com", "guidwardo@gmail.com", "gabe@gmail.com", "garbanzo234@elpolloloco.com", "ara@domain.com", "lachava@hotmail.com"]
		listSpecialty = ["Cardiologists", "Deeznotolist", "Ortopologist", "Dentist", "Cardiologists", "Cardiologists", "Genetisist", "Nurse", "Deeznotolist" ,"Cardiologists"]
		listHospital = ["Hospital San Andres de la Guardia en La Santa Cruz Aveztruz", "Star Childrens Hospital Dallas", "MAC Hospital Mexico City", "Texas General Hospital", "Northwest Hospital", "Baylor Medical Center of Irving", "Medical Center of Lewisville", "Methodist Richardson Medical Center", "Catholic District of People Hospital", "Putos Se La Come Northwestern Hospital"]
		# Test to fills listbox with numbers 100-199. Delete later
		for i in range(10):
			first = self.shortenDisplay(listFirst[i], 16)
			last = self.shortenDisplay(listLast[i], 24)
			phone = self.shortenDisplay(listPhone[i], 16)
			email = self.shortenDisplay(listEmail[i], 28)
			specialty = self.shortenDisplay(listSpecialty[i], 24)
			hospital = self.shortenDisplay(listHospital[i], 44)
			self.infoListbox.insert('end', '{:<16} {:<24} {:<16} {:<28} {:<24} {:<44}'.format(first, last, phone, email, specialty, hospital))

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying doctors data (name, email, notes, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 

	def shortenDisplay(self, string, length):
		'''Given a string and a length, it shortens the word to length,
		   with last three characters being dots (...)'''
		if len(string) <= length:
			return string.upper()

		string = string[:length-3]
		string += '...'
		print(string)
		return string.upper()