import tkinter as tk


class HospitalTab:
	def __init__(self, tabFrame):

		#Create Labels
		self.name = tk.Label(tabFrame, text="Name:")
		self.phone = tk.Label(tabFrame, text="Phone:")
		self.email = tk.Label(tabFrame, text="Email:")
		self.city = tk.Label(tabFrame, text="City:")
		self.state = tk.Label(tabFrame, text="State:")
		self.zip = tk.Label(tabFrame, text="Zip:")
		self.company = tk.Label(tabFrame, text="Company:")

		#Create Entrys
		self.nameEntry = tk.Entry(tabFrame)
		self.phoneEntry = tk.Entry(tabFrame)
		self.emailEntry = tk.Entry(tabFrame)
		self.cityEntry = tk.Entry(tabFrame)
		self.stateEntry = tk.Entry(tabFrame)
		self.zipEntry = tk.Entry(tabFrame)

		companyList = ["Company 1", "Company 2", "Company 3", "Company 4"]

		self.companyVar = tk.StringVar(tabFrame)
		self.companyVar.set("N/A")
		self.companyOptionMenu = tk.OptionMenu(tabFrame, self.companyVar, *companyList)

		#Create Buttons
		self.buttonSearch = tk.Button(tabFrame, font="Calibri 12", text="SEARCH")
		self.buttonAdd = tk.Button(tabFrame, font="Calibri 12", text="  ADD  ")
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

		self.zip.grid(row=5, column=0, padx=1, pady=5)
		self.zipEntry.grid(row=5, column=1, padx=1, pady=5)
		
		self.company.grid(row=6, column=0, padx=1, pady=5)
		self.companyOptionMenu.grid(row=6, column=1, padx=1, pady=5)
		
		self.buttonSearch.grid(row=7, column=0, padx=1, pady=5)
		self.buttonAdd.grid(row=7, column=1, padx=1, pady=5)
		self.buttonImport.grid(row=7, column=2, padx=1, pady=5)


		# Creates info-viewer section of tab
		self.infoViewer = HospitalInfoViewer(tabFrame)

		# Fills listbox with info
		self.infoViewer.populateListbox()

class HospitalInfoViewer:
	def __init__(self, frame):

		# 3 Frames. titleFrame and contentFrame are inside viewerFrame.
		self.viewerFrame = tk.Frame(frame, bg='light green')
		self.viewerFrame.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.58)

		# Creates frame for titles
		self.titleFrame = tk.Frame(self.viewerFrame, bg='light blue')
		self.titleFrame.place(relwidth=1, relheight=0.06)

		# Creates label for titles
		self.titleLabel = tk.Label(self.titleFrame, anchor='w', font= "consolas 12", text='{:<44}|{:<16}|{:<28}|{:<24}|{:<16}|{:<12}'.format("Name", "Phone # ", "Email", "City ", "State", "Zip"))
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