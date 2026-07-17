calculator_ascii_art='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(calculator_ascii_art)

# def calculation(first_no,second_no,pick_operation):
#     calculated_value=0
#     if pick_operation=="+":
#         add=first_no+second_no
#         calculated_value+=add
#         print(f'{first_no}+{second_no}={calculated_value}')
#     elif pick_operation=="-":
#         sub=first_no-second_no
#         calculated_value+=sub
#         print(f'{first_no}-{second_no}={calculated_value}')
#     elif pick_operation=="*":
#         miulti=first_no*second_no
#         calculated_value+=miulti
#         print(f'{first_no}*{second_no}={calculated_value}')
#     elif pick_operation=="/":
#         divide=first_no/second_no
#         calculated_value+=divide
#         print(f'{first_no}/{second_no}={calculated_value}')
#     else:
#         print("invalid input")
#     return calculated_value
# new_calculation=True

# while new_calculation:
#     first_no=float (input("what's the first number?:"))

#     print("+")
#     print("-")
#     print("*")
#     print("/")

#     continue_calculation_with_last_output=True
#     while continue_calculation_with_last_output:
#         pick_operation=input("pick an operation:")

#         second_no=float(input("what's the next number?:"))

#         calculatedvalue=calculation(first_no=first_no,second_no=second_no,pick_operation=pick_operation)

#         next_calculation=input(f'type "y" to continue calculating with {calculatedvalue} or type "n" to start a new calculation:')
#         if next_calculation =="y":
#             first_no=calculatedvalue
            

#         if next_calculation=="n":
#             next_calculation=True
#             first_no=float (input("what's the first number?:"))

#             print("+")
#             print("-")
#             print("*")
#             print("/")

#             pick_operation=input("pick an operation:")

#             second_no=float(input("what's the next number?:"))

#             calculatedvalue=calculation(first_no=first_no,second_no=second_no,pick_operation=pick_operation)

#             next_calculation=input(f'type "y" to continue calculating with {calculatedvalue} or type "n" to start a new calculation:')


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":multi,
    "/":div
}
def calculator():
    first_no=float(input("Enter first number:"))
    for symbols in operations:
        print(symbols)
    should_continue=True
    while should_continue:
        pick_operation=input("pick an operation")
        second_no=float(input("Enter second number:"))
        calculation_function=operations[pick_operation]
        calculated_value=calculation_function(first_no,second_no)
        print(f"{first_no} {pick_operation} {second_no} = {calculated_value}")
        next_calculation=input(f'"y" to continue calculating with {calculated_value},"n" to start a new calculation:')
        if next_calculation=="y":
            should_continue=True
            first_no=calculated_value
        elif next_calculation=="n":
            should_continue=False
            calculator()

calculator()
    
