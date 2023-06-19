deposit = float(input("How much do you deposit?: "))
withdraw =  float(input("How much do you withdraw?: "))
money = deposit - withdraw
interest = 0.05
year = float(input("How many years have you left your account?: "))
final1 = money * interest * year
final = final1 + money
print("You have: ", final, " in  your account.")
