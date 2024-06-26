# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:32:56 2024

@author: Maja
"""
#               ***  Python - Programming Basics   *** 
                    

# Impoert libraries
import numpy as np
import pandas as pd
import math
from datetime import datetime

# 1. Create a matrix with three rows A, B and C and four columns with names Q, W, E and R. Fill the matrix with any numbers between 1 and 10.

# Creating an array
matrix1 = np.random.randint(0, 10, size=12).reshape(3, 4)

# Creating row and columns names
row_names = ["A", "B", "C"]
column_names = ["Q", "W", "E", "R"]

# Naming rows and colums of the array
my_matrix = pd.DataFrame(matrix1, index=row_names, columns=column_names)

# Displaying result
my_matrix

# 2. x = 24, y =”Hello World”, z = 93.65.
#    Identify the class of x, y and z and convert all three into factor.

x = 24
y = "Hello World"
z = 93.65

# Identify the class of x, y and z

print(type(x))
print(type(y))
print(type(z))

# Changing the class to factor

x1 = pd.Categorical(['24'])
y1 = pd.Categorical(['Hello World'])
z1 = pd.Categorical(['93.65'])

print(type(x1))
print(type(y1))
print(type(z1))

# 3. q = 65.9836
#          a. Find square root of q and round it up to 3 digits.
#          b. Check if log to the base 10 of q is less than 2.

q = 65.9836

# a)
q_squared = math.sqrt(q)
print(q_squared)

q_sqrt_rounded = round(q_squared,3)
print(q_sqrt_rounded)

# b)

log_q_base_10 = math.log10(q)
print(log_q_base_10)
is_log_less_than_2 = log_q_base_10 < 2
print(is_log_less_than_2)

print("The square root of q rounded up to 3 digits:", q_sqrt_rounded)
print("Is log to the base 10 of q less than 2?", is_log_less_than_2)


# 4. x = c(“Intelligence”, “Knowledge”, “Wisdom”, “Comprehension”) 
#    y = “I am”
#    z = “intelligent”
#          a. Find first 4 letters of each word in x.
#          b. Combine y and z to form a sentence “I am intelligent”
#          c. Convert all the words in x to upper case.

x = ["Intelligence", "Knowledge", "Wisdom", "Comprehension"]
y = "I am"
z = "intelligent"

# a) 
first4 = [r[0:4] for r in x]
print(first4)

# b)

print( y+ " "+ z )

# or

combined_string = "{} {}".format(y, z)
print(combined_string)

# 5. a = c(3,4,14,17,3,98,66,85,44)
#    Print “Yes” if the numbers in ‘a’ are divisible by 3 and “No” if they are not divisible by 3 using ifelse().

a = [3,4,14,17,3,98,66,85,44]
print(a)
    
for num in a:
    if num % 3 == 0:
        print("Yes")
    else:
        print("No")

# 6. b = c(36,3,5,19,2,16,18,41,35,28,30,31)
#    List all the numbers less than 30 in b using for loop.

b = [36,3,5,19,2,16,18,41,35,28,30,31]
print(b)

for num in b:
    if num < 30:
        print(num)
        
# 7. Date = “01/30/18”
#         a) Convert Date into standard date format (yyyy-mm-dd) and name it as Date_new.
#         b) Extract day of week and month from Date_new.
#         c) Find the difference in the current system date and Date_new.

# a)

Date = "01/30/18"
Date_new = datetime.datetime.strptime(Date, "%m/%d/%y").strftime("%Y-%m-%d")
print(Date_new)

#b) 

week_day = datetime.datetime.strptime(Date_new, "%Y-%m-%d").strftime("%A")
month = datetime.datetime.strptime(Date_new, "%Y-%m-%d").strftime("%B")
print("Day of week:", week_day)
print("Month:", month)

#c)

today= datetime.datetime.now()
print(today)
    
difference = today - datetime.datetime.strptime(Date_new, "%Y-%m-%d")
print("Difference in days:", difference.days)   





