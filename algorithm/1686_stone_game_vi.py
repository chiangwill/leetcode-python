def stoneGameVI(aliceValues: list[int], bobValues: list[int]) -> int:

    # zip 之後排序，合併分數越大的越前面（依照最佳策略）
    tuple_list = sorted(zip(aliceValues, bobValues), key=lambda x: -sum(x))

    # 輪流得分
    a = sum([tuple_element[0] for tuple_element in tuple_list[0::2]])
    b = sum([tuple_element[1] for tuple_element in tuple_list[1::2]])

    return (a >= b) - (a <= b)


print(stoneGameVI([1, 3], [2, 1]))
print(stoneGameVI([1, 2], [3, 1]))
print(stoneGameVI([2, 4, 3], [1, 6, 7]))
