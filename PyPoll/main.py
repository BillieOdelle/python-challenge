import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')
print(election_data_csv)

count = 0
previousLine = None
Dict = {}
highestVoteCount = 0
winner = None

with open(election_data_csv, 'r') as csv_file:
    csvData = csv.reader(csv_file)
    csv_header = next(csv_file)
   
    
    for line in csvData:
        count = count + 1
        Candidate = line[2]
        VoteCount = Dict.get (Candidate, 0)
        Dict [Candidate] = VoteCount + 1
    
    analysisLocation = os.path.join('Analysis', 'Results.txt')
    file1 = open(analysisLocation,"w") #write mode  
    print('Election Result')
    file1.write('Election Result')
    print()
    print('-------------------------------------')
    file1.write('\n')
    file1.write('--------------------------------------')
    print()
    file1.write('\n')
    print('Total Votes:', count)
    file1.write('Total Votes:' + str(count))
    print('-------------------------------------')
    file1.write('\n')
    file1.write('--------------------------------------')
    for key, value in Dict.items():
        Percentage_Value = value/count*100
        if value > highestVoteCount:
            highestVoteCount = value
            winner = key
        print(f"{key}: {Percentage_Value:.3f}% ({value})")
        file1.write('\n')
        file1.write(f"{key}: {Percentage_Value:.3f}% ({value})")
    print('--------------------------')
    file1.write('\n')
    file1.write('--------------------------------------')
    print('Winner:', winner)
    print('---------------------------')
    file1.write('\n')
    file1.write('Winner:' + str(winner))
    file1.write('\n')
    file1.write('--------------------------------------')