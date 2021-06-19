import tkinter as tk

class resellersTab:
	def __init__(self, tabFrame):

		# Create Labels
		self.resellerFirstName = tk.Label(tabFrame, text="First Name:")
		self.resellerLastName = tk.Label(tabFrame, text="Last Name:")
		self.resellerPhone = tk.Label(tabFrame, text="Phone:")
		self.resellerEmail = tk.Label(tabFrame, text="Email:")

		#Create Entrys
		self.resellerFirstNameEntry = tk.Entry(tabFrame)
		self.resellerLastNameEntry = tk.Entry(tabFrame)
		self.resellerPhoneEntry = tk.Entry(tabFrame)
		self.resellerEmailEntry = tk.Entry(tabFrame)

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.resellerFirstName.grid(row=0, column=0, padx=5, pady=5)
		self.resellerFirstNameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.resellerLastName.grid(row=1, column=0, padx=5, pady=5)
		self.resellerLastNameEntry.grid(row=1, column=1, padx=15, pady=5)

		self.resellerPhone.grid(row=2, column=0, padx=5, pady=5)
		self.resellerPhoneEntry.grid(row=2, column=1, padx=15, pady=5)

		self.resellerEmail.grid(row=3, column=0, padx=5, pady=5)
		self.resellerEmailEntry.grid(row=3, column=1, padx=15, pady=5)

		self.buttonSearch.grid(row=4, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=4, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=4, column=2, padx=1, pady=5)

		# TODO: Add info-viewer for tab
		#	- Scrollable widget