import os 

nations = ['England','Brazil', 'Germany','Italy', 'Spain','France','Portugal','Netherlands','Australia','Belgium','Turkey',"Czech",'Argentina']

def main():
    for each in nations:
        command = 'python extract_goals.py ' + str(each)
        os.system(command)     

if __name__ == '__main__':
    main()
