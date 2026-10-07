# remember to have user insert filename
#make new txt file for output
import sys


target =input("Enter target file (ex. file.txt): ")
try:
    file = open(target, "r")
except:
    print("Target file " + target + " does not exist.")
    sys.exit(1)

outputName = input("Enter name of output file (ex. image.txt): ")

try: #attempt to create image file
    f = open(outputName, "x")
    f.close()
except: #if it exists, overwrite the old one
    f = open(outputName, "w") 
    f.close()

outputF = open(outputName, "a")
outputF.write("v3.0 hex words addressed\n")
lineCount = 0
count = 0
for line in file:
    instruction = 0
    Rm = 0
    Rn = 0
    Rt = 0
    total = 0
    if line[0:3] == "ADD":
        instruction = 0 #00
    if line[0:3] == "SUB":
        instruction = 1 #01
    if line[0:3] == "LDR":
        instruction = 2 #10
    if line[0:3] == "STR":
        instruction = 3 #11
    
    if line[4:6] == "X1":
        Rm = 0
    if line[4:6] == "X2":
        Rm = 1
    if line[4:6] == "X3":
        Rm = 2
    if line[4:6] == "X4":
        Rm = 3
    
    if line[7:9] == "X1":
        Rn = 0
    if line[7:9] == "X2":
        Rn = 1
    if line[7:9] == "X3":
        Rn = 2
    if line[7:9] == "X4":
        Rn = 3

    if line[10:12] == "X1":
        Rt = 0
    if line[10:12] == "X2":
        Rt = 1
    if line[10:12] == "X3":
        Rt = 2
    if line[10:12] == "X4":
        Rt = 3
    
    

    instruction = bin(instruction)[2:] #convert to string of bits, removing the initial "0b"
    Rm = bin(Rm)[2:]
    Rn = bin(Rn)[2:]
    Rt = bin(Rt)[2:]

    #Pad 0's to front of binary #'s so their lenths are all 2 bits
    instruction = instruction.zfill(2)
    Rm = Rm.zfill(2)
    Rn = Rn.zfill(2)
    Rt = Rt.zfill(2)
    
    

    total = instruction + Rm + Rn + Rt #concatenate the string into 1 number
    total = int(total, 2) #convert to an integer


    hexVal = hex(total)[2:] #convert to hexadecimal, remove the leasing "0x"
    hexVal = hexVal.zfill(2)
    if(count%16 == 0):
        if(count != 0):
            outputF.write("\n")
        outputF.write(hex(count)[2:].zfill(2) + ": " + hexVal)
        lineCount = lineCount + 1
    else:
        outputF.write(" " + hexVal)
    

    if(count == 16*16): #file is full!
        break
    
    count = count + 1

if(count != 16*16): #if not every line is full
    while(count != 16*16):
        if(count%16 == 0):
            if(count != 0):
                outputF.write("\n")
            outputF.write(hex(count)[2:].zfill(2) + ": " + "00")
            lineCount = lineCount + 1
        else:
            outputF.write(" " + "00")
        count = count +1

    

file.close()
outputF.close()


