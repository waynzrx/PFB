#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "Data Structure"
#name = Wayne Teo Ren Xian
#np_email = s10240130@connect.np.edu.sg
#student_id = S10240130B
#class_number = TI01

#--------------------- 1. List ---------------------#

# You are given information of the membership numbers and the membership fees of the local gyms.
# The information is a nested list `gym_data`. The elements in each sub-list contain:
## 1. The gym name
## 2. The number of members
## 3. Membership fee per member

gym_data_list = [['FitFirst', 8500, 3500], ['PlanetFit', 5500, 2300], [
    'GoldGym', 9000, 1800], ['AnyTimeFit', 7200, 2400], ['VirginFit', 3200, 3800]]

# 1.
# Write a function `total_summary` with a single parameter `option`.
# When "membership" is supplied to the option parameter, `total_summary_list` function will return
# the total number of membership across the gyms.
# When "fee" is supplied to the option parameter, `total_summary_list` function will return
# the total membership fee revenue collected across the gyms.
# Otherwise, it will return `invalid entry` for any other values supplied to the `option` parameter.
# Note: total membership fee revenue =  the number of members x membership fee per member


# Examples of what the functions will display and return when executed:

## print(total_summary_list("membership"))
## Total number of members across the gyms: 33400


## print(total_summary_list("fee"))
## Total membership fees revenue collected across the gyms: $88040000

#--------------------- 1. List ---------------------#
def total_summary_list(option):
    """
    This function calculates the total number of members or total fee revenue for a list of gyms, 
    depending on the option input.
    paramters: option - specify whether to calculate the total number of members 
    or the total fee revenue. 
    Should be either "membership" or "fee", anything else will return "Invalid entry"
    return: total number of members or total fee revenue with a label, as a string
    """
    # Initialize variables to keep track of the running total
    total_members = 0
    total_fee = 0
    
    # Iterate through each gym in the list
    for gym in gym_data_list:
        
        # Check the value of the option input
        if option == "membership":
            # If the option is "membership", add the number of members at this gym to the running total
            total_members += gym[1]
        elif option == "fee":
            # If the option is "fee", calculate the total membership fee revenue 
            # by multiplying the number of members by the membership fee, and add that to the running total
            total_fee += gym[1] * gym[2]
        else:
            # If the option input is anything else, return "Invalid entry"
            return "Invalid entry"
            
    # Return the final total along with the appropriate label
    if option == "membership":
        return "Total number of members across the gyms: " + str(total_members)
    elif option == "fee":
        return "Total membership fees revenue collected across the gyms: $" + str(total_fee)

# Test the function with the option "membership"
print(total_summary_list("membership"))
# Test the function with the option "fee"
print(total_summary_list("fee"))




#--------------------- 2. Dictionary ---------------------#
# The same information is now structured as a dictionary.
# Write a similar function that will total number of membership and
# total membership fee revenue.

gym_data_dict = {'FitFirst': {"number of members": 8500,
                              "membership fee": 3500
                              },
                 "PlanetFit": {"number of members": 5500,
                               "membership fee": 2300
                               },
                 "GoldGym":  {"number of members": 9000,
                              "membership fee": 1800
                              },
                 "AnyTimeFit": {"number of members": 7200,
                                "membership fee": 2400
                                },
                 "VirginFit": {"number of members": 3200,
                               "membership fee": 3800
                               },
                 }



def total_summary_dict(option):
    """
    This function calculates the total number of members or total fee revenue for a dictionary of gyms, 
    depending on the option input.
    parameters: option - specify whether to calculate the total number of members 
    or the total fee revenue. 
    Should be either "membership" or "fee", anything else will return "Invalid entry"
    return: total number of members or total fee revenue with a label, as a string
    """
    # Initialize list to store the number of members or fee revenue
    values = []
    if option == "membership":
        # Iterate through the gym_data_dict, and retrieve the number of members of each gym
        for gym in gym_data_dict:
            values.append(gym_data_dict[gym]["number of members"])
        #Calculate the total of number of members using sum()
        return "Total number of members across the gyms: " + str(sum(values))
    elif option == "fee":
        # Iterate through the gym_data_dict, and calculate the total fee revenue for each gym 
        # by multiplying the number of members by the membership fee 
        for gym in gym_data_dict:
            values.append(gym_data_dict[gym]["number of members"] * gym_data_dict[gym]["membership fee"])
        # Calculate the total of fee revenue using sum()
        return "Total membership fees revenue collected across the gyms: $" + str(sum(values))
    else:
        # check if option passed is valid or not
        return "Invalid entry"



# Test the function with the option "membership"
print(total_summary_dict("membership"))
# Test the function with the option "fee"
print(total_summary_dict("fee"))
