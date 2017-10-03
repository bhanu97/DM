import os

dict_of_extensions ={}  #Dictionary of extensions
dict_of_extensions["NoTypeFound"] =0;   # Files with no extensions
fold =[]      # list of subfolders
files = []  # List of all files

    
def first_iteration(fold_addr):    #Function to return the result of first iteration 
    list_subfolders = os.listdir(fold_addr)
    return list_subfolders    # result of the  first iteration


def sub_fold_search(listx,location): #function to find files inside sub folders
    new_location = location          #listx -list of folders and subfolders to iterate
    for i in listx:
        new_location=location
        new_location+='\\'+i
        try:
            subfold_contents = os.listdir(new_location)
        except WindowsError:
             files.append(i)
             new_location=location
             continue
        if len(subfold_contents)!=0:
            fold.append(i)
            sub_fold_search(subfold_contents,new_location)
            
def dict_create(files):
    for j in files: 
        k = 0    # position of te current letter
        pos = 0  # position of last '.' in the filename 
        for j1 in j:
            k+=1
            if j1==".":
                pos = k

        if pos==0:
           dict_of_extensions["NoTypeFound"]+=1         
        else :
            extension_type = j[pos:]    
            if extension_type in dict_of_extensions.keys():
                dict_of_extensions[extension_type]+=1
            else:
                dict_of_extensions[extension_type] =1

def getCountForFileTypes(fold_addr):
    list12 = first_iteration(fold_addr)
    sub_fold_search(list12,fold_addr)
    dict_create(files)
    return dict_of_extensions

def getTotalFileCount(fold_addr):
    list11 = first_iteration(fold_addr)
    sub_fold_search(list11,fold_addr)
    return len(files)


