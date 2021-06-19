import tkinter as tk


class hospitalsTab:
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