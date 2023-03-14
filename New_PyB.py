#!/usr/bin/env python
# coding: utf-8

# In[478]:


import pandas as pd
import csv
import os

file = "Resources/budget_data.csv"
df = pd.read_csv(file)

months = df["Date"].count()
total = df["Profit/Losses"].sum()

with open(file) as csvfile:
    csv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv)
    change = 0
    dates = []
    porl= []
    holder = 0
    
    for row in csv:
        dates.append(row[0])
        
        change = int(row[1])-holder
        porl.append(change)
        holder = int(row[1])
porl_df = pd.DataFrame(
                      {"Date":dates,
                       "Profit/Loss":porl})

greatest_inc = porl_df["Profit/Loss"].max()
greatest_dec = porl_df["Profit/Loss"].min()

sorted_porl = porl_df.sort_values("Profit/Loss",ascending=False)
sorted_porl2 = porl_df.sort_values("Profit/Loss",ascending=True)
greatest_date_inc = sorted_porl.iloc[0,0]
greatest_date_dec = sorted_porl2.iloc[0,0]
avg_change = porl_df["Profit/Loss"].mean()   


print("Financial Analysis")
print("----------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date_inc} ${greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_date_dec} ${greatest_dec}")

out = open("Resources/output.txt","w")

x0 = "Financial Analysis"
x1 = "---------------------"
x2 = str(f"Total Months: {months}")
x3 = str(f"Total: ${str(total_pl)}")
x4 = str(f"Average Change: ${round(avg_change,2)}")
x5 = str(f"Greatest Increase in Profits: {greatest_date_inc} (${greatest_inc})")
x6 = str(f"Greatest Decrease in Profits: {greatest_date_dec} (${greatest_dec})")

out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n')


# In[453]:





# In[454]:





# In[ ]:





# In[ ]:





# In[387]:





# In[388]:





# In[ ]:





# In[ ]:





# In[ ]:




