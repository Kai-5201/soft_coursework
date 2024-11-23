# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:05:00 2024

@author: 22930
"""

import pandas as pd
import numpy as np


class fish_status:
    
    fish_type = np.array([100.0,12,2,2.0,50.0,9,2,1.0,90.0,6,2,0.5,100.0,10,2,2.0,200.0,12,2,2.5,300.0,12,6,3.0])
    fish_type = fish_type.reshape(6,4)
    fish_type = pd.DataFrame(fish_type,index=['Clef Fins','Timpani Snapper','Andalusian Brim','Plagal Cod','Fugue Flounder','Modal Bass'],
                        columns=['Fertilizers (ml)','Feed (kg)','Salt (kg)','Maintenance Time (in days)'])


    #due to the unit of Capacity in fertiliser is different, so need to covret(暂未解决，看后续哪个单位常用再进行)
    #*time is quarter and hatchery pays fixed quarterly cost of 1500,start  cash is 10000
    #supply = np.array([20,10,0.4,0.10,400,200,0.1,0.001,200,100,0.0,0.001])
    #supply = supply.reshape(3,4)
    #supply =pd.DataFrame(supply,index=['Fertiliser','Feed','Salt'],columns=['Main Capacity','Aux Capacity','Depreciation','Warehouse Costs']) 


    vendors = np.array([0.3,0.1,0.05,0.2,0.4,0.25])
    vendors = vendors.reshape(2,3)
    vendors = pd.DataFrame(vendors,index=['Slippery Lakes','Scaly Wholesaler'],columns=['Fertiliser','Feed','Salt'])
    vendors.iloc[0,1]

    vendors.insert(0,'d','l')# 可能单位转换会用到

    demand = np.array([25,250,10,350,15,250,20,400,30,550,50,500])
    demand = demand.reshape(6,2)
    demand = pd.DataFrame(demand,index=['Clef Fins','Timpani Snapper','Andalusian Brim','Plagal Cod','Fugue Flounder','Modal Bass'],
                          columns=['Demand','Price'])
    sellnumber = 0
    def __init__(self,number_labour):
        self.List1 = pd.DataFrame(np.nan,range(6),range(5))
        self.List1 = pd.DataFrame(self.List1,index=['Clef Fins','Timpani Snapper','Andalusian Brim','Plagal Cod','Fugue Flounder','Modal Bass'],
                            columns=['Fertilizers (ml)','Feed (kg)','Salt (kg)','Maintenance Time (in days)','Sell number'])
        #self.List2 = pd.DataFrame([[20,10],[400,200],[200,100]],index=['Fertiliser','Feed','Salt'],columns=['Main Capacity','Aux Capacity'])
        supply = np.array([20,10,0.4,0.10,400,200,0.1,0.001,200,100,0.0,0.001])
        supply = supply.reshape(3,4)
        
        supply =pd.DataFrame(supply,index=['Fertiliser','Feed','Salt'],columns=['Main Capacity','Aux Capacity','Depreciation','Warehouse Costs']) 

        self.List2 = supply
        self.List2['Total'] = self.List2['Main Capacity'] + self.List2['Aux Capacity']
        self.List2.loc['Feed':'Salt','Warehouse Costs'] = self.List2.loc['Feed':'Salt','Warehouse Costs'] * 1000
        self.days = 5
        self.workdays = number_labour * self.days * 9#9 is the working week of labour 
        self.currentdays = 0
        self.available_week = self.workdays/self.days
        
        