def number_pattern(n):
    num = []
    if not isinstance(n,int):
        return ('Argument must be an integer value.')
    elif n < 1:
        return ('Argument must be an integer greater than 0.')
    else:
        for number in range (1,n+1):
            num.append(str(number))
    return " ".join(num)
print(number_pattern(4))
