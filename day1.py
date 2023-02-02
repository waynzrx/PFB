#####  Store your name, email, student_id and class_number as STRINGS #####
#ind_assign1 = "day 1"
#name = Wayne Teo Ren Xian
#np_email = s10240130@connect.np.edu.sg
#student_id = s10240130B
#class_number = TI01

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

#QUESTION 1
def acceleration_function():
    # Prompt the user for the input values
    final_velocity = input("Enter the final velocity (in m/s): ")
    starting_velocity = input("Enter the starting velocity (in m/s): ")
    elapsed_time = input("Enter the elapsed time (in seconds): ")

    # Convert input values into float
    final_velocity = float(final_velocity) 
    starting_velocity = float(starting_velocity)
    elapsed_time = float(elapsed_time)

    # Calculate the average acceleration
    acceleration = (final_velocity - starting_velocity) / elapsed_time

    return acceleration

# Example 1
#final_velocity=20, starting_velocity=5, elapsed_time=10
print(acceleration_function())

#Output: 1.5 (meters per second)




#QUESTION 2
def check_pw(password):
    # Initialize counters for the number of upper and lower case characters
    num_upper = 0
    num_lower = 0

    # Iterate over the length of the password
    for i in range(len(password)):
        # If the character is upper case, increment the counter
        if password[i].isupper():
            num_upper += 1
        # If the character is lower case, increment the counter
        elif password[i].islower():
            num_lower += 1

    # Check if the password is strong or weak using boolean and compound conditions
    # The function checks a password for strength by checking for certain characteristics.
    # It determines if a password is strong or weak based on the following criteria:
    #The password must be at least 14 characters long.
    # 1. The password must contain at least one upper case character.
    # 2. The password must contain at least one lower case character.
    # 3. The password must contain at least one exclamation mark (!).
    # 4. The password must contain at least one at symbol (@).
    if (len(password) >= 14) and (num_upper > 0) and (num_lower > 0) and ("!" in password) and ("@" in password):
        return "Strong Password"
    else:
        return "Weak Password"

# Example 1
print(check_pw("MyStrongP@ssword!"))
# Output: Strong Password

# Example 2
print(check_pw("myweakpassword"))
# Output: Weak Password






