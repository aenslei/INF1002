'''
Task Description: 
      In this task, we need to design one recursive function digit_recursive(x) to 
      calculate how many digits a positive number has. For instance, 10 has two 
      digits, and 122 has three digits, and 5679 has four digits. HINT: The number 
      of digits can be calculated by repeatedly dividing by 10 (without keeping the 
      remainder) until the number is less than 10. 

      Please write another function digit_iterative(x) to achieve the same 
      functionality to calculate the number of the digits of x but uses while loop. 
      Write one main program to allow users to input one number and call these two 
      functions to evaluate the output.

      The example executions are shown as follows: 
      
Note: 
      Your output should be in ONE line

Running example:
      C:\INF1002\Lab4\CountDigits> python CountDigits.py 789
      The number of digit(s) calculated by recursive is 3 and by iterative is 3.
'''
import sys
def digit_recursive(x):
      if x < 10:
            return 1
      else:
            return 1 + digit_recursive(x // 10)

def digit_iterative(x):
      count = 0
      while x > 0:
            x = x // 10
            count += 1
      return count

def CountDigits():
      if len(sys.argv) != 2:
            print("Usage: python CountDigits.py <number>")
            return
      
      try:
            number = int(sys.argv[1])
            if number < 0:
                  raise ValueError("The number must be positive.")
      except ValueError as e:
            print(f"Invalid input: {e}")
            return
      
      recursive_count = digit_recursive(number)
      iterative_count = digit_iterative(number)
      
      print(f"The number of digit(s) calculated by recursive is {recursive_count} and by iterative is {iterative_count}.")


if __name__=='__main__':
      CountDigits()
      



