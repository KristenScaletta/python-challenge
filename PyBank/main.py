# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#Dictionary to store data

       


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
    maxincrease = 0 
    maxdecrease = 0  
    monthincrease = "a"
    monthdecrease = "b"
    for row in csvreader:
        #print_info(row)
        #Count how many months. 
        if len(row[0]) != 0:
            months = months + 1
        
        # Read each row of data after the header and total the second column. Source: https://www.reddit.com/r/learnpython/comments/5djs0i/summing_columns_in_csv_file/
        total += float(row[1])
        # Calculates mininmum decrease and maximim increase.
        
        if float(row[1]) > float(maxincrease):
            maxincrease = float(row[1])
            monthincrease = str(row[0])
        if float(row[1]) < float(maxdecrease):
            maxdecrease = float(row[1])
            monthdecrease = str(row[0])

 #calculates average change--need formula
    change = (maxdecrease - maxincrease)/total
 #outputs the P&L total. Neet to output to a text file.
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: {change}") #Need formula
    print(f"Greatest Increase in Profits: {monthincrease} (${maxincrease})")
    print(f"Greatest Decrease in Profits: {monthdecrease} ({maxdecrease})")  
       
# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..", "PyBank/Analysis/pybankanalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(f"Financial Analysis")
    csvwriter.writerow(f"------------------")
    csvwriter.writerow(f"Total Months: {months}")
    csvwriter.writerow(f"Total: ${total}")
    csvwriter.writerow(f"Average Change: {change}") #Need formula
    csvwriter.writerow(f"Greatest Increase in Profits: {monthincrease} (${maxincrease})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {monthdecrease} ({maxdecrease})")  
       
