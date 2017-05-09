def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return solution2(n)

def solution1(n):
    results = []
    for i in range(1, n+1):
        flag = 0
        if i % 3 == 0:
            flag += 3
        if i % 5 == 0:
            flag += 5
        
        results.append(representation(i, flag))
    
    return results

def representation(n, flag):
    switcher = {
        3: 'Fizz',
        5: 'Buzz',
        8: 'FizzBuzz',
    }

    return switcher.get(flag, str(n))

def solution2(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

if __name__ == '__main__':
    TEST = 15
    print(fizzBuzz(TEST))