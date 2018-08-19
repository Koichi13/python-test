import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join("..", "Output", "Financial Analysis.csv")
with open(csvpath, newline='') as csvfile:
    f = csv.reader(csvfile, delimiter=',')

    csv_header = next(f)
    
    date_count = 0
    total = 0
    change = []
    profit = 0
    change_value = 0

    for row in f:
        date_count = date_count + 1

        total += int(row[1])

        change_value = int(row[1]) - profit
        change.append(change_value)
        profit = int(row[1])
        
    change.pop(0)
    average_change = sum(change) / float(len(change))

    highest_change = max(change)
    lowest_change = min(change)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(date_count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: $" + str(highest_change))
    print("Lowest Increase in Profits: $" + str(lowest_change))

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: " + str(date_count)])
    csvwriter.writerow(["Total: $" + str(total)])
    csvwriter.writerow(["Average Change: $" + str(round(average_change, 2))])
    csvwriter.writerow(["Greatest Increase in Profits: $" + str(highest_change)])
    csvwriter.writerow(["Lowest Increase in Profits: $" + str(lowest_change)])

    