if __name__ == "__main__":
    a = list(map(int, input().split())

    b = a.copy()
    b.sort()

    if a == b:
        print(True)
    else:
        print(False)
