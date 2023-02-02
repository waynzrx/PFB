## CPF contribution rates By Employer from 1 Jan 2022
## Employee's Age (years)   CPF Rate by Employer (%)
##=======================   ==========================
## 55 and below                  17
## Above 55 to 60                14
## Above 60 to 65                10
## Above 65 to 70                 8
## Above 70                     7.5
 
## Write a function: co_cpf_rate() to determine Employer's 
## CPF contribution rate based employee's age
 
## when this line is executed (outside function):
## print(co_cpf_rate())
## user will be prompted to enter employee's age in years
## output will then show the rate.
##
## e.g. if user enters 55, output will be:
## Employer's CPF contribution rate is 17%

age = float(input("Enter employee's age (in years): "))

if age <= 55:
    ecc_rate = "Employer's CPF contribution is 17%"
elif age <= 60:
    ecc_rate = "Employer's CPF contribution is 14%" 
elif age <= 65:
    ecc_rate = "Employer's CPF contribution rate is 10%"
elif age <= 70: 
    ecc_rate = "Employer's CPF contribution rate is 8%"
else:
    ecc_rate = "Employer's CPF contribution rate is 7.5%"

print(ecc_rate)


    


