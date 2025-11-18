def add(num1, num2):   
    return num1 + num2
def sub(num1, num2):   
    return num1 - num2
def multi(num1, num2):   
    return num1 * num2
def div(num1, num2):   
    return num1 / num2

def calculator():
    while(True):
        print("Select operation.")
        print("1.Add +")
        print("2.Subtract -")
        print("3.Multiply *")
        print("4.Divide /")
        print("5.Stop")

        option = input("Enter your choice(1/2/3/4/5): ")

        number1 =float(input("Enter first number: ")) 
        number2 =float(input("Enter second number: "))

        if option == '5':
            exit()
        if option == '1':
            print(add(num1=number1, num2=number2))
        if option == '2':
            print(sub(num1=number1, num2=number2))
        if option == '3':
            print(multi(num1=number1, num2=number2))
        if option == '4':
            print(div(num1=number1, num2=number2))
           
calculator()



