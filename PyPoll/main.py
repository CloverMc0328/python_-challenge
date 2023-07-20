import os 

import csv

BallotID_List = []
Candidate_List = []
Unique_Candidate_List = []

csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#with open (csvpath, encoding = 'UTF-8') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter= ',')
    #print(csv_reader)
    #data = list(csv_reader)

csvpath = os.path.join("PyPoll","Resources","election_data.csv")

with open (csvpath) as csv_file:
    csv_reader = csv.DictReader(csv_file , delimiter=',')
    data = list(csv_reader)
   
    for Data_index in range(len(data)):
        BallotID_List.append((data[Data_index]['Ballot ID']))
        Candidate_List.append((data[Data_index]['Candidate']))
    

Candidate = Candidate_List[0]
Unique_Candidate_List.append(Candidate)

Candidate_List = sorted(Candidate_List)
Candidate_List_index = 0
for Candidate_List_index in range(len(Candidate_List) -1):
    if Candidate_List[Candidate_List_index] !=  Candidate_List[Candidate_List_index + 1]:
        Candidate = Candidate_List[Candidate_List_index + 1]
        Unique_Candidate_List.append(Candidate)


for Unique_Candidate_List_index in range(len(Unique_Candidate_List) - 1):
    MaxCount = Candidate_List.count(Unique_Candidate_List[0])
    if Candidate_List.count(Unique_Candidate_List[Unique_Candidate_List_index]) < Candidate_List.count(Unique_Candidate_List[Unique_Candidate_List_index + 1]):
        Winner = Unique_Candidate_List[Unique_Candidate_List_index + 1]


Analysis_Result_file = 'PyPoll/Analysis/Result.txt'
with open(Analysis_Result_file, 'w') as Result:
    Result.write("Election Results" + '\n'+ '\n')
    Result.write("----------------------------" + '\n'+ '\n' )
    Result.write(f'Total Votes: {len(BallotID_List)}' + '\n'+ '\n')
    Result.write("----------------------------" + '\n'+ '\n')
    
    for Unique_Candidate_List_index in range(len(Unique_Candidate_List)):
        Vote_Count = Candidate_List.count(Unique_Candidate_List[Unique_Candidate_List_index])
        Percentage_of_Vote_Count = round((Vote_Count / len(Candidate_List) * 100),3)
        Result.write(f"{Unique_Candidate_List[Unique_Candidate_List_index]}: {Percentage_of_Vote_Count}% ({Vote_Count})" + '\n'+ '\n')
        
    Result.write("-----------------------------" + '\n'+ '\n')
    Result.write("Winner: " + Winner + '\n'+ '\n') 
    Result.write("-----------------------------")

print("Code Ran Successfully")