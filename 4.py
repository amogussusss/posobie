if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as a:
        f = a.readlines()

    biggest = 0
    for i in f:
        if len(i) > biggest:
            biggest = len(i)

    for i in range(1, biggest + 1):
        for j in f:
            if len(j) == i:
                print(j)
