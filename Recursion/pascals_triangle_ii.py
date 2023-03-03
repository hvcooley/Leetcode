#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 5 2022

@author: harrisoncooley
"""

class Solution:
    def getRow(self, ndx: int) -> list[int]:
        pascals = [[1], [1,1]]
        if ndx == 0:
            return pascals[0]
        elif ndx == 1:
            return pascals[1]
        for i in range(2, ndx+1):
            newList = []
            for j in range(i+1):
                #print("Looking at i: " + str(i) + " and j: " + str(j))
                if j == 0:
                    newList.append(1)
                elif j == i:
                    newList.append(1)
                else:
                    #print("In general case")
                    newList.append(pascals[i-1][j-1] + pascals[i-1][j])
            #END for j
            pascals.append(newList)
        #END for i
        return pascals[ndx]