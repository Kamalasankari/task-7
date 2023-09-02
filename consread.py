file1 = open("../myfile.txt", 'w')
L = ["This the task given by guvi \nto read the content of the file \nin the console"]
file1.writelines(L)
file1.close()
file1 = open("../myfile.txt", 'r')
print("Content in the file is ")
print(file1.read())
print()