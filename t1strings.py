#
# Quotation marks
# as delimeter for strings
#



## single and double quotes
# print("hello world!")
# print('hello world!')


## mix of both single/double or triple!!!
print("What's your name")
print("""I said "we can use 3 quotes" """)
print("""this is how to get single ' using 3 quotes """)


## backslash \ (as escape)
print('What\'s your name? - using single quotes and backslash')



## \n => new line
print("What's\n your\n name?") 
print("What's\nyour\nname?")


## \t => tab
# print ("What's\t  your\t name?")


age = 30 
# data typr integer w value of 30 has been assigned to a variable age 

##conventions 
## (1) camel case notation
##     e.g thisVariableName


##---------------
## assignment =
## concatenate 
# ---------------
# firstname = 'tom'
## let's read this as "string tom" is assigned  (=) to variable firstname

firstname = "tom"
lastname = "mathew"
print(firstname)
print(lastname)
print(firstname + " " + lastname) # NOT reco 

fullname = firstname + " " + lastname 
print(fullname)


# print("tom" == "Tom")

#_________________________
#built-in functions
# len(), type()
#_________________________

print(len(firstname))
print(len(fullname))
print(type(fullname))
print(type(10))
print(type(10))
print(type(10.0))

firstname = "tom"
lastname = "mathew"
fullname = firstname + " " + lastname 

print(firstname[0])
print(firstname[1])
print(firstname[2])
# print(firstname[3])

## notation for slicing 
## ver_name[start]: end_excluding]
## ver_name[start_index : end_index 1]

print(firstname[0:2]) # get fm index 0 to 1
## t [0] m
## 0 [1] 2

print(firstname[-1])

## need to re assign if no need to replace item(s)
firstname = "tom"
lastname = "bom"
# print(firstname)


#age = input("Enter your age:")
#print(type(age))


age_str = "25"
print(type(age_str))

age_int = int(age_str)
print(type(age_int))

age_str2 = "25.50"


name = "tony"
age = 30

print(f"{name} is {age} years old.")
print(f"{name.upper()} is {age/2} years old")





##important 
## .replace() - method  => string method

## replace ALL occurences 
phrase ='This is a string'
print(phrase.replace('s','p'))
print(phrase)

#Another example
profit_day1 = "$262"
profit_day2 = "$762"
profit_day1 = profit_day1.replace("$","")
profit_day2 = profit_day2.replace("$","")

total_profit = float(profit_day1) + float(profit_day2)
print(f"Total profit: ${total_profit}")


