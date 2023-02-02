#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "conditionals"
#name = Wayne Teo Ren Xian
#np_email = s10240130@connect.np.edu.sg
#student_id = S10240130B
#class_number = TI01

#------------------------ Part 1 : if, elif, else ------------------------#
# Write a function: tax_rebate() to determine tax rebate from income level
#-------------------------------------------------------------------------#

# The function will prompt a user to declare his/her yearly income
# and determine the amount of one-time off tax rebate he/she should receive.
# Note that the function does not require any parameters. It will return the
# amount of tax rebate based on the following tax rules:

# Yearly Income in $ 	                # Tax Rebate in $
# ------------------                      -------------
# 0 to less than 40000 	                      2000
# 40000 to less than 100000	                  1000
# 100000 to less than 150000 	              500
# equal or greater than 150000 	             not eligible

# Executing the function based on different income levels will display and return output
# like the followings:

#### Example 1 ####
# Declare your yearly income : 10000
# Your tax rebate is : $2000

#### Example 2 ####
# Declare your yearly income : 80000
# Your tax rebate is : $1000

#### Example 3 ####
# Declare your yearly income : 110000
# Your tax rebate is : $500

#### Example 4 ####
# Declare your yearly income : 150000
# You are not eligible for tax rebate

#### Example 5 ####
# Declare your yearly income : 200000
# You are not eligible for tax rebate

# Execute with this line (in the main program, outside the function):
# print(tax_rebate())

def tax_rebate():
    """
    - function will return rebate based on income level
    """
    yearlyincome = input("Declare your yearlyincome")

    yearlyincome = float(input("Enter yearlyincome: "))
    #if loop so if yearly income is less than 40000, it will print the following message
    if yearlyincome < 40000: 
        return ("Your tax rebate is $2000")
    #if loop so if yearly income is less than 100000 but more than 40000, it will print the following message
    elif yearlyincome < 100000:
        return ("Your tax rebate is $1000")
    #if loop so if yearly income is less than 150000 but more than 100000, it will print the following message
    elif yearlyincome < 150000:
        return ("Your tax rebate is $500")
    #if loop so if yearly income is more than 150,000, it will print the following message
    else :
         return ("You are not eligible for tax rebate")
         
    print(tax_rebate())
    
    

#---------------------------------- Part 2  ---------------------------------#
# Improve the tax_rebate() function from Part 1 to make the program
# less susceptible to crashing.
#----------------------------------------------------------------------------#

# It should prevent the program from crashing if the user entered "string"
# data type when declaring his/her income.

# The function should loop endlessly to ask the user to declare the income until
# he/she use "number" data type.

# Here is an example of how the program will behave:

    # Declare your yearly income: ten thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: one thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: 10000
    # Your tax rebate is : $2000

# Tips:
# Design the function with `while loop` in mind, so that program will
# keep looping until the user input entered the correct data type.

# Execute with this line (in the main program, outside the function):
# print(tax_rebate_2())

def tax_rebate_2():
    """
    - Function will return rebate based on income level
    """
income = input("Declare your yearly income: ")
#If input is not a digit, it will print the following
while income.isdigit() == False:
        print("[INVALID INPUT] Only number is accepted, please re-enter again.")
        income = input("Declare your yearly income: ")
#

print(tax_rebate_2())