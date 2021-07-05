"""
背包问题动态规划法
核心：首先求出一张表，表示前面所有item组合对应的限制重量的value最大值，这个表行数值是len(item)+1,列数值是max_capacity+1。
最后这张表中，同一行中最后一列数值最大，同一列中最后一行数值最大。这样最后一行最后一列是表中最大值。
然后根据这张表，从最后一行最后一列开始往前推，如果它与上一行同一列的值不相同，则表示
这个item应该选进去，然后除去这个item的重量，找到上一行的列，依上办法进行对比
一直到第一个item为止。
"""

class Item:
    def __init__(self,NameTuple):
        self.name = NameTuple[0]
        self.weight = NameTuple[1]
        self.value = NameTuple[2]

def knapsack(items,max_capacity):
    table = [[0.0 for _ in range(max_capacity+1)] for _ in range(len(items)+1)]
    for i, item in enumerate(items):
        for capacity in range(1,max_capacity+1):
            previous_item_value = table[i][capacity]
            if capacity >= item.weight:
                value_freeing_weight_for_item = table[i][capacity-item.weight]
                table[i+1][capacity] = max(value_freeing_weight_for_item+item.weight,previous_item_value)
            else:
                table[i+1][capacity] = previous_item_value

    solution = []
    capacity = max_capacity
    for i in range(len(items),0,-1):
        if table[i-1][capacity] != table[i][capacity]:
            solution.append(items[i-1])
            capacity -= items[i-1].weight
    return solution

if  __name__ == "__main__":
    totalWeight = 0
    totalValue = 0
    max_capacity = 75
    items = [ Item(("television",50,500)),
              Item(("candlesticks",2,300)),
              Item(("stereo",35,400)),
              Item(("laptop",3,1000)),
              Item(("food",15,50)),
              Item(("clothing",20,800)),
              Item(("jewelry",1,4000)),
              Item(("books",100,300)),
              Item(("printer",18,30)),
              Item(("refrigerator",200,700)),
              Item(("painting",10,1000))]
    solution = knapsack(items,max_capacity)
    
    print()
    print("Name         Weight     Value")
    for s in solution:
        print("%-12s    %-6d   %-6d"%(s.name,s.weight,s.value))
        totalWeight += s.weight
        totalValue += s.value
    print()
    print("TOTALWEIGHT:%s  TOTALVALUE:%s"%(totalWeight,totalValue))
    
              

    
             
