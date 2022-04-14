if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = f.readlines()

    for i in range(len(a)):
        for j in range(len(a[i]):
            if j != len(a[i]) - 1:
                if a[i][j] == a[i][j+1]:
                    print(a[i])
                    break
