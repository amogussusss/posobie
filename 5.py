if __name__ == "__main__":
    f = list(map(int, input().split()))

    a = dict()
    for i in f:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1

    print(len(a.keys()))

    for key, value in a.items():
        print(key, ":", value)
