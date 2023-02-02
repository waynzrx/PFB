#-------------------------------- Q2 ------------------------------------#
# Write a function: loan_calculator(amount, interest, month).
# The function will calculate the total loan amount payable.
#------------------------------------------------------------------------#

#### Example of how the function works ####

# Given a loan amount of $1000, 10% interest rate and 5 month loan period,
# the function will calculate the interests payment plus the principal loan amount.
# When `loan_calculator(1000,0.10,5)` is executed, it will return $1,610.51

# The calculation of $1610.51 is as follow:
# Month 1 = $1100 ($1000 * 1.1)
# Month 2 = $1210 ($1100 * 1.1)
# Month 3 = $1331 ($1210 * 1.1)
# Month 4 = $1464 ($1331 * 1.1)
# Month 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.
# BONUS: Can you use f-strings to include a $ symbol with the return value?

# Expected output is just:
# $1,610.51

# IMPORTANT: Must use 'for loop' in your solution.

def loan_calculator(amount, interest, month):
    """
    function will calculate interests payment plus principal loan amount
    """
    for months in range(5):
        
        Total_amount = amount*(1+interest)**month
        return(f"${Total_amount:,.2f}")

print(loan_calculator(1000,0.1,5))





