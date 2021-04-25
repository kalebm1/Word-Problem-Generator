

filer = open("C:/Users/kaleb/OneDrive/Desktop/code projects/Python Projectws/Word Problem Generator/etc/again/item-list.txt")

fileL = filer.readlines()
count = 0
for line in fileL:
    char = line[len(line)-2]
    print(char)
    if(char!='s' and char!='x'):
        line = line.rstrip("\n")+"s"
        line+="\n"
        fileL[count] = line
    if(char=='x'):
        line = line.rstrip("\n")+"es"
        line+="\n"
        fileL[count] = line
    count+=1
filer.close()

filer = open("C:/Users/kaleb/OneDrive/Desktop/code projects/Python Projectws/Word Problem Generator/etc/again/item-list.txt","w")

filer.writelines(fileL)

filer.close()