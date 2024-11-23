# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:07:28 2024

@author: 22930
"""

import numpy as np
import pandas as pd

class technician:
    #samename check 未实现  2.加后缀 麻烦有时间后可优化

    exist = 0
    def __init__(self):
        self.List = pd.DataFrame(np.nan,range(5),range(2))
        self.List.columns = ['name','time']
        self.time = 0
        self.exist = 0
 
