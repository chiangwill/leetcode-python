def mostWordsFound(sentences: list[str]) -> int:

    return max([len(element.split()) for element in sentences])


print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))
