import tkinter as tk

class doctorsTab:
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