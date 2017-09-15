import sys

list1 = ["for","if","while","else if","else","int","float","void","char"]

myfile =open("d.c")


def myfunc4(num2,key2,count2):
    myfile4 = open('d.c', 'r').readlines()[num2:]
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
    bt= True
    count1 = 0 
    myfile3 = open('d.c', 'r').readlines()[num1:]
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
               bt =False
               break
        if not bt:
           break
    if bt:
       myfunc2(num1,key1)
       
    else:
        #print count1
        myfunc4(num1,key1,count1+1)
           
'''def myfunc5():
    myfile5 =open("d.c")
    for i in list2:
        nb1 = True
        hp1 =True
        bt1 = True
        for j in myfile5:
            if i in j:
               for k in j:
                   if k=='(':
                      nb1 =False
                   elif k==')':
                        nb1 =True
                   if k==';' and nb1:
                        hp1 =
               
 '''      


def myfunc2(num,key):
    brac = 1    # num of bracs
    c = False   
    myfile2 = open('d.c', 'r').readlines()[num:]
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
    count = 0   #line num
    for i in myfile:
        count+=1
        for j in list1:
            if j=="else":
               if j in i and "if"  not in i:
                  print "\n *****************************************NEW BLOCK******************************************************************"
                  myfunc3(count-1,j)
            elif j=="if":
                 if j in i and "else"  not in i:
                    print "\n *****************************************NEW BLOCK******************************************************************"
                    myfunc3(count-1,j)
            else:
                if j in i:
                   print "\n *****************************************NEW BLOCK******************************************************************"
                   myfunc3(count-1,j)
myfunc(myfile)

