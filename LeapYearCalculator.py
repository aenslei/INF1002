r'''
Task Description:
In this task, you will develop a program to compute all the leap years within a 
specified time period. The user will input a start year and an end year. 
Your task is to determine how many leap years are included in this period and 
print out those leap years. 

The rule for determining leap years is as follows:
	. A year is called a leap year, if the year is perfectly divisible by 4 - except 
       for years which are both divisible by 100 and not divisible by 400. The second 
       part of the rule effects century years. 
       For example; the century years 1600 and 2000 are leap years, 
       but the century years 1700, 1800, and 1900 are not. This means that three times 
       out of every 400 years there are 8 years between leap years.

More information about the leap years rule can be found online. 

Input: Two numbers (one is the start year, and another is the end year)
Output: The number of leap years and all the leap years (Your output should be in one line)
Note: In case of invalid input, print the message "Your input is invalid!".

Running Examples:

C:\INF1002\Lab2\LeapYearCalculator> python LeapYearCalculator.py 1989 2000
The number of Leap Years is 3, the Leap Years are 1992, 1996, 2000
'''

import sys
def is_leap_year(year):
     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def LeapYearCalculator():
     if len(sys.argv) != 3:
          print("Your input is invalid!")
          return

     try:
          start_year = int(sys.argv[1])
          end_year = int(sys.argv[2])
     except ValueError:
          print("Your input is invalid!")
          return

     if start_year > end_year:
          print("Your input is invalid!")
          return

     leap_years = [year for year in range(start_year, end_year + 1) if is_leap_year(year)]
     print(f"The number of Leap Years is {len(leap_years)}, the Leap Years are {', '.join(map(str, leap_years))}")

if __name__=='__main__':
     LeapYearCalculator()
      
