def mult_recur(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + mult_recur(a, b-1)

def power_recur(n, p):
    if p == 1:
        return n
    elif p == 0:
        return 1
    elif p == -1:  #  Base case for -1
        return 1 / n
    elif p < 0:  #  Recursive case for other negatives
        return 1 / mult_recur(n, power_recur(n, -(p+1)))
    else:
        return mult_recur(n, power_recur(n, p-1))

#  result = power_recur(2, -2)
#  print(result)