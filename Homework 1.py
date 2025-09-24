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

salary=float(input("Enter your annual salary in Lyon: "))
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment=250000 #25% of 1 million
current_savings=0
r=0.04 #annual return of investments
months=36
highest_possible_rate=10000 # This represents 1.0 the max rate you can save per month, it is shown as 10^4 so as to be precise in the optimal saving rate.

#

def simulate_savings(annual_salary, portion_saved):
    ### This function checks to see if, depending on the portion saved each month, after 3 years you will be able to afford your down payment
    temp_salary = annual_salary
    monthly_salary=temp_salary/12
    current_savings=0

    for month in range(1,37): # From the first month to the 36th
        
        if month%6==0: #if it has been six months, add the semi annual salary raise 
            temp_salary*=(1+semi_annual_raise)
            monthly_salary = temp_salary / 12 
        current_savings += current_savings * (r / 12) # add the annual investments split every month
        current_savings += monthly_salary * portion_saved

    return current_savings


def calculate_best_savings_rate(annual_salary):
    ### This function will calculate the best saving rate in order to take the least amount of months to pay the down payment

    if simulate_savings(annual_salary, 1.0) < (portion_down_payment - 100): # Checks to see if it is possible to pay in 3 years if you put your entire salary into savings
        print("It is not possible to pay the down payment in three years.")
        return
    
    lowest_rate=0
    highest_rate=highest_possible_rate
    bisection_step=0

    while lowest_rate <= highest_rate:
        bisection_step += 1
        division_guess = (lowest_rate + highest_rate) // 2
        rate = division_guess / highest_possible_rate
        current_savings = simulate_savings(annual_salary, rate)
        if abs(current_savings - portion_down_payment) <= 100: 
            # if the absolute value of our current savings - the money needed for the down payment is inferior / equal to 100 then that means the 
            # rate used produces savings within 100€ of what we need, which is the tolerance we accept
            print(f"Best savings rate: {rate:.4f}")
            print("Steps in bisection search:", bisection_step)
            return
        elif current_savings < portion_down_payment: # if the savings accumulated after the use of the simulate savings function is inferior to the amount need for the down payment 
            lowest_rate = division_guess + 1 # This narrows the search to the upper half of the range of 0 to 1.0 which we had split at the beginning of the loop (direct use of bisection search)
        else: # However if the savings accumulated are too high then we can go even lower, we are in the right range but we need to split it at least once more to be more precise
            highest_rate = division_guess - 1

#

calculate_best_savings_rate(salary)

### Here we get the following :

# Enter your annual salary in Lyon: 90000
# Best savings rate: 0.7265
# Steps in bisection search: 7

# Enter your annual salary in Lyon: 50000
# It is not possible to pay the down payment in three years.
# (This is because if 100% is saved up every month, then after three years you only get ≈ 233,559.57€)

# Enter your annual salary in Lyon: 35000
# It is not possible to pay the down payment in three years.
