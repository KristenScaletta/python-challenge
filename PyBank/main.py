# Import the os module
import os

# Module for reading CSV files (Note..I could not goet 'Pybank', 'Resources', 'filename' to work on my machine. Advice would be appreciated.)
import csv

csvpath = os.path.join('..', 'PyBank/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#Use CSV module to read CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    #Declare variables
    total = 0
    months = 0
    maxincrease = 0 
    maxdecrease = 0  
    monthincrease = "a"
    monthdecrease = "b"
    row_list = []
    avg_change = 0
    
    #Reads each row in the open CSV file
    for row in csvreader:
        
        
        #Calculates total. Reads each row of data and totals the second column. Source: https://www.reddit.com/r/learnpython/comments/5djs0i/summing_columns_in_csv_file/
        total += float(row[1])
        
        # Calculates mininmum decrease and maximim increase.
        
        if float(row[1]) > float(maxincrease):
            maxincrease = float(row[1])
            monthincrease = str(row[0])
        if float(row[1]) < float(maxdecrease):
            maxdecrease = float(row[1])
            monthdecrease = str(row[0])

        row_list.append(row[1])
 
    #calculates total months
    months = len(row_list)
    
    #calculates average change
    start = row_list[0]
    end = row_list[months - 1]
    numerator = float(end) - float(start)
    avg_change = float(numerator)/float(months)

#outputs the requested data in a terminal.
    
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: {avg_change}") 
    print(f"Greatest Increase in Profits: {monthincrease} (${maxincrease})")
    print(f"Greatest Decrease in Profits: {monthdecrease} ({maxdecrease})")  
       
#Outputs the requested data in a new text file. Source: https://www.geeksforgeeks.org/reading-writing-text-files-python/
# Dependencies
import os

# Specify the file to write to
output_path = os.path.join("..", "PyBank/Analysis/pybankanalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

#Adds output to the new text file or overwrites file with the below outputs.
    txtfile.writelines(f"Financial Analysis\n")
    txtfile.writelines(f"------------------\n")
    txtfile.writelines(f"Total Months: {months}\n")
    txtfile.writelines(f"Total: ${total}\n")
    txtfile.writelines(f"Average Change: {avg_change}\n") #Need formula
    txtfile.writelines(f"Greatest Increase in Profits: {monthincrease} (${maxincrease})\n")
    txtfile.writelines(f"Greatest Decrease in Profits: {monthdecrease} ({maxdecrease})\n")  
