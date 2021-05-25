from timeit import Timer

def test1():#时间最长
    l = []
    for i in range(1000):
        l = l + [i]

def test2():#减少到前面的十几分之一
    l = []
    for i in range(1000):
        l.append(i)

def test3():#约为tes2时间半，test4的一倍
    l = [i for i in range(1000)]

def test4():#最省时间，约为test3的时间一半
    l = list(range(1000))

if __name__ == "__main__":
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000)," millseconds.")

    t2 = Timer("test2()","from __main__ import test2")
    print("append ",t2.timeit(number=1000)," millseconds.")

    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ", t3.timeit(number=1000)," millseconds.")

    t4 = Timer("test4()","from __main__ import test4")
    print("list range ",t4.timeit(number=1000)," millseconds.")

    """
concat  2.529250366  millseconds.
append  0.16544344300000002  millseconds.
comprehension  0.074596632  millseconds.
list range  0.03615529400000028  millseconds.
"""
               
