r'''
Task Description: 
    In this task, we need to design one recursive function to calculate the SUM value
    of one input number. The SUM of x is defined as the summation of all the positive 
    numbers that are not bigger than X, such as 1+2+3…+X.

    So please design one recursive function sum_recursive(x) to return the SUM value of x. 
    In addition, please implement another function sum_iterative(x) to return the SUM 
    value of x     with the iterative manner (e.g. for loop).  Write the main program to 
    allow users to input one number to your program and call these two functions to see 
    whether they get the same output. 
    
    The example executions are shown as follows:

Note: 
    Your output should be in ONE line.

Running example: 
    C:\INF1002\Lab4\SumCalculator> python SumCalculator.py 3
    The SUM value calculated by recursive is 6 and by iterative is 6.
'''
import sys

def sum_recursive(x):
    if x <= 0:
        return 0
    else:
        return x + sum_recursive(x - 1)

def sum_iterative(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def SumCalculator():
    if len(sys.argv) != 2:
        print("Usage: python SumCalculator.py <number>")
        return
    
    try:
        x = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    sum_rec = sum_recursive(x)
    sum_iter = sum_iterative(x)
    
    print(f"The SUM value calculated by recursive is {sum_rec} and by iterative is {sum_iter}.")

if __name__ == '__main__':
    SumCalculator()


if __name__=='__main__':
     SumCalculator()