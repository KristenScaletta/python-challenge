# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll/Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#Variable and disctionaries to store data
total_votes = 0
candidate_dict={}
candidate_percent_dict = {}

#Use CSV module to read CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    for row in csvreader:
        #calculates total votes
        total_votes = total_votes + 1
        #calculates votes per candidate. Source: Mohammad's assistance.
    
        candidate = row[2]
        if candidate in candidate_dict:
            candidate_dict[candidate] += 1
        else:
            candidate_dict[candidate] = 1
        
        #calculates percentage of votes per candidate
        candidate_percent_dict[candidate] = f"{round(candidate_dict[candidate] / total_votes * 100, 2)}"

#prints results
print(f"Election Results")
print(f"------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------")
winner_votes = 0
#finds results for each candidate in the dictionaries
for candidate in candidate_dict and candidate_percent_dict:
    print(f"{candidate}: {candidate_dict[candidate]}, {candidate_percent_dict[candidate]}%") 
    #calculates winner
    if candidate_dict[candidate] > winner_votes:
        winner_votes = candidate_dict[candidate]
        winner = candidate
#prints winner and spaces
print(f"------------------")
print(f"The winner is: {winner}")
print(f"------------------")
  
#Outputs the requested data in a new text file. Source: https://www.geeksforgeeks.org/reading-writing-text-files-python/
# Dependencies
import os

# Specify the file to write to
output_path = os.path.join("..", "PyPoll/Analysis/pypollanalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

#Adds output to the new text file or overwrites file with the below outputs. Same as print above.
    txtfile.writelines(f"Election Results\n")
    txtfile.writelines(f"------------------\n")
    txtfile.writelines(f"Total Votes: {total_votes}\n")
    txtfile.writelines(f"------------------\n")
    winner_votes = 0
    for candidate in candidate_dict and candidate_percent_dict:
        txtfile.writelines(f"{candidate}: {candidate_dict[candidate]}, {candidate_percent_dict[candidate]}%\n") 
        if candidate_dict[candidate] > winner_votes:
            winner_votes = candidate_dict[candidate]
            winner = candidate
    txtfile.writelines(f"------------------\n")
    txtfile.writelines(f"The winner is: {winner}\n")
    txtfile.writelines(f"------------------\n")
