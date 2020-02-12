from imdb import IMDb
from pprint import pprint
# prime_mutiprocessing.py

import time
import math
from multiprocessing import Pool
from multiprocessing import freeze_support
from eralash import similar


'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i,j, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i, is_prime(i, j))

originals = [12313]
year = [123123]
primary = []
data1 = {}
id = []
'''Define task function'''


def is_prime(i, j):
    if (similar(originals[i], j) >= 0.5 or similar(primary[i], j) >= 0.5) and ((
            (str(year[i]) == str(data1[j]['year'])) or (
            (str(year[i]) == str(int(data1[j]['year']) - 1)) or (str(year[i]) == str(int(data1[j]['year']) + 1))))):
        data1[j]['id'] = id[i]



def main():


    '''
    set up parameters required by the task
    '''

    n_processors =6

    '''
    pass the task function, followed by the parameters to processors
    '''
    out = run_multiprocessing(is_prime, 10, 9, n_processors)

    pprint(data1)


if __name__ == "__main__":

    freeze_support()   # required to use multiprocessing
    main()