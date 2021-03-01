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

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   
    total = 0
    months = 0
    #i = 0
    list = []
      
    for row in csvreader:
        # Count how many months by counting length of each row to convert to int. The limitation of this approach is the string must contain the same amount of characters, as it does in this data set. I'd love advice on how to count rows that contain a string in a more streamlined manner that is more broadly applicable.
        months += len(row[0])
        
        # Read each row of data after the header and total the second column. Source: https://www.reddit.com/r/learnpython/comments/5djs0i/summing_columns_in_csv_file/
        total += float(row[1])
    #need to work on this. Doesn't pull min and max.
        currentcount = row[1]
        list.append(currentcount)
        currentcount=0
        max = max(list)
        if int(row[1]) == int(max):
            maxmonth = row[0]
   #print(list)
    #calculates the total months by dividing the months by the number of characters in the string (which in this case works since each string in the first column has 8 characters.)
    total_months = int(((months) / 8))

    #outputs the P&L total
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits: {maxmonth} (${max(list)})")
    print(f"Greatest Decrease in Profits: ${min(list)}")  
       
