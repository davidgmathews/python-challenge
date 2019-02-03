#library csv needed for csv.reader function
#library os needed for path generation
import csv
import os

#initializing a list to capture data
data=[]

#defining path to data source
election_data=os.path.join(".","election_data.csv")

print(election_data)

#establishing a connection to data source and reading in data
with open(election_data,"r",newline="",encoding="utf-8") as file:
    read_obj=csv.reader(file,delimiter=",")
    
    #iterating over the csv.reader object read_obj to populate "data"
    for something in read_obj:
        data.append(something)

#Skipping headers (index:0)
data=data[1:]

#Counting total votes
total_votes=len(data)

#Initializing dictionary to store vote tally by candidate
#Keys will be candidate names, and values will be vote tally for the respective candidate
vote_count_dict={}

#iterating over data object which is a list of vote count lists
for i in range(len(data)):
    
    #if the candidate exists as a key in the dictionary, we want to increment his/her vote count
    if data[i][2] in vote_count_dict:
        vote_count_dict[data[i][2]]=vote_count_dict[data[i][2]]+1
    else:
        
        #if the candidate does not exist as a key in the dictionary, 
        #we want to create a new key under his/her name and assign 1 vote
        vote_count_dict[data[i][2]]=1

#Creating a vote count list from the vote_count_dict dictionary
#Purpose of converting dictionary to list is to make identifying winner easier
#We will identify winner based on the max votes and using index function to find location of max votes

#Initializing list
vote_count_list=[]

#First element of this list will contain candidate names
vote_count_list.append(list(vote_count_dict.keys()))

#Second element of this list will contain vote tallies
vote_count_list.append(list(vote_count_dict.values()))

#identifying the winner based on total vote
winner=vote_count_list[0][vote_count_list[1].index(max(vote_count_list[1]))]

#Creating another dictionary to store candidate names, vote tally, and percentage votes received
#Having these metrics organized in dictionary enables easier printing of results

#Initialzing a new dictionary
results_dict={}
for key in vote_count_dict:
    results_dict[key]={"Vote_Count":vote_count_dict[key],"Vote_Percentage":round(vote_count_dict[key]/total_votes*100,3)}

#This section will print results to screen

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for key in results_dict:
    print(f"{key}: {results_dict[key]['Vote_Percentage']}% ({results_dict[key]['Vote_Count']})")
print("-------------------------")
print(f"Winner: {winner}")

#Here we establish a .txt file to send the results to

#os.path function creates a path to the output file based on the Operating System
election_results=os.path.join(".","election_results.txt")

#function to open a connection to the output file, and write results to it
with open(election_results, "w") as text_file:
    print("Election Results",file=text_file)
    print("-------------------------",file=text_file)
    print(f"Total Votes: {total_votes}",file=text_file)
    print("-------------------------",file=text_file)
    for key in results_dict:
        print(f"{key}: {results_dict[key]['Vote_Percentage']}% ({results_dict[key]['Vote_Count']})", file=text_file)
    print("-------------------------",file=text_file)
    print(f"Winner: {winner}",file=text_file)