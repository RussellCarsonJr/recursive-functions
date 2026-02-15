def mult_recur(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + mult_recur(a, b-1)

def fact_recur(n):
    if n == 0:  #  0! = 1 (mathematical definition)
        return 1
    elif n == 1:
        return 1
    elif n < 0:  #  Factorial undefined for negative numbers
        raise ValueError("Factorial is not defined for negative numbers")
    else:
        return mult_recur(n, fact_recur(n-1))

#  result = fact_recur(0)
#  result = fact_recur(1)
result = fact_recur(4)
#  result = fact_recur(-1)
print(result)
