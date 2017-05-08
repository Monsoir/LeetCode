FIRSTROW = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
SECONDROW = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
THIRDROW = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    results = []
    for word in words:
        if allInRow(FIRSTROW, word) or allInRow(SECONDROW, word) or allInRow(THIRDROW, word):
            results.append(word)

    return results

def allInRow(row, word):
    for letter in word.lower():
        if letter in row:
            continue
        else:
            return False

    return True

if __name__ == '__main__':
    TEST = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(TEST))