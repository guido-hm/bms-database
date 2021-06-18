import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("300x400")

class LoginWindow:
	def __init__(self, master):
		self.master = master

		self.loginFrame = tk.Frame(master)
		self.loginFrame.place(relwidth=1, relheight=1)

		self.loginLabel = tk.Label(self.loginFrame, font="Calibri 24", text="Login")
		self.loginLabel.pack()

		# Username
		self.usernameLabel = tk.Label(self.loginFrame, font="Calibri 14", text="Username: ")
		self.usernameLabel.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.05)

		self.usernameEntry = tk.Entry(self.loginFrame)
		self.usernameEntry.place(relx=0.4, rely=0.6, relwidth=0.5, relheight=0.05)

		# Password
		self.passwordLabel = tk.Label(self.loginFrame, font="Calibri 14", text="Password: ")
		self.passwordLabel.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.05)

		self.passwordEntry = tk.Entry(self.loginFrame)
		self.passwordEntry.place(relx=0.4, rely=0.65, relwidth=0.5, relheight=0.05)

		#Login Button
		self.loginButton = tk.Button(self.loginFrame, font="Calibri 14", text="Login", command = lambda: self.Login(self.usernameEntry.get(), self.passwordEntry.get()))
		self.loginButton.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

	def Login(self, username, password):
		""" Compares the entered password hash to the hash stored in the database.
		If it matches, login is successful."""

		# TODO: Build Function
		#	- Figure out where usernames and passwords will be stored
		#	- Add if else statement. If login is successful, DatabaseWindow() is called.
		#	- Else, error window is displayed.

		# Calling DatabaseWindow with no conditional temporarily
		self.DatabaseWindow()

	def DatabaseWindow(self):
		# TODO: Build Function
		#	- Self.loginFrame and everything in it will be destroyed
		#	  and a new frame will be created, where the rest of the program will live.

		self.loginFrame.destroy()

		# Changes the window size
		root.geometry("900x500")

		# New frame for database created
		self.databaseFrame = tk.Frame(self.master)
		self.databaseFrame.place(relwidth=1, relheight=1)

		# TODO: Build Function
		#	- Self.loginFrame and everything in it will be destroyed
		#	  and a new frame will be created, where the rest of the program will live.




window = LoginWindow(root)
root.mainloop()