from datetime import datetime

currtime = datetime.now().strftime("%d/%m/%y %H:%M:%S")
print(currtime)
f = str(currtime)
file_name = f + ".txt"
print(file_name)
file = open("file_name", 'w')
file.write(datetime.now().strftime("%d/%m/%y %H:%M:%S"))
file.close()
file = open("file_name", 'r')
print(file.read())
