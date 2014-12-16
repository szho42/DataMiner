import sys
import re

def save_as_file(data,filename):
    fileout = open(filename,'wb')
    fileout.write(data)
    fileout.close() 


def extract_nation(lines, nation,season):
    data = "" 
    for line in lines:
        line_array = line.split(',')
        if(line_array[10].split(' ')[0] == str(nation)):
            if(line_array[8]==str(season)):
                data += str(line_array[0]) + '\t' + str(line_array[2]) + \
                        '\t' + str(line_array[3]) + '\t' + \
                        str(line_array[5]).replace('OG','') + '\t' + \
                        str(line_array[7]) + '\t' + \
                        str(line_array[9]) + '\n'
    return data        


def main():
    arguments = sys.argv
    nation = arguments[1]
    season = arguments[2]
     
    #read data
    filein = open('data.csv','rb')
    lines = filein.readlines()

    #extract data
    data = extract_nation(lines, nation, season)

    filein.close()
   
    #save file
    filename = str(nation)+'-'+str(season).replace('/','-') + '.txt'
    save_as_file(data,filename)


if __name__ == '__main__':
    main()   
