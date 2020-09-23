import os
import csv

print(list_candidates)

# % of votes per candidate & total number of votes per candidate
# % of votes per candidate & total number of votes per candidate, descending

votes_candidate = election_data_df.groupby('Candidate').size().to_frame('counts')
votes_candidate['perc_candidate']= votes_candidate['counts']/votes_candidate['counts'].sum()
votes_candidate.sort_values('perc_candidate', inplace=True, ascending=False)

print(votes_candidate)

# # add % and zero decimals
output = votes_candidate.to_string(formatters={"perc_candidate":'{:,.0%}'.format})
print (output)

# election winner via popular vote
winner = election_data_df['Candidate'].value_counts().idxmax()

print(winner)

# results, every record on new line, rounded 2 decimals for average and 0 decimals for max in min
# results, every record on new line
results = ("Election Results \n"
+ "-------------------------------\n"
+ "Total Votes: " + str(total_votes) + "\n" 
+ "-------------------------------\n"     
+ str(votes_candidate)  + "\n"            
+ output + "\n"            
+ "-------------------------------\n"
+ "Winner: " + winner + "\n"
+ "--------------------------------\n") 

           
@@ -2,7 +2,7 @@
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 147,
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
@@ -16,7 +16,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
@@ -124,7 +124,7 @@
       "9  13870173  Marsh    Correy"
      ]
     },
     "execution_count": 148,
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
@@ -139,7 +139,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
@@ -159,7 +159,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
@@ -179,7 +179,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
@@ -188,8 +188,8 @@
     "text": [
      "            counts  perc_candidate\n",
      "Candidate                         \n",
      "Correy      704200            0.20\n",
      "Khan       2218231            0.63\n",
      "Correy      704200            0.20\n",
      "Li          492940            0.14\n",
      "O'Tooley    105630            0.03\n"
     ]
@@ -200,7 +200,7 @@
    "\n",
    "votes_candidate = election_data_df.groupby('Candidate').size().to_frame('counts')\n",
    "votes_candidate['perc_candidate']= votes_candidate['counts']/votes_candidate['counts'].sum()\n",
    "\n",
    "votes_candidate.sort_values('perc_candidate', inplace=True, ascending=False)\n",
    "print(votes_candidate)\n"
   ]
  },
@@ -213,7 +213,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
@@ -233,14 +233,31 @@
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": []
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            counts perc_candidate\n",
      "Candidate                        \n",
      "Khan       2218231            63%\n",
      "Correy      704200            20%\n",
      "Li          492940            14%\n",
      "O'Tooley    105630             3%\n"
     ]
    }
   ],
   "source": [
    "# add % and zero decimals\n",
    "output = votes_candidate.to_string(formatters={\"perc_candidate\":'{:,.0%}'.format})\n",
    "print (output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
@@ -251,12 +268,12 @@
      "-------------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------------\n",
      "            counts  perc_candidate\n",
      "Candidate                         \n",
      "Correy      704200            0.20\n",
      "Khan       2218231            0.63\n",
      "Li          492940            0.14\n",
      "O'Tooley    105630            0.03\n",
      "            counts perc_candidate\n",
      "Candidate                        \n",
      "Khan       2218231            63%\n",
      "Correy      704200            20%\n",
      "Li          492940            14%\n",
      "O'Tooley    105630             3%\n",
      "-------------------------------\n",
      "Winner: Khan\n",
      "--------------------------------\n",
@@ -265,12 +282,12 @@
    }
   ],
   "source": [
    "# results, every record on new line, rounded 2 decimals for average and 0 decimals for max in min\n",
    "# results, every record on new line\n",
    "results = (\"Election Results \\n\"\n",
    "+ \"-------------------------------\\n\"\n",
    "+ \"Total Votes: \" + str(total_votes) + \"\\n\" \n",
    "+ \"-------------------------------\\n\"     \n",
    "+ str(votes_candidate)  + \"\\n\"            \n",
    "+ output + \"\\n\"            \n",
    "+ \"-------------------------------\\n\"\n",
    "+ \"Winner: \" + winner + \"\\n\"\n",
    "+ \"--------------------------------\\n\") \n",
@@ -280,7 +297,7 @@
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
@@ -314,7 +331,7 @@
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
   "version": "3.7.0"
  }
 },
 "nbformat": 4, 

