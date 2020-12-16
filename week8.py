import os #imports the library 

#def GetInfo():   # get name, address, and phone number 
    #name = input("What is your name: ")
    #address = input("What is your address: ")
    #number = input("what is your phone number: ")



directory = input("Please inser the path to where you want the file: " '')
file_name = input("What do you want the file name to be: ")
path = directory+file_name

if os.path.isdir(directory): #check if file path exists
    print('Directory Exists')
else:
    print("No directory found: Creating New one.") #create directory if it doesnt exist
    os.mkdir(directory) 


name = input("What is your name: ")
address = input("What is your address: ")        #Get info from user
number = input("what is your phone number: ")
information = [name, address, number]

with open(path, 'w') as fileHandle: #opens the file for writing
    fileHandle.write(str(information)) #write data to file

with open(path, 'r') as fileHandle: #opens the same file for reading
   data = fileHandle.read() #read data from the file
   print(data) #print to user
   print(path)


