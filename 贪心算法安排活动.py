#-*- coding:utf-8 -*-
#usr!/bin/env python

def bubble_sort(s,f):
    for i in range(len(f)):
        for j in range(0,len(f)-i-1):
            if f[j] > f[j+1]:
                f[j], f[j+1] = f[j+1], f[j]
                s[j], s[j+1] = s[j+1], s[j]
    return s, f

def greedy_activity(s,f,n):
    a = [True for x in range(n)]
    j=0
    for i in range(1,n):
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a

n = int(input("""请输入活动数量和起始时间（数量和活动用回车分隔，
    活动之间用空格分隔。例如：6（回车） （1,3) (3,4) (0,4) (5,7) (3,6) (7,8):"""))
arr = input().split()
s = []
f = []
for ar in arr:
    ar = ar[1:-1]
    start = int(ar.split(',')[0])
    end = int(ar.split(',')[1])
    s.append(start)
    f.append(end)

s, f = bubble_sort(s,f)
G = greedy_activity(s,f,n)

res = []
for t in range(len(G)):
    if G[t]:
        res.append('({},{})'.format(s[t],f[t]))

print(' '.join(res))

            
