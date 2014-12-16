import os 

nations = ['England','Brazil', 'Germany','Italy', 'Spain','France','Portugal','Netherlands','Australia','Belgium','Turkey',"Czech",'Argentina']

seasons = ['2001/2002','2002/2003','2003/2004','2004/2005','2005/2006','2006/2007','2007/2008','2008/2009','2009/2010','2010/2011','2011/2012','2012/2013','2013/2014','2014/2015']

def main():
    for nation in nations:
        for season in seasons:
            command = 'python extract_goals_by_season.py ' + str(nation) + ' ' + str(season)
            os.system(command)     

if __name__ == '__main__':
    main()
