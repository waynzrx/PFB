#Q1 - nested List - ----------------------#
#=========================================#
## An exchange facilitates trading of securties.
## Part of its revenue includes collecting trading fees for each transaction.
## Given a nested list `trade_data_list`, the 
## elements in each sub-list contains:
## 1. The name of exchange
## 2. The number of trades
## 3. The trading fee per trade
 
trade_data_list = [['FTX', 22244, 1.4],['Hahanance', 888666, 2],['Crynance', 333777, 1.8]]
 
## Write a function `tt_summary` with one parameter, `selection`.
##
## When "numtrades" is supplied to the parameter, 
## the function will return the total number of trades across all the exchanges.
##
## When "income" is supplied to the parameter, 
## the function will return the total trading fees collected across all the exchanges.
##
## It will return `not valid entry` for any other values supplied to the parameter.
##
## Trading fees collected is calculated by : number of trades x trading fee per trade
 
## Execute with these lines (i.e. put these in main program outside function):
## print(tt_summary("numtrades"))
## print(tt_summary("income"))
## print(tt_summary("whatever"))

trade_data_list = [['FTX', 22244, 1.4],
['Hahanance', 888666, 2],
['Crynance', 333777, 1.8]]

def tt_summary(selection):
    num_trades = 0
    income = 0
    for exchange in trade_data_list: num_trades += exchange[1]
    income += exchange[1] * exchange[2]
    if selection == "numtrades":
        return num_trades 
    elif selection == income:
        return income
    else:
        return "not valid entry"

    print(tt_trades("num_trades"))
    print(tt_trades("income"))
    print(tt_trades("whatever"))
    
    