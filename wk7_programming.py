
    

## Binance Coin, or BNB, is a crypto currency
## that is traded on major crypto exchanges 
## write a program using a for loop 👀👀to calculate the final price of BNB
## if it increases at a fixed % for a no. of days in a row,
## based on following:
## c_price  => current price of BNB
## p_inc    => % increase (in decimals)
## inc_days => cumulative days of increase in price at p_inc
##
## Example, if we use these values:
# c_price = 300
# p_inc = 0.2
# inc_days = 7
## we should get: 
## $1,074.95
##
## BUT program shd work for other
## values for c_price, p_inc and inc_days too.

c_price  = 300
p_inc = 0.2 
inc_days = 7
#while c_price==300:
    #Futurevalue = c_price * (1+p_inc)**7 
    #print(Futurevalue)

for days in range(inc_days):
    c_price = c_price * (1+p_inc)

print(f"${c_price:,.2f}")


##====================================================
## write a program wih a function, to_the_moon() with 
## 3 parameters to perform the above
##
## the 3 parameters are:
## c_price  => current price BNB
## p_inc    => % increase (in decimals)
## inc_days => cumulative days of increase in price at p_inc
## 
## when this line is executed in the program (outside the function),
## with these nos. 300, 0.20 and 7 for c_price, p_inc, inc_days
## respectively, for example:
## print(to_the_moon(300, 0.2, 7))
##
## the output should be:
## The price of BNB will be $1,074.95
##
## NOTE: an alternative way to write the above is:
## print(to_the_moon(c_price=300, p_inc=0.2, inc_days=7))
##==========================================================

def to_the_moon(c_price, p_inc, inc_days):
    """"""
    """"""
    for days in range(inc_days): 
         c_price = c_price * (1+p_inc)
         Futurevalue = c_price * (1+p_inc)**inc_days 
         return(f"The price of BNB will be ${Futurevalue:,.2f}")


print(to_the_moon(300,0.2,7))



