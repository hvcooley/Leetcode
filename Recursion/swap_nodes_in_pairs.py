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
    def helper(self, curr: Optional[ListNode], trail: Optional[ListNode]):
        if not curr or not curr.next:
            return
        secNode = curr.next
        curr.next = secNode.next
        secNode.next = curr
        if trail:
            trail.next = secNode
        self.helper(curr.next, curr)
  #END helper
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        storeHead = head
        if head.next:
            head = head.next
        self.helper(storeHead, None)
        return head
  #END swapNodes
        