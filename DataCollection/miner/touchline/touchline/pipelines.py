# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TouchlinePipeline(object):
    def process_item(self, item, spider):
 
        return item

class CSVWriterPipeline(object):
    def process_item(self, item, spider):
       fields = ["home_team", "goal_home", "goal_away", "away_team","score_time","scorer"] 
       with open('test.csv', 'a+') as f:
           f.write("{}\n".format('\t'.join(str(field) for field in fields)))
           for each in item['home_scores'].keys():
               f.write("{}\n".format('\t'.join([str(item['home_team']),\
                                             str(1),\
                                             str(0),\
                                             str(item['away_team']),\
                                             str(item['home_scores'][each]),\
                                             str(each)])))  
       
       return item

class CSVWriterPipeline2(object):
    def process_item(self, item, spider):
       fields = ["game_id","home_team", "goal_home", "goal_away", "away_team","score_time","scorer", \
                 "game_date","season","league","nation","half_score","final_score"] 
       with open('data.csv','a') as csvfile:
           writer = csv.DictWriter(csvfile,  fieldnames=fields)
           if(len(item['home_scores'])!=0 or len(item['away_scores'])!=0):
               
               for each in item['home_scores'].keys():
                   writer.writerow({'game_id':str(item['game_id']),\
                                'home_team': str(item['home_team']),\
                                'goal_home': str(1),\
                                'goal_away': str(0),\
                                'away_team': str(item['away_team']),\
                                'score_time': str(each),\
                                'scorer': str(item['home_scores'][each]),\
                                'game_date': str(item['date']),\
                                'season': str(item['season']),\
                                'league': str(item['league']),\
                                'nation': str(item['nation']),\
                                'half_score':str(item['half_time_score']),\
                                'final_score':str(item['final_score'])})
               for each in item['away_scores'].keys():
                   writer.writerow({'game_id':str(item['game_id']),\
                                'home_team': str(item['home_team']),\
                                'goal_home': str(0),\
                                'goal_away': str(1),\
                                'away_team': str(item['away_team']),\
                                'score_time': str(each),\
                                'scorer': str(item['away_scores'][each]),\
                                'game_date': str(item['date']),\
                                'season': str(item['season']),\
                                'league': str(item['league']),\
                                'nation': str(item['nation']),\
                                'half_score':str(item['half_time_score']),\
                                'final_score':str(item['final_score'])}) 

           else:
               writer.writerow({'game_id':str(item['game_id']),\
                                'home_team': str(item['home_team']),\
                                'goal_home': str(0),\
                                'goal_away': str(0),\
                                'away_team': str(item['away_team']),\
                                'score_time': "",\
                                'scorer': "",\
                                'game_date': str(item['date']),\
                                'season': str(item['season']),\
                                'league': str(item['league']),\
                                'nation': str(item['nation']),\
                                'half_score':str(item['half_time_score']),\
                                'final_score':str(item['final_score'])})
           
       return item
