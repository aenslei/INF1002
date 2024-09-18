'''
Task Description:
Develop one employee weekly payment calculation program as we have discussed in 
Lecture 2. The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.45. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!

'''
# import sys
# # write your code here
# def WeeklyPaymentCalculator():
#     # Read the command line arguments
#     if len(sys.argv) != 4:
#         print("Your input is invalid!")
#         sys.exit(1)

#     try:
#         # Parse the command line arguments
#         working_hours = int(sys.argv[1])
#         normal_rate = float(sys.argv[2])
#         overtime_rate = float(sys.argv[3])

#         # Calculate the payment
#         if working_hours <= 40:
#             normal_payment = normal_rate * working_hours
#             overtime_payment = 0
#         elif (working_hours > 40 and working_hours < 168):
#             #168 Hours is the limit as that is the most anyone can work within a week. 24x7
#             normal_payment = normal_rate * 40
#             overtime_payment = overtime_rate * (working_hours - 40)
#         else:
#             print("Your input is invalid!")
#             sys.exit(1)

#         total_payment = normal_payment + overtime_payment

#         # Print the results
#         print(f"Normal Salary: {normal_payment:.2f}, Extra Salary: {overtime_payment:.2f}, Total Salary: {total_payment:.2f}")

#     except ValueError:
#         print("Your input is invalid!")
#         sys.exit(1)
#     pass


# if __name__=='__main__':
#     WeeklyPaymentCalculator()
    

import sys

def WeeklyPaymentCalculator():
    try:
        # Ensure there are enough command-line arguments
        if len(sys.argv) != 4:
            print("Your input is invalid!")
            sys.exit(1)

        # Parse the command line arguments
        working_hours = int(sys.argv[1])
        normal_rate = float(sys.argv[2])
        overtime_rate = float(sys.argv[3])

        # Validate working hours
        if working_hours < 0 or working_hours > 168:
            print("Your input is invalid!")
            sys.exit(1)

        # Calculate the payment
        if working_hours <= 40:
            normal_payment = normal_rate * working_hours
            overtime_payment = 0
        else:
            normal_payment = normal_rate * 40
            overtime_payment = overtime_rate * (working_hours - 40)

        total_payment = normal_payment + overtime_payment

        # Print the results with the required precision
        print(f"Normal Salary:{normal_payment:.2f}, Extra Salary:{overtime_payment:.2f}, Total Salary:{total_payment:.2f}")

    except ValueError:
        print("Your input is invalid!")
        sys.exit(1)

if __name__ == '__main__':
    WeeklyPaymentCalculator()
