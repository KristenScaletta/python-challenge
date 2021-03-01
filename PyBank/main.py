# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#Lists to store data



#Use CSV module to read CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

   
    total = 0
    months = 0
    #i = 0
    list = []
      
    for row in csvreader:
        # Count how many months. 
        if len(row[0]) != 0:
            months = months + 1
        
        # Read each row of data after the header and total the second column. Source: https://www.reddit.com/r/learnpython/comments/5djs0i/summing_columns_in_csv_file/
        total += float(row[1])
    #need to work on this. Doesn't pull min and max.
        currentcount = row[1]
        list.append(currentcount)
        currentcount=0
        #max = max(list)
        #if int(row[1]) == int(max):
         #   maxmonth = row[0]
   #print(list)
    

    #outputs the P&L total
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits: (${max(list)})")
    #print(f"Greatest Decrease in Profits: {maxmonth} ${min(list)}")  
       
