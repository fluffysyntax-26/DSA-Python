from typing import List

def generate(numRows):
        res = [[1]]

        for i in range(numRows - 1): 
            temp = [0] + res[-1] + [0]
            row = []
            print(temp)
            for j in range(len(res[-1]) + 1): 
                row.append(temp[j] + temp[j+1])
            print(row, "\n")
            res.append(row)

        return res

print(generate(5))