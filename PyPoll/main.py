# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll/Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')





#Use CSV module to read CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    #Lists to store data
    candidate_list = []
    total_votes = 0
    candidate_votes = [0, 0, 0, 0, 0, 0]
    percent_votes = [0, 0, 0, 0, 0, 0]
    candidate_number = 0
    votecount = 0
    percent = 0
            
    for row in csvreader:
        

        #counts total number of votes cast
        if len(row[0]) != 0:
            total_votes = total_votes + 1
        
        #makes list of all unique candidates.
        candidate_name = row[2]

        

        if candidate_name not in candidate_list:
            
            candidate_list.append(candidate_name)

        #insert vote count in right spot tied to candidate number. Doesn't yet work
        candidate_number = len(candidate_list)
    

        candidate_number = int(candidate_number) - 1
        votecount = int(candidate_votes[candidate_number]) + 1
        candidate_votes[candidate_number] = votecount 
        votecount = 0
        candidate_number = 0

        list_length = int(len(candidate_list)) 
        
    
       

        
        
       
        
   
    #Establishes dictionary of candidate name and votes           
    
   
    candidate_info = {
             "Name": candidate_list,
            "Votes": candidate_votes,
            "Percent": percent_votes
            }

    
    #Prints Election Results Header and Total Votes
    print(f"Election Results")
    print(f"------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------")
    
    #Prints candidates and individual vote totals
    
    i = 0
    list_length = int(len(candidate_list)) 
    winner = 0
    while list_length > 0:
       
        
        candidate_info["Percent"][i] = candidate_info["Votes"][i]/total_votes * 100
        
        print(f"{candidate_info['Name'][i]}: {float(candidate_info['Percent'][i])}% ({candidate_info['Votes'][i]})")

       #determine winner
        if candidate_info["Votes"][i] > winner:
            winner = candidate_info["Votes"][i]
            winner_name = candidate_info["Name"][i]
        i = i + 1
        list_length = list_length - 1
    
    print(f"------------------")

    #Prints winner
    print(f"Winner: {winner_name}") 
    print(f"------------------")
  
       
