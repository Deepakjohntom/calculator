def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    return a/b


operation_dict={
"+":add,
"-":sub,
"*":mult,
"/":divide
}


def calculator():
    n1=float(input("Enter first number: "))

    for symbol in operation_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick a symbol: ") # +,-,*,/

        n2=float(input("Enter second number: "))

        cal_function=operation_dict[op_symbol]
        output=cal_function(n1,n2)

        print(f"{n1}{op_symbol}{n2} = {output}")

        should_continue=input(f"Enter 'Y' to continue calculation with {output} or Enter 'N' to continnue new calculation and Enter 'X' to exit the calculation: ").upper()
        if should_continue=='Y':
            n1=output
        elif should_continue=='N':
            continue_flag = False
            calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()