 Your task is to create a Python script that analyzes the votes and calculates each of the following:
o	The total number of votes cast
o	A complete list of candidates who received votes
o	The percentage of votes each candidate won
o	The total number of votes each candidate won
o	The winner of the election based on popular vote.

import pandas as pd

df = pd.read_csv("Resources/election_data.csv")

tot_votes = df.Candidate.count()
winner = df.groupby('Candidate').count().County.idxmax()

x = df.Candidate.unique()
z = df["Candidate"].value_counts()
y = ((z / tot_votes) * 100).round(2)

with open("output.csv",'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {tot_votes}\n")
    f.write("-------------------------\n")
    for i in range(4):
        f.write(f"{x[i]}: {y[i]}% ({z[i]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_votes}")
print("-------------------------")
for i in range(4):
    print(f"{x[i]}: {y[i]}% ({z[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
