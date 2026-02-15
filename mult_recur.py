def mult_recur(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + mult_recur(a, b-1)

result = mult_recur(4, 8)
print(result)