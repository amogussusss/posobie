if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = f.readlines()

    biggest = 0
    for i in a:
        if len(i) < biggest:
            biggest = len(i)

    for i in a:
        if len(i) == biggest:
            print(i)
