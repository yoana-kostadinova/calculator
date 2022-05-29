import math
num1 = None
num2 = None
num3 = None
inpt = None
op = None
res = None
Continue = True

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


print(" ____________\n| __________ |\n||welcome   ||\n||to my     ||\n||calculator||\n|^^^^^^^^^^^^|\n| [M|V|C][-] |\n| [7|8|9][+] |\n| [4|5|6][x] |\n| [1|2|3][%] |\n| [.|O|:][=] |\n^^^^^^^^^^^^^^\n")

while Continue == True:
        
        inpt = input("\nEnter the first number: \n")

        while isDigit(inpt) == False:
                print("That's not a valid number! Try again ")
                print("  (っ°皿°)っ ")
                inpt = input("Enter the first number: \n")


        if isDigit(inpt) == True:
                num1 = float(inpt)
                inpt = None


        inpt = input("Choose an operation between\n + - * / % RECP, SQRT, SIGN, MC, CE: \n")

        while inpt != '+' and inpt != '-' and inpt != '*' and inpt  != '/' and inpt != '%' and inpt != 'RECP' and inpt != 'SQRT' and inpt != 'SIGN' and inpt != 'MC' and inpt != 'C' and inpt != 'CE':
                print("That's not a valid operation! Try again ")
                print(" (⩺_⩹) ")
                inpt = input("Choose an operation between\n + - * / % RECP, SQRT, SIGN, MC, CE: \n")

        op = inpt 
        inpt = None


        while op != 'RECP' and op != 'SQRT' and op != 'SIGN' and op != 'MC' and op != 'CE'  :
                inpt = input("Enter the second number: \n")

                while isDigit(inpt) == False:
                        print("That's not a valid number! Try again ")
                        inpt = input("Enter the second number: \n")


                if isDigit(inpt) == True:
                        num2 = float(inpt)
                        inpt = None
                        break


        if op == '+':
                res = num1+num2
                print (str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(res) )

        elif op == '-':
                res = num1 - num2
                print (str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(res) )

        elif op == '*':
                res = num1*num2
                print (str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(res) )

        elif op == '/':
                res = num1/num2
                print (str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(res) )

        elif op == '%' :
                num3 = num1/100
                res = num3*num2
                print (str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(res) )

        elif op == 'RECP' :
                res = 1/num1
                print (str(num1) + ' ' + str(op) +  ' = ' + str(res) )

        elif op == 'SQRT' :
                if num1<0 :
                        print("Error! The square root of a negative number does not exist among the set of Real Numbers!")
                        print("( >▃< )")
                else :
                        res = math.sqrt(num1)
                        print (str(num1) + ' ' + str(op) +  ' = ' + str(res) )


        elif op == 'SIGN' :
                res = -num1
                print (str(num1) + ' ' + str(op) +  ' = ' + str(res) )


        elif op == 'MC' :
                num1 = None
                num2 = None
                print ("First number = " + str(num1))
                print ("Second number = " + str(num2))
                continue
        else :
                num1 = None
                continue
                

        inpt = input("\nDo you wish to continue? yes/no ")
        while inpt != "yes" and inpt != "no" :
                inpt = input("\nDo you wish to continue? yes/no ")
        if inpt == "yes" :
                print("*************************************")
                Continue = True
        else :
                print("*************************************")
                Continue = False
                print("Thank you for using my calculator! Made by Yoana Kostadinova 201220026 ")
                print("\n░░░░░░░░░░░░░░░░░░░░░▄▀░░▌\n░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌\n░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌\n░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌\n░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█\n░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄\n░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄\n░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐\n░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌\n░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄\n▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀\n▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄\n▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀\n▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄\n▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀\n")





                
