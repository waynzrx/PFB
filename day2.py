#####  Store your name, email, student_id and class_number as STRINGS #####
#ind_assign1 = "day 2"
#name = Wayne Teo Ren Xian
#np_email = s10240130@connect.np.edu.sg
#student_id = S10240130B
#class_number = TI01

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

#QUESTION 1
def waist_hip():
    """
    Calculate a person's waist-to-hip ratio (WHR) and determine their health risk.
    
    This function prompts user to enter their gender, waist measurement, and hip measurement.
    It then calculates the WHR using the waist measurement divided by the hip measurement.
    The function then determines the user's health risk based on their gender and WHR, and returns
    the health risk level.
    """
    # Ask the user for their gender
    gender = input("What is your gender (M or F)? ")
    
    # Ask the user for their waist and hip measurements
    waist = float(input("What is your waist measurement (in inches)? "))
    hips = float(input("What is your hip measurement (in inches)? "))
    
    # Calculate the WHR by dividing the waist measurement by the hip measurement
    whr = waist / hips

    # Determine the health risk based on the gender and WHR
    if gender == "M":
        # If the WHR is below 0.9, the health risk is low
        if whr < 0.9:
            risk = "Low"
        # If the WHR is below 1.0 but above or equal to 0.9, the health risk is moderate
        elif whr < 1.0:
            risk = "Moderate"
        # If the WHR is 1.0 or above, the health risk is high
        else:
            risk = "High"
    
    # If the person's gender is female
    elif gender == "F":
        # If the WHR is below 0.8, the health risk is low
        if whr < 0.8:
            risk = "Low"
        # If the WHR is below 0.9 but above or equal to 0.8, the health risk is moderate
        elif whr < 0.9:
            risk = "Moderate"
        # If the WHR is 0.9 or above, the health risk is high
        else:
            risk = "High"
    
    # Return the calculated WHR and health risk
    return f"Your Health Risk Level: {risk}"

# Test the function
print(waist_hip())




#QUESTION 2 
def calc_age(age):
  """
  1. This function converts an age in years to the equivalent age in days.
  2. This function returns an error message if the input age is negative.
  """

  # Check if the age is less than 0
  if age < 0:
    # If the age is negative, return an error message
    return "Age cannot be negative a number"
  else:
    # If the age is a postive number, calculate the equivalent age in days 
    # and return a string with the result
    return f"{age} years is equal to {age * 365} days"

# Test the calc_age function with different input values
print(calc_age(40)) 
# Output: 40 years is equal to 14600 days

print(calc_age(-10)) 
# Output: Age cannot be negative a number




