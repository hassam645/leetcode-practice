class Solution:
    def KthSmallest(self,matrix: list[list[int]], k:int)->bool:
        arr=[]
        for i in matrix:
            for j in i:
                arr.append(j)
                arr.sort()
                return arr(k-1)