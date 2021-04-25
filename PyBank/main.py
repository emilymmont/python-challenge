import os
import csv
from pathlib import Path

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):

        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)

greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average  Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

input_file = os.path.join("PyBank", "Resources", "budget_data.csv")

output_file = os.path.join("PyBank", "analysis", "Financial_Analysis.txt")

with open(output_file,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average  Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")