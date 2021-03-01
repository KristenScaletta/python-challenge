# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll/Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#Lists to store data
candidate_list = []
listtoprint = []


#Use CSV module to read CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   
    total_votes = 0
      
    for row in csvreader:
        #counts total number of votes cast
        if len(row[0]) != 0:
            total_votes = total_votes + 1
        
        #makes list of all unique candidates. This doesn't yet work.
        candidate_list = row[2]
        candidate = row[2]
        if candidate not in candidate_list:
            listtoprint.append(candidate)
        #append to list only if not already in it.

    #outputs the P&L total
    print(f"Election Results")
    print(f"------------------")
    print(f"{listtoprint}: ")
    print(f"Total Votes: {total_votes}")
    print(f"------------------")
    print(f"------------------")
    print(f"Winner: ")  
       
