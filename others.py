import tkinter as tk

class othersTab:
	def __init__(self, tabFrame):

		#Create Labels
		self.otherFirstName = tk.Label(tabFrame, text="First Name:")
		self.otherLastName = tk.Label(tabFrame, text="Last Name:")
		self.otherPhone = tk.Label(tabFrame, text="Phone:")
		self.otherEmail = tk.Label(tabFrame, text="Email:")
		self.otherOccupation = tk.Label(tabFrame, text="Specialty:")
		self.otherHospital = tk.Label(tabFrame, text="Hospital:")

		#Create Entrys
		self.otherFirstNameEntry = tk.Entry(tabFrame)
		self.otherLastNameEntry = tk.Entry(tabFrame)
		self.otherPhoneEntry = tk.Entry(tabFrame)
		self.otherEmailEntry = tk.Entry(tabFrame)
		self.otherOccupationEntry = tk.Entry(tabFrame)

		# TODO: Change Hospital Entry to a Drop Down Menu
		self.otherHospitalEntry = tk.Entry(tabFrame)

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
		self.otherHospitalEntry.grid(row=5, column=1, padx=15, pady=5)

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# TODO: Add info-viewer for tab
		#	- Scrollable widget