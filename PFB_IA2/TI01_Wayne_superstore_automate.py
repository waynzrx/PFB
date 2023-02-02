from pathlib import Path
import matplotlib.pyplot as plt # ensure you have installed matplotlib before importing it. available in the project brief.
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd()/"superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 3 empty lists to store profit and quantity by each cluster
    cluster1 = [] 
    cluster2 = []
    cluster3 = []

    # append profit and quantity as a list back to each empty list
    for row in reader:
                
        if row[4] == "Cluster 1":
            cluster1.append([row[13], row[14]])
        elif row[4] == "Cluster 2":
            cluster2.append([row[13], row[14]])
        else:
            cluster3.append([row[13], row[14]])

#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1
# variables to store the results

def calculate_profit_and_quantity(cluster1, cluster2, cluster3): 
    """
    This function receives the cluster1, cluster2, cluster3 lists as input,
    it calculates the total profit and total quantity for each cluster
    and returns a tuple containing the results
   
    Parameters:
    cluster1, cluster2, cluster3 : list
        A list of profits and quantities for each cluster
 
    Returns:
    tuple:
        Data structure containing 3 tuple with (total_profit, total_quantity) for each cluster
    """

     # iterate through the three input lists
    for cluster in [cluster1, cluster2, cluster3]:
        # iterate through the items in each cluster
        for item in cluster:
            # extract the profit and quantity values
            profit = float(item[0])
            quantity = int(float(item[1]))

            # check which cluster the item belongs to
            # and sums profit and quantity per cluster
            if cluster == cluster1:
                # add the profit and quantity to the corresponding variables
                cluster1_profit += profit
                cluster1_quantity += quantity
            elif cluster == cluster2:
                # add the profit and quantity to the corresponding variables
                cluster2_profit += profit
                cluster2_quantity += quantity
            else:
                # add the profit and quantity to the corresponding variables
                cluster3_profit += profit
                cluster3_quantity += quantity
                                                                                                          

    # return the results in the form of two tuples
    return ((cluster1_profit, cluster2_profit, cluster3_profit),
            (cluster1_quantity, cluster2_quantity, cluster3_quantity))



# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.

# This code create two lists: cluster_profit and cluster_quantity 
# by extracting the values of 'profit' and 'quantity' respectively, 
# from a list of dictionaries called sales.
# Define the sales data as a list of dictionaries
sales = [{'product': 'A', 'quantity':18362, 'profit':133426},
         {'product': 'B', 'quantity':8716, 'profit':43684},
         {'product': 'C', 'quantity':10524, 'profit':109224}]

# Create a list of profit values using a list comprehension
cluster_profit = [row['profit'] for row in sales]
# Create a list of quantity values using a list comprehension
cluster_quantity = [row['quantity'] for row in sales]



def cluster_report_txt(cluster_profit, cluster_quantity):
    """
    This function writes the profit and quantity for each cluster
    to a file named cluster_report.txt
 
    Parameters:
    profit_report : tuple
        A tuple containing the profit for each cluster
    quantity_report : tuple
        A tuple containing the quantity for each cluster
    """
    # Create the profit report string for each cluster
profit_str_1 = "Cluster 1: ${0:,.1f}".format(cluster_profit[0])
profit_str_2 = "Cluster 2: ${0:,.1f}".format(cluster_profit[1])
profit_str_3 = "Cluster 3: ${0:,.1f}".format(cluster_profit[2])

# Create the quantity report string for each cluster
quantity_str_1 = "Cluster 1: {0:,.1f}".format(cluster_quantity[0])
quantity_str_2 = "Cluster 2: {0:,.1f}".format(cluster_quantity[1])
quantity_str_3 = "Cluster 3: {0:,.1f}".format(cluster_quantity[2])


# This code reads a CSV file called "superstore_transaction.csv" 
# Separates the data into three lists based on a column value, 
# then calculates total profit and total quantity for each list 
# and saves them into a file.
with open("cluster_report.txt", "w") as file:
    file.write("Profit report:\n")
    file.write(profit_str_1 + '\n')
    file.write(profit_str_2 + '\n')
    file.write(profit_str_3 + '\n')
    file.write("\nQuantity report:\n")
    file.write(quantity_str_1 + '\n')
    file.write(quantity_str_2 + '\n')
    file.write(quantity_str_3 + '\n')





#--------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2. 
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python. 
# You will learn about data visulisation in analytics module in year 2. 

cluster_profit = [133426, 43684, 109224] # hardcoded profit by clusters 
cluster_quantity = [18632, 8716, 10524] # hardcoded quantity sold by clusters. 
fig, axs = plt.subplots(2, figsize = (10,7))
fig.suptitle("SuperStore Business Performance")
cluster = ["cluster 1", "cluster 2", "cluster 3"]
axs[0].bar(cluster, cluster_profit)
axs[1].bar(cluster, cluster_quantity)
axs[0].set_xlabel("Profit by Clusters")
axs[1].set_xlabel("Quantity Sold by Clusters")
axs[0].set_ylabel("Profit ($)")
axs[1].set_ylabel("Quantity (000s)")
fig.savefig("cluster_barplot.png") 
plt.imread("cluster_barplot.png")
plt.show() 













