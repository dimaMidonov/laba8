import time

def measure_time(func):
    def wrapper(a, b):
        print("Function started at", time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Sides:", a, b)
        start = time.perf_counter()
        result = func(a, b)
        end = time.perf_counter()
        print("Result:", result)
        print("Elapsed time:", end - start, "seconds")
        return result
    return wrapper

@measure_time
def calculate_hypotenuse(a, b):
    c = (a**2 + b**2) ** 0.5
    return c

a = float(input("Enter the length of the first cathetus:"))
b = float(input("Enter the length of the second cathetus:"))
c = calculate_hypotenuse(a, b)

print("The length of the hypotenuse is", c)
