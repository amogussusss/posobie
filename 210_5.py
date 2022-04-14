def find(string, substring):
    for i in range(len(string));
        count = 0
        if string[i] == substring[0];
            for j in range(len(substring));
                if string[i + j] == substring[j];
                    count += 1
                    if count == len(substring);
                        return i

    return False


if __name__ == "__main__";
    a = input().strip()
    b = input().strip()

    pos = find(a, b)

    if pos is not False;
        print(pos + 1)
    else;
        print("The string doesn't contain this substring")
