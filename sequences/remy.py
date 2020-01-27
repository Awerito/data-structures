def a(n):
    r = 0
    for i in range(1, n):
        if n & i:
            r += 1
    return r

if __name__=="__main__":
    total = 100
    for i in range(1, total + 1):
        print(a(i))
