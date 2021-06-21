import tkinter as tk

class ResellersTab:
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

		# Creates info-viewer section of tab
		self.infoViewer = ResellersInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class ResellersInfoViewer:
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

		# TODO: Write function to fill in listbox with resellers data
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, speciality, hospital))


		# Test to fills listbox with numbers 400-499. Delete later
		for i in range(100):
			self.infoListbox.insert('end', i+400)

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying resellers data (name, email, catalogs, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 