import scrapy
from touchline.items import TouchlineItem
import urlparse
import ids


class TouchlineSpider(scrapy.Spider):
    name = "touch-line-spider"
    allowed_domains = ["wettbasis.touch-line.com"]
   
    def start_requests(self):
        urls = []

        filein = open('entries.txt','rb')
        lines = filein.readlines()

        for each in lines:
            CTID = each.split(',')[0]
            CPID = each.split(',')[1]
            MAID = each.split(',')[2].replace('\n','')
            urls.append(scrapy.FormRequest(url="http://wettbasis.touch-line.com/",\
					method="GET",\
					formdata={'Lang':'0','CTID':CTID, 'CPID':CPID,\
					'MAID': str(MAID), 'pStr':'Match_Details'},
					callback=self.parse))
        return urls


#        for eachCountry in ids.ids.keys():
#            CTID = ids.ids[str(eachCountry)]['CTID'] 
#            CPID = ids.ids[str(eachCountry)]['CPID']
#            for eachID in ids.ids[str(eachCountry)]['IDs']:
#                startID = eachID[0]
#                endID = eachID[1]
#                for game_id in range(startID, endID,1):
#                    urls.append(scrapy.FormRequest(url="http://wettbasis.touch-line.com/",\
#					method="GET",\
#					formdata={'Lang':'0','CTID':CTID, 'CPID':CPID,\
#					'MAID': str(game_id), 'pStr':'Match_Details'},
#					callback=self.parse))

        #for game_id in range(493586,493725,1):
        #    urls.append(scrapy.FormRequest(url="http://wettbasis.touch-line.com/",\
#					method="GET",\
#					formdata={'Lang':'0','CTID':'11', 'CPID':'4',\
#					'MAID': str(game_id), 'pStr':'Match_Details'},
#					callback=self.parse))

    def get_season(self,date):
        date_array = date.split("/")
        season = None
        if(int(date_array[1])<7):
           temp_year = int(date_array[2])
           season = str(temp_year-1)+"/"+str(temp_year)
        else:
           temp_year = int(date_array[2])
           season = str(temp_year)+"/"+str(temp_year+1)
        return season

    def parse(self, response):
        item = TouchlineItem()
        try:
            #get game ids on touch-line.com
            parsed_url = urlparse.urlparse(str(response.url)) 
            MAID = urlparse.parse_qs(parsed_url.query)['MAID'][0]
            item['game_id'] = MAID

            #get leagure and nation information
            league_info = response.xpath("//td[@class='tabHeadL']/text()").extract()
            item['league'] = league_info[0].encode('ascii','ignore').replace(' ','').replace('-','')
            item['nation'] = league_info[1].encode('ascii','ignore')

            #get date information
            date = response.xpath("//td[@class='med']/b/text()").extract()
            item['date'] = date[0].encode('ascii','ignore').replace(' ','')

            item['season'] = self.get_season(item['date'])
            
            #get team information
            teams_socre = response.xpath("//td[@class='titlebarsub2']/b/text()").extract()
            print teams_socre
            

            #get home score information
            home_scores_players = response.xpath("//div[@class='statscol']/table[3]//tr[2]/td[1]//table//tr[contains(@class,'tabCell')]//a/text()").extract()
            home_scores_mins = response.xpath("//div[@class='statscol']/table[3]//tr[2]/td[1]//table//tr[contains(@class,'tabCell')]//td/text()").extract()
            home_scores = {}
            for index in range(len(home_scores_players)):
                home_scores[home_scores_mins[2*index+1].encode('ascii','ignore').replace(' ','')\
                              .replace('(','').replace(')','')] = \
                    home_scores_players[index].encode('ascii','ignore').replace(' ','')\
                              .replace('(','').replace(')','')
                          
            #get away score information 
            away_scores_players = response.xpath("//div[@class='statscol']/table[3]//tr[2]/td[3]//table//tr[contains(@class,'tabCell')]//a/text()").extract()
            away_scores_mins = response.xpath("//div[@class='statscol']/table[3]//tr[2]/td[3]//table//tr[contains(@class,'tabCell')]//td/text()").extract()

            away_scores = {}
            for index in range(len(away_scores_players)):
                away_scores[away_scores_mins[2*index+1].encode('ascii','ignore').replace(' ','')\
                              .replace('(','').replace(')','')] = \
                    away_scores_players[index].encode('ascii','ignore').replace(' ','')\
                              .replace('(','').replace(')','')

            if(len(home_scores)==0 and len(away_scores)==0):
                item['home_team'] = teams_socre[0].encode('ascii','ignore')  
                item['away_team'] = teams_socre[2].encode('ascii','ignore')
                item['home_scores'] = home_scores 
                item['away_scores'] = away_scores
                item['half_time_score'] = teams_socre[1].encode('ascii','ignore') 
                item['final_score'] = teams_socre[1].encode('ascii','ignore') 
            else:
                item['home_team'] = teams_socre[0].encode('ascii','ignore')  
                item['away_team'] = teams_socre[3].encode('ascii','ignore')    
                item['half_time_score'] = teams_socre[2].encode('ascii','ignore').replace('(','').replace(')','')
                item['final_score'] = teams_socre[1].encode('ascii','ignore')
 
                item['home_scores'] = home_scores
                item['away_scores'] = away_scores

        except Exception:
            print "Catch errors"
            pass

        yield item
