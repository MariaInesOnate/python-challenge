import csv
import os 

#PyBankExercise#

filename = "budget_data.csv"
#Create path to csv file# 
csvpath = os.path.join("Resources", filename)

#Set Variables#
total_months = 0 
total_revenue = 0 
change_in_month = []
profitloss = []
months = []
revenue = []
date = []
max_decrease = revenue [0]
max_increase = revenue [0]

#Open csv file#
with open(csvpath, 'r') as csvfile 

#Now store content in csvreader#  
        csvreader = csv.reader(budget, delimiter = ',') 
#Read the header#        
        csv_header = next(csvreader) 
#Time to iterate# 
        for row in csvread:
                  profitloss.append((float(row[1])
                  date.append(row[0])
        
#Calculate total number of months# 
total_months = len(months)

#Look for greatest increase and greatest decrease# 
for r in range(len(revenue)):
        if revenue [r] >= max_increase:
                max_increase = revenue[r]
                max_increase_month = months[r]
        elif revenue[r] <= max_dec:
                max_decrease = revenue [r]
                max_decrease_month = months[r]
        total_revenue += revenue[r]

#Find the average change in revenue#   
average_cr = round(total_revenue/total_months, 2)                                

#Create path for output file# 
output_path = os.path.join('..', 'python_challenge', 'summary.txt')

# Print Financial Analysis
print(f" ")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_total}")
print(f"Average Change: ${average_cr}")
print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

#Print to terminal# 
print(output)

#Save to text file# 
with open(file_to_output, "a") as txt_file: 
         txtfile.write(f"Financial Analysis\n")
         txtfile.write(f"--------------------------\n")
         txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_amount}\n")
        txtfile.write(f"Average Change: {average_change:.2f}\n")
        txtfile.write(f"Greatest Inc in Profits:, {greatest_increase_month}, ( ${highest})\n")
        txtfile.write(f"Greatest Dec in Profits:, {greatest_decrease_month}, (${lowest})\n")                            
