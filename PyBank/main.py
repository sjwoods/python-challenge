import csv
import os

budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

total_months = []
total_profit = []
monthly_profit = []

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)
    
    for row in csvreader:
    
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_profit.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit)
max_decrease_value = min(monthly_profit)

max_increase_month = monthly_profit.index(max(monthly_profit)) + 1
max_decrease_month = monthly_profit.index(min(monthly_profit)) + 1

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {len(total_months)}") 
print(f"Total: ${sum(total_profit)}") 
print(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")   

output_file = ("Financial_Analysis.txt")

with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("/n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("/n")
    file.write("Total: ${sum(total_profit)}")
    file.write("/n")
    file.write("Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
    file.write("/n")
    file.write("Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("/n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")     
    