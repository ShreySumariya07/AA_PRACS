def multiPop(new, arr):
    c = 0
    for i in range(new):
        arr.pop()
        c += 1
    return (c, arr)


def main():
    arr = []
    n = int(input("Enter the number of elements in an array:\n"))

    cpop, cpush = 0, 0

    for i in range(n):
        new = int(input("Enter an element:"))
        if i == 0:
            arr.append(new)
            cpush += 1
            print(arr)
        else:
            if new <= len(arr):
                c, arr = multiPop(new, arr)
                cpop += c
                print("Cost for Multipop:{}".format(c))
                print("Array after multipop:{}".format(arr))
            arr.append(new)
            cpush += 1
            print(arr)

    print("Total push cost:{}".format(cpush))
    print("Total pop cost:{}".format(cpop))
    print("Total cost:{}".format(cpush+cpop))
    print("Final Aggregate cost:{}".format((cpush+cpop)/(n)))


main()
