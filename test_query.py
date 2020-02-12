from eralash import similar
import pandas as pd
from pprint import pprint
import numpy as np


def test():
    a = {'Ivan Koblyk':['hui', '234', '234'], 'LIubomyr Koblyk':['manda', 'sdf', '123'], 'Andrew_Horpenko':['putin huilo', '134', 'hui ebanyi']}
    test1 = pd.DataFrame(a)
    mask = similar(test1.iloc[0].tolist(), 'hui')
    pprint(mask)


if __name__ == '__main__':
    test()
