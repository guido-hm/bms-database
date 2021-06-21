import tkinter as tk

class DoctorsTab:
	def __init__(self, tabFrame):

		#Create Labels
		self.doctorFirstName = tk.Label(tabFrame, text="First Name:")
		self.doctorLastName = tk.Label(tabFrame, text="Last Name:")
		self.doctorPhone = tk.Label(tabFrame, text="Phone:")
		self.doctorEmail = tk.Label(tabFrame, text="Email:")
		self.doctorSpecialty = tk.Label(tabFrame, text="Specialty:")
		self.doctorHospital = tk.Label(tabFrame, text="Hospital:")

		#Create Entrys
		self.doctorFirstNameEntry = tk.Entry(tabFrame)
		self.doctorLastNameEntry = tk.Entry(tabFrame)
		self.doctorPhoneEntry = tk.Entry(tabFrame)
		self.doctorEmailEntry = tk.Entry(tabFrame)
		self.doctorSpecialtyEntry = tk.Entry(tabFrame)

		# TODO: Change Hospital Entry to a Drop Down Menu
		self.doctorHospitalEntry = tk.Entry(tabFrame)

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.doctorFirstName.grid(row=0, column=0, padx=5, pady=5)
		self.doctorFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.doctorLastName.grid(row=1, column=0, padx=5, pady=5)
		self.doctorLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		self.doctorPhone.grid(row=2, column=0, padx=5, pady=5)
		self.doctorPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		self.doctorEmail.grid(row=3, column=0, padx=5, pady=5)
		self.doctorEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		self.doctorSpecialty.grid(row=4, column=0, padx=5, pady=5)
		self.doctorSpecialtyEntry.grid(row=4, column=1, padx=15, pady=5)

		self.doctorHospital.grid(row=5, column=0, padx=5, pady=5)
		self.doctorHospitalEntry.grid(row=5, column=1, padx=15, pady=5)

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# TODO: Add info-viewer for tab
		#	- Scrollable widget

		# Creates info-viewer section of tab
		self.infoViewer = DoctorsInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class DoctorsInfoViewer:
	def __init__(self, frame):

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

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

		# TODO: Write function to fill in listbox with doctors data
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, speciality, hospital))


		# Test to fills listbox with numbers 100-199. Delete later
		for i in range(100):
			self.infoListbox.insert('end', i+100)

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying doctors data (name, email, notes, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 