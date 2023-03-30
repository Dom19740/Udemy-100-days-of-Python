# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this

print("\n!!!*** Welcome to the tip calculator ** *!!!\n")

total = float(input("What was the total bill? "))  # $150.00

tip = float(input("How much tip would you like to give? 10%, 12%, or 15%? ")) / 100 # 12 converted to 0.12

people = int(input("How many people to split the bill? "))  # 5

pay = format((((total * tip) + total) / people), '.2f') # Tip calculation and force to 2 decimal places

print(f"\nEach person should pay: ${pay}\n")
