#library needed for csv.reader function
import csv
#initializing a list to capture data
data=[]
#defining path to data source
budget_data="c:/Users/david/OneDrive/DV/HomeWork/HW_3_Py_Me_Up_Charlie/python-challenge/PyBank/budget_data.csv"
#establishing a connection to data source and reading in data
with open(budget_data,"r",newline="",encoding="utf-8") as file:
    read_obj=csv.reader(file,delimiter=",")
    #iterating over the csv.reader object read_obj to populate "data"
    for something in read_obj:
        data.append(something)
        
#Skipping headers (index:0)
data=data[1:]
#declaring variables to store date, profit/loss, and profit/loss change data
profit_loss=[]
date=[]
profit_loss_change=[]

#isolating the data in "data" list into separate lists for computation and display
for i in range(len(data)):
    profit_loss.append(float(data[i][1]))
    date.append(data[i][0])
    #there is no change in profit/loss until the second row
    if i>0:
        profit_loss_change.append(profit_loss[i]-profit_loss[i-1])

#outputting required results to screen using print() and concatenation
print("Financial Analysis")
print("-----------------------------")
#coercing number to string using str() for concatenation
print("Total Months: " + str(len(date)))
#applying sum function over a numeric vector
print("Total: $" + str(sum(profit_loss)))
#applying round function to 2 decimal places
print("Average Change: $" + str(round(sum(profit_loss_change)/len(profit_loss_change),2)))
#using index method to locate index of maximum/minimum values
print("Greatest Increase in Profits: " + str(date[profit_loss.index(max(profit_loss))]) + " ($" + str(max(profit_loss)) + ")")
print("Greatest Decrease in Profits: " + str(date[profit_loss.index(min(profit_loss))]) + " ($" + str(min(profit_loss)) + ")")

