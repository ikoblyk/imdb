import pandas as pd
from pprint import pprint
from file import data1
from collections import defaultdict
import json
from collections import namedtuple
import threading
from pprint import pprint
# prime_mutiprocessing.py
from multiprocessing import Pool
from multiprocessing import freeze_support
from eralash import similar
from itertools import product



'''
Index(['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult',
       'startYear', 'endYear', 'runtimeMinutes', 'genres'],
      dtype='object')
'''


Movie = namedtuple('Movie', 'year id rate')

#l = pd.read_csv('/home/ivan/Documents/806999ebef28ccc786fa8aa85e0e220f/data',delimiter='\t',encoding='utf-8')
df_chunk = pd.read_csv(r'/home/ivan/Documents/806999ebef28ccc786fa8aa85e0e220f/data',delimiter='\t',encoding='utf-8', chunksize=100000, dtype={'startYear':'str'})

chunk_list = []  # append each chunk df here 

# Each chunk is in df format
for chunk in df_chunk:
    # perform data filtering

    # Once the data filtering is done, append the chunk to list
    chunk_list.append(chunk)

# concat the list into dataframe 
l = pd.concat(chunk_list)




originals = l["originalTitle"].tolist()
#year = l["startYear"].tolist()
#id = l["tconst"].tolist()
primary = l["primaryTitle"].tolist()





'''
def run_multiprocessing(func, i, j, n_processors):
    with Pool(processes=n_processors) as pool:
        pool.map(func, [originals[i], primary[i], i, j, data1[j], id[i], year[i]])



def is_prime(argss:[]):
    if (similar(originals[i], j) >= 0.5 or similar(primary[i], j) >= 0.5) and ((
            (str(argss[6]) == str(argss[4]['year']))  or (
            (str(argss[6]) == str(int(argss[4]['year']) - 1))) or (str(argss[6]) == str(int(argss[4]['year']) + 1)))):
        data1[j]['id'] = argss[6]
'''

def main(i, j):

    n_processors = 6


  #  run_multiprocessing(is_prime, i, j, n_processors)


'''
pprint(type(year[0]))

for i in range(len(originals)):
    if originals[i] in data1.keys():
        if (year[i] == int(data1[originals[i]]['year'])) or ((year[i]) - 1 == int(data1[originals[i]]['year'])) or (year[i] + 1 == int(data1[i]['year'])):
            data1[originals[i]]['id'] = id[i]

    elif primary[i] in data1.keys() :
        if (year[i] == int(data1[primary[i]]['year'])) or ((year[i]) - 1 == int(data1[primary[i]]['year'])) or (year[i] + 1 == int(data1[primary[i]]['year'])):
            data1[primary[i]]['id'] = id[i]
    else:
        for j in data1.values():
            if len(j)!=3:
                if j['ukr_nazva'] == originals[i]:
                    if (year[i] == int(j['year'])) or ((year[i])-1 == int(j['year'])) or (year[i]+1 == int(j['year'])):
                        j['id'] = id[i]
                elif j['ukr_nazva'] == primary[i]:
                    if (str(year[i]) == str(j['year'])) or (str(year[i]) == str(int(j['year']) - 1)) or (
                            str(year[i]) == str(int(j['year']) + 1)):
                    j['id'] = id[i]

'''
for j in data1.keys():
    res = similar(originals[:50], j)
    if list(res).__len__()!=0:
        pprint(res)


pprint(originals[:50])



def write():
    with open('waht_left_ids.json', "w") as write_file:
        json.dump(data1, write_file, indent=4)








