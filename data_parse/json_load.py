import json
import sys, os
from data_parse.database import Database
sys.path.append(os.path.abspath(os.path.join('..', 'data_parse')))
db = Database()


class JsonParse:
    ##################################################
    #Parses string json inpiut into list of Dictionary
    ##################################################
    def __init__(self):
        self.res_dict = []
    def get(self):
        for line in db.read():
             self.res_dict.append(json.loads(line))
        return self.res_dict
