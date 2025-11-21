print("     Calculator")
print("======================")

num1=int(input("Enter first Number : "))
num2=int(input("Enter secound Number : "))
ope=input("Which operation do you want to perform(+ , - , * , / ) : ")

if ope=="+":
    sum=num1+num2
    print(sum)
elif ope== "-":
    sub=num1-num2
    print(sub)
elif ope== "*":
    mul=num1*num2
    print(mul)
elif ope== "/":
    div=num1/num2
    print(div)
else:
    print("Try Again...")
