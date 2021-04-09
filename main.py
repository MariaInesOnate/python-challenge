import csv
import os 

#PyBankExercise#
#Create path to csv file# 
csvpath = os.path.join("Resources", "budget_data.csv")

#Set Variables#
total_months = 0 
total_revenue = 0 
change_in_month = []
list_profitloss = []
months = []
revenue = []
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
                  months.append(row[0])
                  total_revenue.append(int(row[1]))
        
#Calculate total number of months# 
total_months = len(months)

