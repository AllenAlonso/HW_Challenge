#!/usr/bin/env python
# coding: utf-8

# In[478]:

#importing whats needed
import pandas as pd
import csv
import os

#path for csv
file = "Resources/budget_data.csv"
df = pd.read_csv(file)

#immediately finding month count and sum of profit/losses
months = df["Date"].count()
total = df["Profit/Losses"].sum()

#couldnt loop properly with pandas so opening with the csv import
with open(file) as csvfile:
    csv = csv.reader(csvfile, delimiter = ",")
    #initializing vars for loop
    csv_header = next(csv)
    change = 0
    dates = []
    porl = []
    
    # Get first row so looping doesn't start at first value of data
    line_here = next(csv)
    # Setup holder
    holder = int(line_here[1])
    
    #append dates to even out list
    dates.append(line_here[0])
    #initializing profit or loss with 0 in starting position
    porl += [0]
  
   #loops through csv row by row, appending column values into dates or porl list
    for row in csv:
        dates.append(row[0])
        #math for profit/loss difference
        change = int(row[1])-holder
        porl.append(change)
        holder = int(row[1])
        
#re-containing lists into dataframe        
porl_df = pd.DataFrame(
                      {"Date":dates,
                       "Profit/Loss":porl})
#gathers max with pandas, can also be done by getting min or max from porl list
greatest_inc = porl_df["Profit/Loss"].max()
greatest_dec = porl_df["Profit/Loss"].min()
#sorts list into descending and ascending df
sorted_porl = porl_df.sort_values("Profit/Loss",ascending=False)
sorted_porl2 = porl_df.sort_values("Profit/Loss",ascending=True)
#records min and max into variable(top of each list)
greatest_date_inc = sorted_porl.iloc[0,0]
greatest_date_dec = sorted_porl2.iloc[0,0]
#math for average change
avg_change = porl_df["Profit/Loss"].sum()  / (len(porl)-1) 

#prints analysis
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date_inc} ${greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_date_dec} ${greatest_dec}")

#creates output file
out = open("Resources/output.txt","w")

x0 = "Financial Analysis"
x1 = "---------------------"
x2 = str(f"Total Months: {months}")
x3 = str(f"Total: ${str(total)}")
x4 = str(f"Average Change: ${round(avg_change,2)}")
x5 = str(f"Greatest Increase in Profits: {greatest_date_inc} (${greatest_inc})")
x6 = str(f"Greatest Decrease in Profits: {greatest_date_dec} (${greatest_dec})")
#writes previous vars into output file
out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n')


