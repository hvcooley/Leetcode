#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 7 2022

@author: harrisoncooley
"""

#Before Python 3.9 list or tuple (lowercase) would not be able to type check
# contents of the colleciton, so there were Generic types List and Tuple to do
# that. But now that feature has been implemented into the built in list 
# and tuple (lowercase)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        maxRange = 0
        ndx = 0
        while ndx < len(nums):
            if nums[ndx] > 0:
                ndxRange = ndx + nums[ndx]
                if ndxRange > maxRange:
                    maxRange = ndxRange
                ndx += 1
            #END if
            else:
                while nums[ndx] == 0 and ndx != len(nums)-1:
                    ndx += 1
                #END while
                if maxRange < ndx and ndx < len(nums):
                    return False
                elif ndx == len(nums)-1:
                    ndx += 1
            #END else
        #END while
        if maxRange >= len(nums)-1:
            return True
        else:
            return False