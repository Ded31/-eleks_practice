name = input("File name: ")

write_file = open("file2.txt", "w") 

try:
  with open(name, "r") as read_file: 
    txt = read_file.read()
    reversed = txt[::-1]
    write_file.write(reversed) 
    write_file.close()
except:
    print("File not found")
 
