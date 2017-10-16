from collections import defaultdict
from pprint import pprint

class makeParser:
      def __init__(self,location):
          self.location = location
          global fileList
          global targetList
          global variable_dict
          global dependencies_target
          dependencies_target= defaultdict(list)
          fileList =[]
          variable_dict ={}
          targetList =[]
          fileList = open(self.location).readlines()
          self.mainParser()
      def mainParser(self):
          for i in fileList:
              ind = fileList.index(i)
              fileList[ind]= fileList[ind].rstrip()
              i =fileList[ind]
              if i:
                 if i[0]=='#':
                    continue
                 elif '#' in i:
                      j =fileList.index(i)
                      fileList[j] = i[0:i.index('#')]
                      i = fileList[j]
                 if ":=" in i or '=' in i:
                      self.extractVariable(fileList.index(i))
                 elif ":" in i:
                      self.extractTarget(fileList.index(i))
      def extractTarget(self,Index):
          pos = fileList[Index].index(':')
          target = fileList[Index][0:pos-1]
          targetList.append(target)
          self.extractDependencies(Index,target)

      def extractVariable(self,Index):
          if ':=' in fileList[Index]:
              pos = fileList[Index].index('=')-1
              variable_value = fileList[Index][pos+3:]
          else:
              pos = fileList[Index].index('=')
              variable_value = fileList[Index][pos+2:]
          variable = fileList[Index][0:pos-1]
          variable_dict[variable]= variable_value
          str_tobe_replaced ="$("+str(variable)+")"
          for i in fileList:
              if str(str_tobe_replaced) in i:
                 x = fileList.index(i)
                 fileList[x]= fileList[x].replace(str_tobe_replaced,variable_value)

      def extractDependencies(self,Index,target):
          pos = fileList[Index].index(':')
          x = fileList[Index][pos+1:].strip()
          y = len(x.split(' '))
          k=0
          while k<y:
                if x.split(' ')[k]=="\\":
                   x = fileList[Index+1][pos+1:].strip()
                   k= 0
                   y =len(x.split(' '))
                else:
                    dependencies_target[target].append(x.split(' ')[k])
                    k+=1

      def print_dependencies(self):
          for i in dependencies_target:
              for j in dependencies_target:
                  if i in dependencies_target[j]:
                     dependencies_target[j]+= dependencies_target[i]
              dependencies_target[i] = list(set(dependencies_target[i]))
              print i +":"
              print  dependencies_target[i]


x = makeParser('C:/Users/C58717/Downloads/b.makefile') #Input file
x.print_dependencies()
