from typing import Text

b = input("Enter your name : ")
a = int(input("Enter your Percentage: "))

if (a<35):
    print("You are Fail!")

elif(a>35 and a<=40):
    print("You are passed!")

elif(a>40 and a<=70):
    print("You are Passed with First class!")

elif(a>70 and a<=100):
    print("You are passed with Destination!")

else:
    print("Enter valid Percentage!")

# file save with txt format

with open("Program/Text.txt", "r") as f :
    Text = f.read()
with open("Program/Text.txt", "a") as f :
    f.write(str("\n"+ b +":"))
    f.write(str(str(a)))



