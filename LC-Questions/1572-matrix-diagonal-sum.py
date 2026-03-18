from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1: 
            return mat[0][0]
        
        if len(mat)/2 != 0:
            total = 0
            for i in range(len(mat)): 
                total += mat[i][i]

            total += mat[0][len(mat)-1]
            total += mat[len(mat)-1][0]

            return total
        else: 
            a = -1
            b = len(mat)
            for i in range(len(mat)): 
                total += mat[i][i]
                total += mat[a+1][b-1]
            
            return total