#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 5 2022

@author: harrisoncooley
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def helper(self, LL1, LL2, carry, ansCurr):
        if not LL1 and not LL2:
            if carry == 1:
                newNode = ListNode(carry)
                ansCurr.next = newNode
                ansCurr = newNode
            return
        elif LL1 and not LL2:
            newVal = LL1.val + carry
            if newVal > 9:
                carry = 1
                newVal = newVal-10
            else:
                carry = 0
            newNode = ListNode(newVal)
            ansCurr.next = newNode
            ansCurr = newNode
            self.helper(LL1.next, None, carry, ansCurr)
        #END elif
        elif LL2 and not LL1:
            newVal = LL2.val + carry
            if newVal > 9:
                carry = 1
                newVal = newVal-10
            else:
                carry = 0
            newNode = ListNode(newVal)
            ansCurr.next = newNode
            ansCurr = newNode
            self.helper(None, LL2.next, carry, ansCurr)
        #END elif
        else:
            newVal = LL1.val + LL2.val + carry
            if newVal > 9:
                carry = 1
                newVal = newVal-10
            else:
                carry = 0
            newNode = ListNode(newVal)
            ansCurr.next = newNode
            ansCurr = newNode
            self.helper(LL1.next, LL2.next, carry, ansCurr)
        #END else
    #END helper

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        self.helper(l1, l2, 0, dummyNode)
        ans = dummyNode.next
        return ans
    #END addTwoNumbers
        