import tkinter as tk

class OthersTab:
	def __init__(self, tabFrame):

		#Create Labels
		self.otherFirstName = tk.Label(tabFrame, text="First Name:")
		self.otherLastName = tk.Label(tabFrame, text="Last Name:")
		self.otherPhone = tk.Label(tabFrame, text="Phone:")
		self.otherEmail = tk.Label(tabFrame, text="Email:")
		self.otherOccupation = tk.Label(tabFrame, text="Occupation:")
		self.otherHospital = tk.Label(tabFrame, text="Hospital:")

		#Create Entrys
		self.otherFirstNameEntry = tk.Entry(tabFrame)
		self.otherLastNameEntry = tk.Entry(tabFrame)
		self.otherPhoneEntry = tk.Entry(tabFrame)
		self.otherEmailEntry = tk.Entry(tabFrame)
		self.otherOccupationEntry = tk.Entry(tabFrame)

		

		# Temporary List(DELETE LATER)
		hospitalList = ['Texas General Hospital', 'Northwest Hospital', 'Baylor Medical Center of Irving', 'Medical Center of Lewisville', 'Methodist Richardson Medical Center']

		#Create OptionMenu
		
		# TODO: Fix problem
		#	- Every time a hospital is selected, the OptionMenu takes on its size.
		#	  This changes the width of the whole grid's column, moving all elements on that column
		# SOLUTION IDEA: Put OptionMenu on screen using .place() rather than .grid()

		self.otherHospitalVar = tk.StringVar(tabFrame)
		self.otherHospitalVar.set(hospitalList[0])
		self.otherHospitalOptionMenu = tk.OptionMenu(tabFrame, self.otherHospitalVar, *hospitalList)


		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.otherFirstName.grid(row=0, column=0, padx=5, pady=5)
		self.otherFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.otherLastName.grid(row=1, column=0, padx=5, pady=5)
		self.otherLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		self.otherPhone.grid(row=2, column=0, padx=5, pady=5)
		self.otherPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		self.otherEmail.grid(row=3, column=0, padx=5, pady=5)
		self.otherEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		self.otherOccupation.grid(row=4, column=0, padx=5, pady=5)
		self.otherOccupationEntry.grid(row=4, column=1, padx=15, pady=5)

		self.otherHospital.grid(row=5, column=0, padx=5, pady=5)
		self.otherHospitalOptionMenu.grid(row=5, column=1, padx=15, pady=5)

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# Creates info-viewer section of tab
		self.infoViewer = OthersInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class OthersInfoViewer:
	def __init__(self, frame):

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
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