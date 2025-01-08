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