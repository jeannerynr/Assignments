### Homework : Purchasing your dream house in Lyon

### Part I: Calculating Time to Save
# for example (test case 2), if annual salary is 75000, portion of salary saved is 0.15, and the cost of your dream home is 600000,
# you will need to wait 131 months.
# test case 1: 157 months.

"""annual_salary=float(input("Enter your annual salary in Lyon: "))
monthly_salary=annual_salary/12
portion_saved=float(input("Enter the portion of salary to be saved, as a decimal: "))
portion_saved*=monthly_salary
total_cost=float(input("Enter the cost of your dream home in Lyon: "))
portion_down_payment=0.25*total_cost
current_savings=0
r=0.04 #annual return of investments
months=0

while current_savings<portion_down_payment: 
    if months%12==0: #if and only if it has been a year of saving up
        current_savings=current_savings+(current_savings*r) #add annual return of the investments (4% of current savings)
    current_savings+=portion_saved
    months+=1
print("Number of months: ",months)"""

### Part 2: Salary Raise
# or example (test case 1), if annual salary is 65000, portion of salary saved is 0.12, the cost of your dream home is 500000, and your semi annual salary raise is 0.04, 
# you will need to wait 149 months.
# test case 2: 201 months

"""annual_salary=float(input("Enter your annual salary in Lyon: "))
monthly_salary=annual_salary/12
portion_saved=float(input("Enter the portion of salary to be saved, as a decimal: "))
portion_saved*=monthly_salary
total_cost=float(input("Enter the cost of your dream home in Lyon: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment=0.25*total_cost
current_savings=0
r=0.04 #annual return of investments
months=0

while current_savings<portion_down_payment: 
    if months%6==0: #if it has been six months, add the semi annual salary raise 
        annual_salary*=(1+semi_annual_raise)
    if months%12==0: #if and only if it has been a year of saving up
        current_savings=current_savings+(current_savings*r) #add annual return of the investments (4% of current savings)
    current_savings+=portion_saved 
    months+=1
print("Number of months: ",months)"""

### Part III: Finding the Right Savings Rate



annual_salary=float(input("Enter your annual salary in Lyon: "))
monthly_salary=annual_salary/12
portion_saved=float(input("Enter the portion of salary to be saved, as a decimal: "))
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment=250000
current_savings=0
r=0.04 #annual return of investments
months=0

while current_savings<portion_down_payment: 
    if months%6==0: #if it has been six months, add the semi annual salary raise 
        annual_salary*=(1+semi_annual_raise)
    if months%12==0: #if and only if it has been a year of saving up
        current_savings=current_savings+(current_savings*r) #add annual return of the investments (4% of current savings)
    current_savings+=portion_saved 
    months+=1
print("Number of months: ",months)
