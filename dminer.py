import sys

list1 = ["for","if","while","else if","else","int","float","void","char"]
list2 = ["int","float","void","char"]

myfile =open("example.c") # Give the input c file here


def myfunc4(num2,key2,count2):
    myfile4 = open('example.c', 'r').readlines()[num2:]
    for i4 in myfile4:
        sr = False
        for i5 in i4:
            sys.stdout.write(i5)
            if i5==';':
               count2-=1
            if count2==0:
               sr = True
               break 
        if sr:
           print "\n"
           break
            

def myfunc3(num1,key1):
    nb = True
    hp =True
    bt= 1 
    count1 = 0 
    myfile3 = open('example.c', 'r').readlines()[num1:]
    if key1 in list2:
       bt =3
       for i3 in myfile3:
        for i4 in i3:
            if i4 =='(':
               nb =False
            if i4 ==';':
               hp = False
            if not nb and hp and i4 =='{':
               bt =1 
               break
               
    else:        
        for i3 in myfile3:
            for i4 in i3:
                if i4 =='(':
                   nb =False
                elif i4 ==')':
                     nb = True
                elif i4 =='{':
                     hp =False
                if not nb and i4 ==';':
                   count1+=1  
                if nb and hp and i4 ==';':
                   bt = 0
                   break
            if bt==0:
               break
               
    if bt==1:
       print "\n *****************************************NEW BLOCK******************************************************************"
       myfunc2(num1,key1)
       
    elif bt==0:
        print "\n *****************************************NEW BLOCK******************************************************************"
        myfunc4(num1,key1,count1+1)
           
 
def myfunc2(num,key):
    brac = 1    
    c = False   
    myfile2 = open('example.c', 'r').readlines()[num:]
    for i1 in myfile2:
        for i2 in i1:
            if i2 =='{':
               brac+=1
               c = True
            if i2=='}':
                 brac-=1
            if c and brac==1:
               break;
            sys.stdout.write(i2)
        

def myfunc(myfile):
    count = 0   
    for i in myfile:
        count+=1
        for j in list1:
            if j=="else":
               if j in i and "if"  not in i:
                  myfunc3(count-1,j)
            elif j=="if":
                 if j in i and "else"  not in i:
                    myfunc3(count-1,j)
            else:
                if j in i:  
                   myfunc3(count-1,j)
                   
myfunc(myfile)


