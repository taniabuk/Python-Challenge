import csv
import os
import datetime
import math


total_votes = 0
max_total = 0
current_total = 0
current_candidate = 0
winner = 0

f = open('PollTotals.txt', 'w+')
f = open('PollTotals.txt', 'r+')

currentDir = os.getcwd()

csvfile = os.path.join(currentDir, 'election_data.csv')

# Open and read csv
with open(csvfile, newline="") as csvdata:
    reader = csv.reader(csvdata, delimiter=",")
#Next row in file    
    next(reader, None)

    votes = []
    candidates = []
    
    for row in reader:
        votes.append(float(row[0]))
        candidates.append(str(row[2]))
#Total Votes
        total = len(votes)

print("Election Results")
print("-------------------------------")
print("Total Votes:", total)
print("-------------------------------")

f.write("Election Results \n")
f.write("------------------------ \n")
f.write(f'Total Votes: {total} \n') 
f.write("------------------------ \n")

#Sorting Candidate column
candidates.sort() 

current_total = 1
current_candidate = candidates [0]

#Loop counting each candidate
for i in range (1, len(candidates)):
    if current_candidate == candidates [i]:
        current_total = current_total + 1
    else:
        print(current_candidate, ": ", round(100*(current_total) / total, 2), "%", "(", current_total, ")")
        f.write(f'{current_candidate}: {round(100*(current_total) / total, 2)}% ({current_total}) \n')
        #f.write(f'Greatest Decrease in Profits: {min_date}, (${min_change}).\n')
#Finding Winner       
        if current_total > max_total:
            winner = current_candidate
            max_total = current_total
        current_candidate = candidates [i]
        current_total = 1
print(current_candidate, ": ", round(100*(current_total) / total, 2), "%", "(", current_total, ")")
f.write(f'{current_candidate}: {round(100*(current_total) / total, 2)}% ({current_total}) \n')

if current_total > max_total:
    winner = current_candidate
    max_total = current_total

print("-------------------------------")
print("Winner: ", winner)
print("-------------------------------")

f.write('------------------------ \n')
f.write(f'Winner: {winner} \n')
f.write('------------------------ \n')

f.close() 