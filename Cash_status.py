# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:05:03 2024

@author: 22930
"""

import pandas as pd
import numpy as np

class money:
    def __init__(self,List1,List2,cash):
        self.cash = cash
        self.fix_quarterly_cost = 1500
        self.person_weeklyRate = 500
        self.work_week = 12
        self.List1 = List1 #type_fish
        self.List2 = List2 #warehouse

      