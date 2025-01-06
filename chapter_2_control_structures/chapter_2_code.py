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
