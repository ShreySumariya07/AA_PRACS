import random
from turtle import hideturtle


def main():
    n = int(input("Enter the number of candidates:"))
    candidate = []

    for i in range(n):
        candidate_number = i+1
        print("Candidate Number:", candidate_number)
        skill = int(input("Enter the skill:"))
        candidate.append((candidate_number, skill))

    salary = 1
    h_cost = 0
    cost = 1

    hired_candidate = candidate[0]
    print("Candidate\tInterview\tisHired\tHired\t cost")
    print(hired_candidate, "\t1\ty\t", h_cost, "\t", cost)

    for i in range(1, n):
        h_cost += 1
        cost += 1
        cand = candidate[i]
        if cand[1] > hired_candidate[1]:
            cost += h_cost*salary
            hired_candidate = cand
            print(cand, "\t1\ty\t", h_cost, "\t", cost)
            h_cost = 0
        else:
            print(cand, "\t0\tn\t0\t", cost)

    print("Best candidate is found at", hired_candidate[0])
    print("Total cost:", cost)

    h_cost = 0
    cost = 1

    hired_candidate = random.choice(candidate)
    candidate.pop(candidate.index(hired_candidate))
    print("Candidate\tInterview\tisHired\tHired\t cost")
    print(hired_candidate, "\t1\ty\t", h_cost, "\t", cost)
    for i in range(1, n):
        h_cost += 1
        cost += 1
        cand = random.choice(candidate)
        candidate.pop(candidate.index(cand))
        if cand[1] > hired_candidate[1]:
            cost += h_cost*salary
            hired_candidate = cand
            print(cand, "\t1\ty\t", h_cost, "\t", cost)
            h_cost = 0
        else:
            print(cand, "\t0\tn\t0\t", cost)

    print("Best Candidate is found at", hired_candidate[0])
    print("Total_cost:", cost)


main()
