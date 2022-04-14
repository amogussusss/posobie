if __name__ == "__main__":
    a = list(map(int, input().split()))

    for i. e in enumerate(a):
        mn = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[mn] = a[mn], e

    print(a)
