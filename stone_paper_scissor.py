import random
import sys
def result(a,b):
    if a==b:
        return 0
    elif(a==0 and b==2):
        return 1
    elif(a==1 and b==0):
        return 1
    elif(a==2 and b==1):
        return 1
    else:
        return -1
def spc(a):
    if a==0:
        a="stone"
    elif a==1:
        a="paper"
    elif a==2:
        a="scissor"
    else :
        print("invalid input ")
        sys.exit()
    return a
a=(int(input("enter 0 for stone /1 for paper/ 2 for scissor:->")))
b=(random.randint(0,2))
result=result(a,b)
print("you entered :",spc(a))
print("random input :",spc(b))
if result ==0:
    print("Draw")
elif result ==1:
    print("Win")
else :
    print("You Loose")