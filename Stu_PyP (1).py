#!/usr/bin/env python
# coding: utf-8

# In[82]:


import csv
import os

#file path into var
file = os.path.join("Resources/election_data.csv")


with open(file) as csvfile:
    csv = csv.reader(csvfile, delimiter = ",")
    
    #initializing vars
    total_votes = 0
    percentages = []
    candidates = []
    cand_votes = {}
    winning_votes = 0
    holder = 0
    #skips header
    header = next(csv)
    
    
    for row in csv:
        #loops for total votes
        total_votes += 1
        
        #grabs current candidate from row
        candidate = row[2]
        
         #appending unique candidate into candidates list
        if candidate not in candidates:
            candidates.append(candidate)
            #initializes candidate with zero votes into cand_votes dictionary
            cand_votes[candidate] = 0
            
        #adds votes for current candidate into proper dict
        cand_votes[candidate] = cand_votes[candidate] + 1
        
        

    #getting percentages and winners by looping through dict 'cand_votes'
    for x in cand_votes:
        percentages.append(cand_votes[x]/total_votes *100)
        
        #checking for winnter by comparing votes
        holder = cand_votes[x]
        if holder > winning_votes:
            winner = x
            winning_votes = cand_votes[x]
    


#printing to terminal
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"{candidates[0]}: {round(percentages[0],3)}% ({cand_votes[candidates[0]]})")
print(f"{candidates[1]}: {round(percentages[1],3)}% ({cand_votes[candidates[1]]})")
print(f"{candidates[2]}: {round(percentages[2],3)}% ({cand_votes[candidates[2]]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

#printing out to text file
out = open("Resources/output.txt","w")

x0= "Election Results"
x1= "----------------------"
x2= str(f"Total Votes: {total_votes}")
x3= "----------------------"
x4= str(f"{candidates[0]}: {round(percentages[0],3)}% ({cand_votes[candidates[0]]})")
x5= str(f"{candidates[1]}: {round(percentages[1],3)}% ({cand_votes[candidates[1]]})")
x6= str(f"{candidates[2]}: {round(percentages[2],3)}% ({cand_votes[candidates[2]]})")
x7= "----------------------"
x8= str(f"Winner: {winner}")
x9= "----------------------"

out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n{x6}\n{x7}\n{x8}\n{x9}\n')


# In[ ]:




