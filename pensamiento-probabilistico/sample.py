def find_it(seq):
    counter = [{x: seq.count(x)} for x in set(seq)]
    for n in counter:
        for i, j in n.items():
            if j % 2 != 0:
                return i


if __name__ == "__main__":
    test_list = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
    # print(find_it(test_list))
