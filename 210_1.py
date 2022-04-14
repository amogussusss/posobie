if __name__ == "__main__":
    a = list()
    for _ in range(10):
        a.append(int(input()))

    negative_count = 0
    positive_sum = 0
    for i in a:
        if i < 0:
            negative_count += 1
        if i > 0:
            positive_sum += i

    print("positive sum =", positive_sum)
    print("negative count =", negative_count)
