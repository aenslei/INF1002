r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys

def EvenOddCalculator():

       # Check if the input is provided
       if len(sys.argv) < 2:
              print("Please provide a series of numbers.")
              return

       # Parse the input
       try:
              numbers = list(map(int, sys.argv[1].split(',')))
       except ValueError:
              print("Please enter valid integers.")
              return

       if len(numbers) < 2:
              print("Please provide at least two numbers.")
              return

       # Initialize variables
       sum_even = 0
       sum_odd = 0
       count_even = 0
       count_odd = 0

       # Calculate sums and counts
       for num in numbers:
              if num % 2 == 0:
                     sum_even += num
                     count_even += 1
              else:
                     sum_odd += num
                     count_odd += 1

       # Calculate the difference between the biggest and smallest numbers
       max_num = max(numbers)
       min_num = min(numbers)
       difference = max_num - min_num

       # Calculate the centered average
       sorted_numbers = sorted(numbers)
       centered_numbers = sorted_numbers[1:-1]
       centered_average = sum(centered_numbers) // len(centered_numbers)

       # Print the results
       print(f"The sum of all even numbers is {sum_even}, the sum of all odd numbers is {sum_odd}, "
                f"the difference between the biggest and smallest number is {difference}, "
                f"the total number of even numbers is {count_even}, the total number of odd numbers is {count_odd}, "
                f"the centered average is {centered_average}.")

if __name__=='__main__':
      EvenOddCalculator()
      
