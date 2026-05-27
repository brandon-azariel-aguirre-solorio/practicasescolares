def square_root_bisection(number, tolerance=1e-7, maximun_interaction=100):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)
    iterations = 0

    while iterations < maximun_interaction:
        midpoint = (low + high) / 2
        square = midpoint ** 2

        if (high - low) < tolerance:
            print(f"The square root of {number} is approximately {midpoint}")
            return midpoint

        if square < number:
            low = midpoint
        else:
            high = midpoint

        iterations += 1

    print(f"Failed to converge within {maximun_interaction} iterations")
    return None

print( square_root_bisection(0.001, 1e-7, 50))
