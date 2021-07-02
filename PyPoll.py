#!/usr/bin/env python
# coding: utf-8

#Create analysis folder in election-analysis.
##Commented out after creation to avoid error.
###new_dir = "analysis"
###os.mkdir(new_dir)

import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate option list.
candidate_options = []
# Candidate option and vote dictionary.
candidate_votes = {}

#1. Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2. Track the largetst county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(reader)
    
    # For each row in the CSV file.
    for row in reader:
        
        # Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        #3. Extract the country name from each row.
        county_name = row[1]
        
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)            
            # Begin tracking that candidate's vote count, set to 0.
            candidate_votes[candidate_name] = 0            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        #4a. Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            #4b. Add the existing county to the list of counties.
            county_list.append(county_name)           
            #4c. Begin tracking the county's vote count.
            county_votes[county_name] = 0           
        #5. Add a vote to that county's vote count.
        county_votes[county_name] += 1        
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
            
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #6a. Write a for loop to get the county from the county dictionary.
    print(f"\nCounty Votes:\n")
    txt_file.write(f"\nCounty Votes:\n")
    for county_name in county_votes:
        #6b. Retrieve the county vote count.
        county_count = county_votes[county_name]
        #6c. Calculate the percentage of votes for the county.
        county_percentage = float(county_count) / float(total_votes) * 100
        #6d. Print the county results to the terminal.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county_count:,})\n")
        print(county_results)
        #6e. Save the county votes to a text file.
        txt_file.write(county_results)   
        
        #6f. Write an if statement to determine the winning county and get its vote count.
        if (county_count > winning_county_count) and (county_percentage > winning_county_percentage):
            winning_county_count = county_count
            winning_county_percentage = county_percentage
            winning_county = county_name

    #7. Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    

    #8. Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)       
    
    #Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        
        
        #Determine winning vote count and candiate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print the winner result
    winning_candidate_summary = (
        f"\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    

    # Print the total votes.
    #print(total_votes)
    # Print the candidate list.
    #print(candidate_options)
    # Print the candidate vote dictionary
    #print(candidate_votes)
    #Print winning candidate, vote count and percentage to terminal.






