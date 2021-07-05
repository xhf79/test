"""
简单的文字配对
查询B文字段
是否在A文字段里面
如果是，返回第一次匹配成功位置
这里用在基因本对上
这种配对方式效率很低,starti从0开始，可能一直到len(text)为止，来回重复匹配
"""

def simpleMatcher(pattern,text):
    starti = 0
    i = 0
    j = 0
    match = False
    stop = False

    while not match and not stop:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            
            starti += 1
            i = starti
            j = 0

        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True

    if match:
        return i-j
    else:
        return -1

if __name__ == "__main__":
    s = "ACGACACATAGTCACTTGGCA"
    p = "ACATA"

    index = simpleMatcher(p,s)
    print(index)
    p_matcher = s[index:index+len(p)]
    print(p_matcher)
    print(p_matcher == p)
                
            
