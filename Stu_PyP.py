#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import csv
import os

#path to csv file
file = "Resources/election_data.csv"
df = pd.read_csv(file)


#using pandas to get a sense of all  totals
total_votes = df["Ballot ID"].count()
percentages = df["Candidate"].value_counts()/total_votes *100

#re-frames percentages as its own df, reset index in order to put canditate name as column for iloc
percentages_df = pd.DataFrame({"Percentage": percentages})
percentages_df = percentages_df.reset_index()

#gets total votes for each candidate, reset index from greatest to lowest
votes = pd.DataFrame(df["Candidate"].value_counts())
votes = votes.reset_index()
votes = votes.sort_values("Candidate",ascending=False)

#gets max for the organized votes df
winner = votes.iloc[0,0]

#recording all candidates in specified order into vars
#could likely instead try to loop to generalize the csv reading, but since we have the format this works
cand1 = votes.iloc[1,0]
cand2 = votes.iloc[0,0]
cand3 = votes.iloc[2,0]

#recording all percentages in specified order into vars
perc1 = percentages_df.iloc[1,1]
perc2 = percentages_df.iloc[0,1]
perc3 = percentages_df.iloc[2,1]

#recording all vote numbers in specified order into vars
vote1 = votes.iloc[1,1]
vote2 = votes.iloc[0,1]
vote3 = votes.iloc[2,1]

#printing information
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"{cand1}: {round(perc1,3)}% ({vote1})")
print(f"{cand2}: {round(perc2,3)}% ({vote2})")
print(f"{cand3}: {round(perc3,3)}% ({vote3})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

#creating output file
out = open("Resources/output.txt","w")

x0= "Election Results"
x1= "----------------------"
x2= str(f"Total Votes: {total_votes}")
x3= "----------------------"
x4= str(f"{cand1}: {round(perc1,3)}% ({vote1})")
x5= str(f"{cand2}: {round(perc2,3)}% ({vote2})")
x6= str(f"{cand3}: {round(perc3,3)}% ({vote3})")
x7= "----------------------"
x8= str(f"Winner: {winner}")
x9= "----------------------"

#writing into the text file with previous x vars
out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n{x6}\n{x7}\n{x8}\n{x9}\n')






