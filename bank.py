char_name = input("Welcome to the national bank of whatever. what is your name?")
starting_balance = (5000.25)
print(f"hello {char_name} your current balance is {starting_balance}")
pay_check = float(input("how much would you like to deposit"))

new_balance = starting_balance + pay_check
print(f"your balance after deposit is {new_balance}")

object_name = input(f"seems that you have gone shopping, what did you buy?")
object_price = float(input(f"How much did this {object_name} cost?"))

ending_balance = new_balance - object_price

print(f"{char_name}, after spending money on {object_name} your current balance after purchase is {ending_balance}")