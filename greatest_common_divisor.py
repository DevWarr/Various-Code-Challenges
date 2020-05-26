from random import randint


def solution(m, f):

    if M == "0" or F == "0":
        # If either value is zero, it's impossible
        return "impossible"
    if M == "1" and F == "1":
        # if both values are 1, return 0
        return "0"

    # Grab integer values and set initial steps taken
    M = int(m)
    F = int(f)
    steps_taken = 0

    if M < F:
        # Swap values so the greater value is always M
        M, F = F, M

    while True:
        # Thank you Euclid for this algorithm to find the Greatest Common Divisor :pray:
        # Grab the remainder
        r = M % F
        if r == 0:
            # If our remainder is zero, we're at the end of our loop
            if F != 1:
                # If F isn't 1, then we didn't start with 1 bomb each. Impossible!
                steps_taken = "impossible"
            else:
                # If F IS one, example
                # M = 6, F = 1
                # [1, 1] -> [2, 1] -> [3, 1] -> [4, 1] -> [5, 1] -> [6, 1]
                #        ↑s1       ↑s2       ↑s3       ↑s4       ↑s5
                # 5 loops total, or 6 - 1
                steps_taken += M - 1
            break
        else:
            steps_taken += int(M/F)
            M = F
            F = r
    return str(steps_taken)


def create_tests(max_range):
    m = 1
    f = 1

    for i in range(0, max_range):
        which = randint(0, 100)
        if which > 0:
            f += m
        else:
            m += f
    return [str(m), str(f)]


c1 = create_tests(randint(40, 600))
c2 = create_tests(randint(40, 600))
c3 = create_tests(randint(40, 600))
c4 = create_tests(randint(40, 600))
c5 = create_tests(randint(40, 600))
c6 = create_tests(randint(40, 600))

print(c1, solution(*c1))
print(c2, solution(*c2))
print(c3, solution(*c3))
print(c4, solution(*c4))
print(c5, solution(*c5))
print(c6, solution(*c6))
