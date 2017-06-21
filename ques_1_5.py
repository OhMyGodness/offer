# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:46:45 2017

@author: Luoxin
"""

################################ques_1####################################
class Solution:
    # array 二维列表
    def Find(self, target, array):
        def split_search(target,row):
            L = 0
            H = len(row)-1
            while 1:
                if H - L == 1:
                    if target == row[L] or target == row[H]:
                        return 1
                    else:
                        return 0
                if target <= row[int((L+H)/2)]:
                    L = L
                    H = int((L+H)/2)
                else:
                    L = int((L+H)/2)
                    H = H
                
        for row in array:
            if row:
            	if target >= row[0] and target <= row[-1]:
                 if split_search(target,row):
                     return 1
#                 for num in row:
#                     if target == num:
#                        	return 1
                    
        else:
            return 0
            
            
#array = [[1,2,3,10],[1,4,6,9],[1,4,7,8]]
#
#cls = Solution()
#print cls.Find(7,array)


##################################ques_2################################
'''
linkList,create a linkList from List([1,2,3,4]).
'''
class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        
class LinkList(object):
    def __init__(self):
        self.head = 0
    def initList(self,List):
        if List:
            self.head = Node(List[0])
            p = self.head
            for i in List[1:]:
                
                p.next = Node(i)
                p = p.next
            
            
            
        return self.head

                
    def getitem(self,index):

        j = 0
        p = self.head
        
        while  j < index:
            if  p is None:
                print 'index out of range...'
                return 
            j += 1    
            
            p = p.next
            
            
        return p.val

        
        
                
Link = LinkList()
p = Link.initList([1,2,3,4])               

class Solution2:
    def replaceSpace(self,s):
        L = s.split(' ')
        return '%20'.join(L)
        
cls = Solution2()
print cls.replaceSpace('we are  friend...')
#%%
while p:
    print p.val
    p = p.next
#%%
        








