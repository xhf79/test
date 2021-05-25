from timeit import Timer
import random

print(" Num.       lst_time     d_time") 
for i in range(10000, 200001,20000):
    t = Timer("random.randrange(%d) in x"%i,
              "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f"%(i,lst_time,d_time))
