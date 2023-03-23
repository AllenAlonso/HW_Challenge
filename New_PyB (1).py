#!/usr/bin/env python
# coding: utf-8

# In[28]:


#!/usr/bin/env python
# coding: utf-8

# In[478]:

#importing whats needed
import csv
import os


#file path for csv
file = os.path.join("Resources/budget_data.csv")


#reading csv file, noting delimiter
with open(file) as csvfile:
    csv = csv.reader(csvfile, delimiter = ",")
    #initializing vars for loop
    csv_header = next(csv)
    total = 0
    change = 0
    dates = []
    porl = []   
    porl += [0]
    # Get your first row
    line_here = next(csv)
    # Setup holder
    holder = int(line_here[1])
    # Month
    dates.append(line_here[0])
    
  
   #looping through csv to get differences in profits for 'porl' list
    for row in csv:
        #adds current date from csv into 'dates' list
        dates.append(row[0])
        #creates list of profit or loss in 'porl' list, keeping the prevsious number as a holder to compare to
        change = int(row[1])-holder
        porl.append(change)
        holder = int(row[1])
        total = total + int(row[1])

#records all desired outputs for printing        
months = len(dates)
total = total + int(line_here[1])
avg_change = sum(porl)/(len(porl)-1)
greatest_inc = max(porl)
greatest_dec = min(porl)
i_inc = porl.index(greatest_inc)
i_dec = porl.index(greatest_dec)
greatest_date_inc = dates[i_inc]
greatest_date_dec = dates[i_dec]


#printing internally
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date_inc} ${greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_date_dec} ${greatest_dec}")

#printing into output file
out = open("Resources/output.txt","w")

x0 = "Financial Analysis"
x1 = "---------------------"
x2 = str(f"Total Months: {months}")
x3 = str(f"Total: ${str(total)}")
x4 = str(f"Average Change: ${round(avg_change,2)}")
x5 = str(f"Greatest Increase in Profits: {greatest_date_inc} (${greatest_inc})")
x6 = str(f"Greatest Decrease in Profits: {greatest_date_dec} (${greatest_dec})")

out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n')


# In[454]:





# In[ ]:





# In[ ]:





# In[387]:





# In[388]:





# In[ ]:





# In[ ]:





# In[ ]:




