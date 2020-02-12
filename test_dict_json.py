import json
from collections import namedtuple, defaultdict

Data = namedtuple('Data', 'year name suename')
d = defaultdict()


for i in range(5):
    key = str(input('key:'))
    name = str(input('name:'))
    year = str(input('year:'))
    suename = str(input('suename:'))
    d[key] = Data(year, name, suename)._asdict()


print(json.dumps(d))




