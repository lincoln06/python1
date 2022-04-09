from math import *
x=0
y=1
z=2
i=0

def FirstCheck(x,y,z,i):
    if i<5:
        j=0
        SecondCheck(x,y,z,i,j)
    else:
        return
def SecondCheck(x,y,z,i,j):
    if j>=5:
        ThirdCheck(x,y,z,i,j)
    else:
        i=i+1
        FirstCheck(x,y,z,i)
def ThirdCheck(x,y,z,j,i):
    if j%2==0:
        FifthCheck(x,y,z,j,i)
    else:
        FourthCheck(x,y,z,j,i)
def FourthCheck(x,y,z,j,i):
    if (j+1)%3!=0:
        print(y)
        
    else:
        print(x)

    IncreaseJ(x,y,z,i,j)

def FifthCheck(x,y,z,j,i):
    if j==1 or j==3:
        print(x)
    else:
        print(z)
    IncreaseJ(x,y,z,i,j)
def IncreaseJ(x,y,z,i,j):
    j=j+1
    SecondCheck(x,y,z,i,j)
FirstCheck(x,y,z,i)

        
    
