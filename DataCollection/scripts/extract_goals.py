import sys
import re

def save_as_file(data,filename):
    fileout = open(filename,'wb')
    fileout.write(data)
    fileout.close() 


def extract_nation(lines, nation):
    data = "" 
    for line in lines:
        line_array = line.split(',')
        if(line_array[10].split(' ')[0] == str(nation)):
            data += str(line_array[0]) + '\t' + str(line_array[2]) + \
                        '\t' + str(line_array[3]) + '\t' + \
                        str(line_array[5]) + '\t' + \
                        str(line_array[7]) + '\t' + \
                        str(line_array[9]) + '\n'
    return data        

def extract_all(lines):
    data = ""
    for line in lines:
        line_array = line.split(',')
        data += str(line_array[0]) + '\t' + str(line_array[2]) + \
                        '\t' + str(line_array[3]) + '\t' + \
                        str(line_array[5]) + '\t' + \
                        str(line_array[7]) + '\t' + \
                        str(line_array[9]) + '\n'
    return data  


def main():
    arguments = sys.argv
    nation = arguments[1]
     
    #read data
    filein = open('data.csv','rb')
    lines = filein.readlines()

    #extract data
    data = extract_nation(lines, nation)

    filein.close()
   
    #save file
    filename = str(nation) + '.txt'
    save_as_file(data,filename)


    #save as a big file
    data2 = extract_all(lines)
    filename = 'all.txt'
    save_as_file(data2, filename)  

if __name__ == '__main__':
    main()   
