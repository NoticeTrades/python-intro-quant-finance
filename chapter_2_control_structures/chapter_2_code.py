## Stock Profit/Loss Checker

entry = float(input("What was your entry price? "))
exit = float(input("What was your exit price? "))
shares = int(input("How many shares did you buy? "))

pnl = (exit - entry) * shares

if pnl > 0:
    print(f"You made a profit of ${pnl:.2f}")
elif pnl < 0:
    print(f"You incurred a loss of ${(pnl):.2f}")
else:
    print("You broke even")

## Portfolio Risk Assesment 

investment = float(input("How much have you invested in stocks? "))
investment_2 = float(input("How much have you invested in bonds? "))

total_portfolio = investment + investment_2

if total_portfolio == 0: #Validation to user to enter valid investment amounts
    print("Your total portfolio value is zero. Please enter valid investment amounts.")
else:
    percentage_stock = (investment / total_portfolio) * 100

    if percentage_stock > 70:
        print(f"You have a high risk portfolio as you hold {percentage_stock:.2f}% in stock.")
    elif 40 <= percentage_stock <= 70:
        print(f"You have a moderate risk portfolio as you hold {percentage_stock:.2f}% in stock.")
    else:
        print(f"You have a low risk portfolio with your stock holdings being {percentage_stock:.2f}%.")

""""I can clean up this code above by adding input validation to ensure the user provides non-negative and non-zero inputs."""

# Investment Goal Tracker 

investment = float(input("Enter your current investment amount: "))
goal = float(input("Enter your investment goal:"))
growth_rate = float(input("Enter the annual growth rate (in %): "))

years = 0

while investment < goal:
    years += 1  
    investment += investment * (growth_rate / 100)  # Calculate annual growth
    print(f"Year {years}: ${investment:.2f}")  # Print the balance for each year

# Print the total number of years it took to reach the goal
print(f"You will reach your goal in {years} years.")

## Problem: Grade Evaulator 

grade = float(input("What was your score? Please enter a number between 0 and 100: "))

if grade < 0 or grade > 100:
    print("Please enter a valid score between 0 and 100")
else:
    if 90 <= grade <= 100:
        print("You got an A!")
    elif 80 <= grade < 90:
        print("You got a B!")
    elif 70 <= grade < 80:
        print("You got a C!")
    elif 60 <= grade < 70:
        print("You got a D!")
    else:
        print("You got an F!")


## Problem: Savings Goal Tracker 

savings_goal = float(input("What is your savings goal (e.g., $1,000): "))

savings_balance = 0 

while savings_balance < savings_goal:
    deposit = float(input("How much would you like to deposit? "))
    savings_balance += deposit
    print(f"Your current savings balance is ${savings_balance:.2f}")

# Check if the goal was reached or exceeded after the loop
if savings_balance == savings_goal:
    print("Congratulations! You have reached your savings goal!")
elif savings_balance > savings_goal:
    print("Congratulations! You have exceeded your savings goal!")

