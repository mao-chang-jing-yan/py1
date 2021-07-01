import copy


def findLongestWord(s, dictionary):
    dict1 = {}
    for i in range(len(s)):
        dict1[i] = {"item": s[i], "next": i}

    for m in dictionary:
        for index in dict1.keys():
            for i in range(len(s) + 1):
                if s[index:i] in m and i > dict1[index]["next"]:
                    dict1[index]["item"] = s[index:i]
                    dict1[index]["next"] = i

    maxl = 0
    maxs = ""
    for m in dict1.keys():
        if maxl < len(dict1[m]["item"]) and dict1[m]["next"] - m > 0:
            maxl = len(dict1[m]["item"])
            maxs = dict1[m]["item"]
    print(maxl, maxs)


findLongestWord("idhoaidjforuw9jgf9rfjsodfjdlsfjsekjflwe9gur9wugfr98ug8rtgjrghju", [
    "r",
    "er",
    "r",
    "er",
    "er",
    "grwggugh9gyer98gyer08ger",
    "e8fu0we8u80rug8re",
    "efwe8ugw8eut",
    "ereur8weur0ew8r"])
