import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join("..", "Output", "Election Analysis.csv")
with open(csvpath, newline='') as csvfile:
    f = csv.reader(csvfile, delimiter=',')

    csv_header = next(f)

    vote_count = 0
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    winner = 0

    for row in f:
        vote_count = vote_count + 1
        if row[2] == 'Khan':
            khan = khan + 1
        elif row[2] == 'Correy':
            correy = correy + 1
        elif row[2] == 'Li':
            li = li + 1
        else:
            tooley = tooley + 1

    if khan > correy and khan > li and khan > tooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > tooley:
        winner = "Correy"
    elif li > khan and li > correy and li > tooley:
        winner = "Li"
    else:
        winner = "Tooley"
    
            
    khan_percent = (khan / vote_count) * 100
    correy_percent = (correy / vote_count) * 100
    li_percent = (li / vote_count) * 100
    tooley_percent = (tooley / vote_count) * 100

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(vote_count))
    print("----------------------------")
    print("Khan: " + str(round(khan_percent, 0)) + "% (" + str(khan) + ")")
    print("Correy: " + str(round(correy_percent, 0)) + "% (" + str(correy) + ")")
    print("Li: " + str(round(li_percent, 0)) + "% (" + str(li) + ")")
    print("O'Tooley: " + str(round(tooley_percent, 0)) + "% (" + str(tooley) + ")")
    print("----------------------------")
    print("Winner: " + winner)

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Votes: " + str(vote_count)])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Khan: " + str(round(khan_percent, 0)) + "% (" + str(khan) + ")"])
    csvwriter.writerow(["Correy: " + str(round(correy_percent, 0)) + "% (" + str(correy) + ")"])
    csvwriter.writerow(["Li: " + str(round(li_percent, 0)) + "% (" + str(li) + ")"])
    csvwriter.writerow(["O'Tooley: " + str(round(tooley_percent, 0)) + "% (" + str(tooley) + ")"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Winner: " + winner])