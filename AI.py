#AI
number1 = 0
number2 = 0
symbol = 0
output = 0
print ("Hello and welcome to Vlad's miniature AI")
name = input("Enter your name \n")
print ("Well hello,",name + ".")
print ("I am ROB (Recognising Organised Robot) it's nice to meet you!")
print ("I can do many things, such as do maths equations, have small conversations, and more!")
maths = input("Do you wanna do maths? \n")
if maths == "yes" or "Yes" or "YES":
    print ("Ok, type away")
    number1 = input("Input the first number \n")
    symbol = input("Input your desired operation (+,-,*,/) \n")
    number2 = input("Input the second number \n")
    if symbol == "+":
        output = (int(number1) + int(number2))
    elif symbol == "-":
        output = (int(number1) - int(number2))
    elif symbol == "*":
        output = (int(number1) * int(number2))
    elif symbol == "/":
        output = (int(number1) / int(number2))
    print (output)
else:
    print ("")
