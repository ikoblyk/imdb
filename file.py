import numpy as np
import pandas as pd
from pprint import pprint
from transliteration import cyrrylic_check, transalte
from collections import namedtuple, defaultdict
import json
from tr_test import  rus_ua
from ukr_transliter import translit
from eralash import similar


#data = pd.read_html(r'/home/ivan/Documents/kinopoisk.ru-4878092-votes.xls')
#Film_left = namedtuple('Film', 'year id rate')

with open('waht_left_ids.json', "r") as read_file:
    data1 = json.load(read_file)




'''
o = dict()
for i in data1.keys():
    if data1[i]['id']=='-':
        o[i] = Film_left(data1[i]['year'], data1[i]['id'],  data1[i]['rate'])._asdict()

with open('waht_left_ids.json', "w") as write_file:
    json.dump(o, write_file, indent=4)
'''








