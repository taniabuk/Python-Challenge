import csv
import os
import datetime
import math

row_count = 0
min_change = 0
max_change = 0
average_change = 0
total_revenue = 0
current_change = 0
max_date = 0
min_date = 0
change_temp = 0

currentDir = os.getcwd()

csvfile = os.path.join(currentDir, 'budget_data.csv')

# Open and read csv
with open(csvfile, newline="") as csvdata:
    reader = csv.reader(csvdata, delimiter=",")
#Next row in file    
    next(reader, None)

    amount = []
    date = []
    revchange = []

    for row in reader:
        amount.append(float(row[1]))
        date.append(row[0])
        #current_change = float(row[1])

for i in range(1, len(amount)):
    total_date = len(date)
    total = int(sum(amount))
    revchange.append(amount[i] - amount[i-1])

average_change = round(sum (revchange) / len(revchange), 2)
max_change = int(max(revchange))
min_change = int(min(revchange))


for i in range(1, len(amount)):
    change_temp = int (amount[i] - amount[i-1] )
    if max_change ==  change_temp:
        max_date = date[i] 
    if min_change ==  change_temp:
        min_date = date[i] 
  

    
print("Financial Analysis")
print("++++++++++++++++++++")
print("Total Months:", total_date)
print("Total: $", total)
print("Average Change: $", average_change)
print("Greatest Increase in Profits: ", max_date, "($",max_change,")")
print("Greatest Decrease in Profits: ", min_date, "($",min_change,")")

f = open('BankTotals.txt', 'w+') 
f = open('BankTotals.txt', 'r+') 
 
f.write("Financial Analysis \n")
f.write("+++++++++++++++++++++++ \n")
f.write(f'Total Months: {total_date}.\n')
f.write(f'Total: ${total} \n')
f.write(f'Average Change: ${average_change}.\n')
f.write(f'Greatest Increase in Profits: {max_date}, (${max_change}).\n')
f.write(f'Greatest Decrease in Profits: {min_date}, (${min_change}).\n')
f.close() 
