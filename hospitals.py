import tkinter as tk


class HospitalsTab:
	def __init__(self, tabFrame):

		#Create Labels
		self.hospitalName = tk.Label(tabFrame, text="Name:")
		self.hospitalPhone = tk.Label(tabFrame, text="Phone:")
		self.hospitalEmail = tk.Label(tabFrame, text="Email:")
		self.hospitalCity = tk.Label(tabFrame, text="City:")
		self.hospitalState = tk.Label(tabFrame, text="State:")
		self.hospitalZip = tk.Label(tabFrame, text="Zip:")

		#Create Entrys
		self.hospitalNameEntry = tk.Entry(tabFrame)
		self.hospitalPhoneEntry = tk.Entry(tabFrame)
		self.hospitalEmailEntry = tk.Entry(tabFrame)
		self.hospitalCityEntry = tk.Entry(tabFrame)
		self.hospitalStateEntry = tk.Entry(tabFrame)
		self.hospitalZipEntry = tk.Entry(tabFrame)

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
		self.buttonImport = tk.Button(tabFrame, font="Calibri 12", text="IMPORT")

		#Add buttons onto frame using grid positioning
		self.hospitalName.grid(row=0, column=0, padx=5, pady=5)
		self.hospitalNameEntry.grid(row=0, column=1, padx=15, pady=5)

		self.hospitalPhone.grid(row=1, column=0, padx=5, pady=5)
		self.hospitalPhoneEntry.grid(row=1, column=1, padx=15, pady=5)

		self.hospitalEmail.grid(row=2, column=0, padx=5, pady=5)
		self.hospitalEmailEntry.grid(row=2, column=1, padx=15, pady=5)

		self.hospitalCity.grid(row=3, column=0, padx=5, pady=5)
		self.hospitalCityEntry.grid(row=3, column=1, padx=15, pady=5)

		self.hospitalState.grid(row=4, column=0, padx=5, pady=5)
		self.hospitalStateEntry.grid(row=4, column=1, padx=15, pady=5)

		self.hospitalZip.grid(row=5, column=0, padx=1, pady=5)
		self.hospitalZipEntry.grid(row=5, column=1, padx=1, pady=5)
		

		self.buttonSearch.grid(row=6, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=6, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=6, column=2, padx=1, pady=5)

		# TODO: Add info-viewer for tab
		#	- Scrollable widget

		# Creates info-viewer section of tab
		self.infoViewer = HospitalsInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class HospitalsInfoViewer:
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

		# TODO: Write function to fill in listbox with hospitals data
		# Example on how to fill in data:
		#	- myListbox.insert('end', '{:<14} {:<13} {:<5} {:<5} {:<5} {:<5}'.format(first, last, email, phone, speciality, hospital))


		# Test to fills listbox with numbers 200-299. Delete later
		for i in range(100):
			self.infoListbox.insert('end', i+200)

	def selectItem(self, item):

		# TODO: Write function that opens new Toplevel displaying hospitals data (name, email, affiliated people, etc...)

		# Prints the index of item selected, not the actual data
		print(self.infoListbox.curselection()) 