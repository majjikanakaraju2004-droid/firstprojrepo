''' write a program to find the reverse of the given number'''

num=input("enter the num:")

# write the code of palidrome

def ispalidrome(num):
    rev=0
    rev=reversed(num)
    if num==rev:
        print("True")
    else:
        print("false")

ispalidrome(num)
