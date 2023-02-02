##### Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "functions and loops"
#name = Wayne Teo Ren Xian
#np_email = s10240130@connect.np.edu.sg
#student_id = S10240130
#class_number = TI01

#-------------------------------- Q1 ------------------------------------#
# Write a program that allow users to calculate distance, time, speed.
#------------------------------------------------------------------------#

# The program should include 3 functions:

    #### speed_function() ####
    # speed = distance/time

    #### distance_function() ####
    # distance = time * speed

    #### time_function() ####
    # time = distance/speed

# The functions will round float to 2 decimal places.

# When the 3 functions are executed, they should display and return:

    ##### Example of speed_function() #####
    ## Enter distance (in km): 10
    ## Enter time taken (in hours): 2
    ## Based on the distance and time input, the calculated speed (km/hr) = 5.0
    
    ##### Example of distance_function() #####
    ## Enter time taken (in hr): 2
    ## Enter speed (in km/hr): 5
    ## Based on the speed and time input, the calculated distance (km) =  10.0

    ##### Example of time_function() #####
    ## Enter distance (in km): 10
    ## Enter speed (in km/hr): 5
    ## Based on the speed and distance input, time taken (in hr) = 2.0

# Execute the functions with the following 3 lines 
# NOTE: these 3 lines should be the last 3 lines after and outside all functions
# print(speed_function())
# print(distance_function())
# print(time_function())


 # time = distance/speed
def speed_function():
    """
    - Function calculates speed based on input of distance and time
    """
    time = input("Enter the time taken (in hours): ")
    distance= input("Enter the distance (in km): ")
#convert user input into float
    distance = float(distance)
    time = float(time)
    speed_function = distance/time 
    print(f"based on the distance and time input, the calculated speed (km/hr) = {speed_function}")

    
def distance_function():
    """
    - Function calculates distance based on input of speed and time
    """
    speed = input("Enter the speed (in km/h): ")
    time = input("Enter the time taken (in hours): ")
#convert user input into float
    speed = float(speed)
    time = float(time)
    distance_function = time * speed 
    print(f"based on the speed and time input, the calculated distance (km) = {distance_function} ")
    
    


def time_function():
    """
    - Function calculates time taken based on input of distance and speed
    """
    distance = input("Enter the distance (in km): ")
    speed = input("Enter the speed (in km/h): ")
#convert user input into float 
    distance = float(distance)
    speed = float(speed)
    time_function = distance/speed 
    print(f"Based on the distance and speed input, time taken (in hr) = {time_function}")
    


print(speed_function())
print(distance_function())
print(time_function())

