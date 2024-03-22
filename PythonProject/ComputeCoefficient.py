import math

def compute_coefficients(binomial):
    degree = int(binomial.split('^')[1])
    coefficients = []
    for k in range(degree + 1):
        coefficient = math.comb(degree, k)
        coefficients.append(coefficient)
    return coefficients

while True:
    input_str = input("Enter Binomal/s separated by comma (q to quit): ")
    if input_str.lower() == 'q':
        break

    binomials = input_str.split(',')

    for binomial in binomials:
        binomial = binomial.strip()  # Remove leading/trailing spaces
        coefficients = compute_coefficients(binomial)
        print(f"Coefficients for {binomial}: {coefficients}")