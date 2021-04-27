'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

initial_investment = float(input("How much would you like to initially invest?: "))
interest_rate = float(input("What interest rate would you like to invest at?: "))*.01
investment_years = float(input("How many years would you like to keep your money invested?: "))
return_on_investment = (initial_investment * (1 + interest_rate * investment_years))
print("You will have", return_on_investment, "dollars at the end of your investment.")
