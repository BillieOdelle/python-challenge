import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')
print(budget_data_csv)
count = 0
totalProfit = 0
list = []
previousLine = None
averageChange = 0
greatestincrease = 0
greatestincreasedate = None
greatestdecrease = 0
greatestdecreasedate = None

with open(budget_data_csv, 'r') as csv_file:
    csvData = csv.reader(csv_file)
    csv_header = next(csv_file)
    
    for line in csvData:
        count = count + 1
        # Read the date value from column zero
        dateValue = line[0]
        # Read the profit value from column one and conver to an integer
        profitValue = int(line[1])
        totalProfit = totalProfit + profitValue
        
        if previousLine is not None:
            previousProfit = int(previousLine[1]) 
            thechange =  profitValue - previousProfit
            if thechange > greatestincrease:
                greatestincrease = thechange
                greatestincreasedate = dateValue
            if thechange < greatestdecrease:
                greatestdecrease = thechange
                greatestdecreasedate = dateValue

            list.append(thechange)
        
        previousLine = line
  
    averageChange = sum(list) / len(list)

    print('Financial Analysis')
    print()
    print('-------------------------------------')
    print()
    print('Total Months:', count)
    print()
    print('Total:', '$',totalProfit)
    print()
    print(f"Average Change: ${averageChange:.2f}")
    print()
    print('Greatest Increase in Profits:', greatestincreasedate, '(','$',greatestincrease,')')
    print()
    print('Greatest Decrease in Profits:', greatestdecreasedate, '(','$',greatestdecrease, ')')

# Write to .txt file
analysisLocation = os.path.join('Analysis', 'Results.txt')
file1 = open(analysisLocation,"w") #write mode
file1.write('Financial Analysis')
file1.write('\n')
file1.write('-----------------------------------')
file1.write('\n')
file1.write('Total Months:'+ str(count))
file1.write('\n')
file1.write('Total: $ ' + str(totalProfit))
file1.write('\n')
file1.write(f"Average Change: ${averageChange:.2f}")
file1.write('\n')
file1.write(f"Greatest Increase in Profits: {greatestincreasedate}   (${greatestincrease})")
file1.write('\n')
file1.write(f"Greatest Decrease in Profits: {greatestdecreasedate}   (${greatestdecrease})")
file1.close()