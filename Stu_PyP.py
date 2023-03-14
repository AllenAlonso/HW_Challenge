#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import csv
import os

file = "Resources/election_data.csv"
df = pd.read_csv(file)



total_votes = df["Ballot ID"].count()
candidates = df["Candidate"].unique()

percentages = df["Candidate"].value_counts()/total_votes *100

percentages_df = pd.DataFrame({"Percentage": percentages})
percentages_df = percentages_df.reset_index()

votes = pd.DataFrame(df["Candidate"].value_counts())
votes = votes.reset_index()
votes = votes.sort_values("Candidate",ascending=False)

winner = votes.iloc[0,0]

cand1 = votes.iloc[1,0]
cand2 = votes.iloc[0,0]
cand3 = votes.iloc[2,0]

perc1 = percentages_df.iloc[1,1]
perc2 = percentages_df.iloc[0,1]
perc3 = percentages_df.iloc[2,1]

vote1 = votes.iloc[1,1]
vote2 = votes.iloc[0,1]
vote3 = votes.iloc[2,1]


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

out.write(f'{x0}\n{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x5}\n{x6}\n{x7}\n{x8}\n{x9}\n')


# In[ ]:




