#Library "os" has functions to build file path based on operating system
import os
#Library "csv" has functions to establish a connection to a .csv file
import csv

#Initializing list "data" to hold data being read in from source file
data=[]

#This function creates a path to the source file
budget_data=os.path.join(".","budget_data.csv")
with open(budget_data,"r",newline="",encoding="utf-8") as file:
    #iterable object that helps read in source file
    read_obj=csv.reader(file,delimiter=",")
    
    #iterating over the csv.reader object
    for line in read_obj:
        data.append(line)

#excluding the first line, which contains column headers        
data=data[1:]

#Initializing lists to store profit/loss data, and corresponding dates
#Initializing another list to hold profit/loss change between months

profit_loss=[]
date=[]
profit_loss_change=[]

#iterating over the data list
for i in range(len(data)):
    #Coercing profit/loss values to numeric and appending to list
    profit_loss.append(float(data[i][1]))
    
    #Appending dates to list
    date.append(data[i][0])
    
    #In order to observe a change we need to start at index 1, the second observation
    if i>0:
        #appending the profit/loss change value to list
        profit_loss_change.append(profit_loss[i]-profit_loss[i-1])

#Printing Results to screen
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(len(date)))
print("Total: $" + str(sum(profit_loss)))
print("Average Change: $" + str(round(sum(profit_loss_change)/len(profit_loss_change),2)))
print("Greatest Increase in Profits: " + str(date[profit_loss.index(max(profit_loss))]) + " ($" + str(max(profit_loss)) + ")")
print("Greatest Decrease in Profits: " + str(date[profit_loss.index(min(profit_loss))]) + " ($" + str(min(profit_loss)) + ")")

#Function creates a Operating System dependent file path
output_file=os.path.join(".","financial_results.txt")

with open(output_file, "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-----------------------------", file=text_file)
    print("Total Months: " + str(len(date)), file=text_file)
    print("Total: $" + str(sum(profit_loss)), file=text_file)
    print("Average Change: $" + str(round(sum(profit_loss_change)/len(profit_loss_change),2)), file=text_file)
    print("Greatest Increase in Profits: " + str(date[profit_loss.index(max(profit_loss))]) + " ($" + str(max(profit_loss)) + ")", file=text_file)
    print("Greatest Decrease in Profits: " + str(date[profit_loss.index(min(profit_loss))]) + " ($" + str(min(profit_loss)) + ")", file=text_file)
