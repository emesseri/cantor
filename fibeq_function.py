def fib_seq():

    num_terms = input("Enter number of Fibonacci terms: ")
    valid = num_terms.isnumeric()
    print(num_terms)
    print(valid)
    if valid:
        seq = [0,1]
        for i in range(0, num_terms):
            seq.append(seq[-1] + seq[-2])
        seq.remove(seq[0])
        print(seq)
        return seq
    else:
        print("Invalid input. Input must be a numeric value.")


fib_seq()