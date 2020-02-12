import pandas as pd
from string import ascii_lowercase
from collections import defaultdict
from pprint import pprint
from eralash import similar
from file import data1


a = defaultdict()
l = [i for i in range(10)]


a['itmes'] = list(data1.keys())[:21]

pprint(a)


for i in range(20):
    a[i] = 'a'


frame = pd.DataFrame(a, index=a.keys())

a = [(similar('The Lodger: A Story of the London Fog (1927)', i), i) for i in frame['itmes'].tolist()]

pprint(frame)

pprint(a)