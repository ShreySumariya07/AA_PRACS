def multiPop(new, stack):
    c = 0
    for i in range(new):
        stack.pop()
        c += 1
    return (c, stack)


def main():
    stack = []
    n = int(input("Enter a number:"))
    balance = 0
    account_cost = 3
    cost = 0

    for i in range(n):
        balance += account_cost

        newElement = int(input("\nEnter a valid number:"))

        if i == 0:
            stack.append(newElement)
            cost += 1
            balance -= 1
            print("Stack:", stack)
            print("Real cost:", cost)
            print("Assumed cost:", account_cost)
            print("Balance:", balance)
        else:
            c = 0
            if newElement <= len(stack):
                c, arr = multiPop(newElement, stack)
                cost += c
                balance -= c
                print("Stack after multiPop", arr)
            stack.append(newElement)
            balance -= 1
            cost += 1
            print("Stack:", stack)
            print("Real cost:", c+1)
            print("Assumed cost:", account_cost)
            print("Balance", balance)

    print("Total cost:", cost)
    print("Total assumed cost", n*account_cost)
    print("Balance:", balance)


main()
