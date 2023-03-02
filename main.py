# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:57:08 2023

@author: ASUS
"""

import sys

import pandas as pd
import numpy as np
from tqdm import tqdm


print("Yeditepe_UBY", "hello truba, python version : ")
print(sys.version, __name__)

numbers = np.array([1, 2, 3])
print(numbers)

for x in tqdm(range(100000)):
    pass

print("END OF JOB!")