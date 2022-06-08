
def multiPop(new_element, stack, multipop_cost):
    c = 0
    for i in range(new_element):
        stack.pop()
        c += multipop_cost
    return (c, stack)


def main():
    stack = []
    n = int(input("Enter the number of elements:"))
    push_cost = 2
    pop_cost = 0
    multipop_cost = 0

    potential_cost = 0

    for i in range(n):
        new_element = int(input("\nEnter the new element:"))

        if i == 0:
            stack.append(new_element)
            potential_cost += push_cost
            print("Stack:", stack)
        else:
            c = 0
            if new_element <= len(stack):
                c, arr = multiPop(new_element, stack, multipop_cost)
                potential_cost += c
                print("Stack after multipop:", stack)
            stack.append(new_element)
            potential_cost += push_cost
            print("Stack:", stack)
    print("Total cost:", potential_cost)


main()
