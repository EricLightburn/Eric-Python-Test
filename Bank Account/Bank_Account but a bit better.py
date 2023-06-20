class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance<amount:
			print("\n Insufficient balance")
		else:
			self.balance -= amount
			print("\n You Withdrew: ", amount)
	
	def increment_year(self):		
		year = float(input("How many years have you left your account?: "))
		interest = 0.05
		compound_final = self.balance * ((1 + interest / 1) ** year)
		self.balance = compound_final
		print("\n You have left your account for: ", year, " years and you have a ") 
		print("\n Net Available Balance of",self.balance)

s = Bank_Account()

s.__init__()
s.deposit()
s.withdraw()
s.increment_year()

