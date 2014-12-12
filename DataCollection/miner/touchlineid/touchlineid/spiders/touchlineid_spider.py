import scrapy
from touchlineid.items import TouchlineidItem
import urlparse
import years
import pickle

class TouchlineidSpider(scrapy.Spider):
    name = "touchlineid-spider"
    allowed_domains = ["wettbasis.touch-line.com"]

    def start_requests(self):
        urls = []
        
        for eachCountry in years.years.keys():
            CTID = years.years[str(eachCountry)]['CTID']
            CPID = years.years[str(eachCountry)]['CPID']
            for eachSeason in years.years[str(eachCountry)]['seasons']:
                urls.append(scrapy.FormRequest(url="http://wettbasis.touch-line.com/",\
                                        method="GET",\
                                        formdata={'Lang':'0','CTID':CTID, 'CPID':CPID,\
                                        'type':'R', 'Season': str(eachSeason),\
                                        'pStr':'Comp_Fixture'},
                                        callback=self.parse))
        return urls


    

    def parse(self, response):
        item = TouchlineidItem()
        try:
            #get season on touch-line.com
            parsed_url = urlparse.urlparse(str(response.url))
            season = urlparse.parse_qs(parsed_url.query)['Season'][0]
            item['season'] = season

            item['CTID'] = urlparse.parse_qs(parsed_url.query)['CTID'][0]
            item['CPID'] = urlparse.parse_qs(parsed_url.query)['CPID'][0]

            MAIDs = []
            id_info1 = response.xpath("//tr[@class='tabLnk1']").re(r'MAID=[0-9]*')
            for each in id_info1:
                MAIDs.append((item['CTID'],item['CPID'], str(each).split('=')[1])) 
            id_info2 = response.xpath("//tr[@class='tabLnk2']").re(r'MAID=[0-9]*')
            for each in id_info2:
                MAIDs.append((item['CTID'],item['CPID'], str(each).split('=')[1]))

            item['MAID'] = MAIDs
        except Exception:
            print "catch error"
            pass

        yield item 



