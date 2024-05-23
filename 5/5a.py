 
file1 = open("/Users/radhikakolavali/python/file1.txt", "r")  
file2 = open("File.txt", "w")  
num = 1 
for line in file1:  
    file2.write(str(num)  + ":" +line) 
    num = num + 1 
file1.close()  
file2.close() 
print ("Contents read from file1.txt and copied to File.txt") 