#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 4 2022

@author: harrisoncooley
"""

class Solution:
    def helper(self, s: str, ndx: int):
        swapNdx = len(s)-ndx-1
        if ndx == swapNdx:
            return
        #END if
        store = s[swapNdx]
        s[swapNdx] = s[ndx]
        s[ndx] = store
        #print("The floor is " + str(floor(len(s)/2)))
        if swapNdx == ndx+1:
            return
        else:
            self.helper(s, ndx+1)
    #END helper
    
    def reverseString(self, s: list[str]) -> None:
        #print("The length of the string is " + str(len(s)))
        if not s:
            return
        self.helper(s, 0)
    #ENd reverseStrInPlace
