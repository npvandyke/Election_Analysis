#The data we need to retrieve: 
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on the popular vote 

#Add our dependencies. 
import csv
import os
# Assign a variable to load a file from a direct path. 
file_to_load = 'Resources/election_results.csv'
# Assign a variable to save the file given indirect access. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results 
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read and print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the election\n"
    #"-------------------------\nArapahoe\nDenver\nJefferson")