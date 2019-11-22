#-*- coding:utf-8 -*-
#usr!/bin/envy python3

import sys
class Solution():
    def solveFloyd(self,dist,start,end): #核心算法
        n = len(dist)
        path = self.createPath(n)
        for k in range(n):               #遍历节点，设成中介点
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]: #如果路程更短
                        dist[i][j] = dist[i][k] + dist[k][j] #更新D、P矩阵
                        path[i][j] = path[i][k]
        self.printPath(start,path,end) #输出

    def createPath(self,n):
        return [[i for i in range(n+1)] for i in range(n+1)]
        # path =[]
        # for i in range(n):
        #     row = []
        #     for j in range(n):
        #         row.append(j)
        #     path.append(row)
        # return path

    def printPath(self,current,path,end):
        solution = []
        while current != end:
            solution.append(current)
            current = path[current][end]
        solution.append(current)
        print(solution)

origin_dist = [[0, 10, 15, sys.maxsize, 30, sys.maxsize],
               [10, 0, sys.maxsize, 5, 14, sys.maxsize],
               [15, sys.maxsize, 0, 12, 12, sys.maxsize],
               [sys.maxsize, 5, 12, 0, sys.maxsize, 10],
               [30, 14, 12, sys.maxsize, 0, 20],
               [sys.maxsize, sys.maxsize, sys.maxsize, 10, 20, 0]]
Solution().solveFloyd(origin_dist,0,5)
                        
