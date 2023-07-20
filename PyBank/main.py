import os

import csv

 

Month_list = []

Profit_list = []

csvpath = os.path.join("PyBank","Resources","budget_data.csv")


with open (csvpath) as csv_file:
    csv_reader = csv.DictReader(csv_file , delimiter=',')
    data = list(csv_reader)

    #Total number & Total amount of profits/losses
    for items in range(len(data)):
        Month_list.append({data[items]['Date']}) #Add months from the csv to the month_dict list 
        Profit_list.append((int(data[items]['Profit/Losses']))) #Add profits/losses from the csv to the Profit_list list 
    Total = sum(Profit_list)
    #Average Change:
    index = 0
    profit_change_list =[] #create "profit_change_list" list
    Change_period_list =[]
    profit_change_list_cal =[]
    
    while index < (len(Profit_list)-1):
        profit_change = (Profit_list[index + 1] - Profit_list[index] ) #Calculate the different between 1 period and the one below it
        profit_change_list.append(profit_change) #Add the calculated value to the profit_change list
        Change_period_list.append(Month_list[index + 1])
        index += 1
    sum_profit_change = round(sum(profit_change_list),2)
    average_profit_change = round(sum_profit_change/len(profit_change_list),2) #calculate the average of profit change over time
    
    

    MaxProfitChange = max(profit_change_list)
    MaxIndex = profit_change_list.index(MaxProfitChange)
    GreatestIncreaseChangePeriod = Change_period_list[MaxIndex]
    
    MinProfitChange = min(profit_change_list)
    MinIndex = profit_change_list.index(MinProfitChange)
    GreatestDecreaseChangePeriod = Change_period_list[MinIndex]

    
Analysis_Result_file = 'PyBank/Analysis/Result.txt'
with open(Analysis_Result_file, 'w') as Result:
    Result.write("Financial Anlysis" + '\n'+ '\n')
    Result.write("----------------------------" + '\n'+ '\n' )
    Result.write(f'Total Months: {len(Month_list)}' + '\n'+ '\n')
    Result.write(f'Total Profit: ${Total}' + '\n'+ '\n')
    Result.write(f'Total Profit Change Over Time: ${average_profit_change}' + '\n'+ '\n')
    Result.write(f'Greatest Increase in Profits: {" ".join(GreatestIncreaseChangePeriod)} (${MaxProfitChange})'+ '\n'+ '\n')    
    Result.write(f'Greatest Decrease in Profits: {" ".join(GreatestDecreaseChangePeriod)} (${MinProfitChange})'+ '\n'+ '\n')  



print("Code Ran Successfully")
       

  

  


    
    

  
    
    



    