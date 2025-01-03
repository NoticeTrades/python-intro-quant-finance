#Exercise 1: Declaring and Using Variables

"""Create a variable called name and assign it your name
"""

"""Create another variable age and assign it your age"""

"""Add a variable is_trader and set it to True"""

"""print a sentence that says: "Hi, my name is [name]. 
I am [age] years old, and it's [is_trader] that I am trader"""
"Use an f-string for this"

name = 'nick'
age = 23
is_trader = True

print(f"Hi, my name is {name}. I am {age} years old, and it's {is_trader} that I am a trader.")

#Exercise 2: Playing with Data Types

"""Create three variables: shares (integer), price_per_share(float), and ticker (string, e.g., "NVDA")"""

"""Calculate the total cost of buying the shares and store it in a variable called total_cost"""

"""Print a sentence that shows the ticker, number of shares, and total cost"""

shares = 10
price_per_share = 42.30
ticker = "NVDA"

total_cost = shares * price_per_share

print(f"I bought {shares} shares of {ticker} at a price of {price_per_share:.2f} per share for a total cost of {total_cost:.2f}")

#Exercise 3: Calculating the Average PPS (price per share)

""""" Youre buying shares of a stock in multiple transactions. Write a program to calculate 
the average price per share based on the total cost and the total number of shares purchased.
"""

# Defining shares and prices for three transactions
shares_1 = 10
price_per_share_1 = 30.42
shares_2 = 15
price_per_share_2 = 52.32
shares_3 = 42
price_per_share_3 = 28.32

# Calculating the total cost for each transaction
total_cost_1 = shares_1 * price_per_share_1
total_cost_2 = shares_2 * price_per_share_2
total_cost_3 = shares_3 * price_per_share_3

# Overall total cost and total number of shares
overall_total = total_cost_1 + total_cost_2 + total_cost_3
total_shares = shares_1 + shares_2 + shares_3

# Calculating the average price per share
average_pps = overall_total / total_shares

# Displaying the result
print(f"The average price per share for the stock is ${average_pps:.2f}")
