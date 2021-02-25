import numpy as np
import pandas as pd
from math import log

#For compound_interest_calc
  #p = Principal Balance
  #r = Rate (given in decimal form, ie. 3% should be written as .03)
  #n = Number of times the rate is applied during the time period
  #t = number of time periods elapsed
#This version returns a dictionary with years and the updated principal balance for each year. This version of the function
#   does not take in any additional input payments, it just tracks the growth of the principal.

def compound_interest_calc(p, r, n, t):
  salary_table = {}
  for num in range(30):
    final_amount = p * (( 1 + (r/n))**(n * num))
    salary_table[num] = int(final_amount)
  return salary_table


print(compound_interest_calc(80000, .03, 1, 1))

#The function call below tracks a salary that starts 80,000 and increases 3% per year, and returns the value in year 5.
def salary_by_year(year):
  print((80000 * (( 1 + (.03))**year)))
salary_by_year(5)



### Simple rate-of-return calculator. First function formats answer.

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

def calculate_simple_return(start_price, end_price, dividend=0):
  simple_ror = ((end_price - start_price + dividend)/start_price)
  return simple_ror

simple_return = calculate_simple_return(200, 250, 20)
print('The simple rate of return is ' + str(display_as_percentage(simple_return)))


### Logarithmic Rate of Return


def calculate_log_return(start_price, end_price):
  return log(end_price) - log(start_price)
log_return = calculate_log_return(200, 250)
print('The log rate of return is ' + str(display_as_percentage(log_return)))

#This function is the same as the one above, it has just been shortened

calc_log_return = lambda start, end: log(end) - log(start)

### Code for calculating annualized rates of returns

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_return_a = 0.001
monthly_return_b = 0.022

# Write code here
### To calculate adjusted (usally annualized) log rate of return, you mutiply the log rate of return, by the number of original time periods that are in the new time period.
      #EX: New rate of return = log-rate-of-return * 12 if we want to find out the annual rate of return for an investment where we initially calculated the log rate of return over a 1 month period.

print('The daily rate of return for Investment A is ' + str(display_as_percentage(daily_return_a)))
print('The monthly rate of return for Investment B is ' + str(display_as_percentage(monthly_return_b)))

def annualize_return(log_return, t):
  return log_return * t
annual_return_a = annualize_return(daily_return_a, 252)
print('The annual rate of return for Investment A is ' + str(display_as_percentage(annual_return_a)))
annual_return_b = annualize_return(monthly_return_b, 12)
print('The monthly rate of return for Investment B is ' + str(display_as_percentage(annual_return_b)))

#The following two functions do the same thing, take a return stated as the multiplier rate, and send it back as a percentage.
#The first is a long, but clear delineation of each step, while the second is an efficient one line lambda function

rate_of_return = 0.075

def display_as_percentage(val):
  new_val = val * 100
  rounded_val = round(new_val, 1)
  string_val = str(rounded_val)
  return string_val + '%'

display_as_percentage = lambda val: '{}%'.format(str(round(val * 100, 1)))

print(display_as_percentage(rate_of_return))






