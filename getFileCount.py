import projectParser

fold_add = raw_input("Enter the location of directory: ")
results = projectParser.getTotalFileCount(fold_add)
print "Total number of files in the directory: "
print results
results1 = projectParser.getCountForFileTypes(fold_add)
print results1
