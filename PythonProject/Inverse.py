import random as r

n = 20
InputX = []
OutputF = []
OutputH = []

# Generate input list
for _ in range(n):
    num = r.randint(0, 10)
    InputX.append(num)

# Sort the input list
InputX.sort()

# Define functions f(x) and h(x)
def f(x):
    return 4 * (x ** 2) - 9

def h(x):
    return (2 * x - 3) / 4

# Compute f(x) and h(x) for each input
for numberX in InputX:
    OutputF.append(f(numberX))
    OutputH.append(h(numberX))

# Sort the output lists
OutputF.sort()
OutputH.sort()
for [val, h_val] in zip(OutputF, OutputH):
    add.append(val + h_val)
    subtract.append(val - h_val)
    multiply.append(val * h_val)
    # Divide by zero
    if h_val != 0:
        division.append(round((val / h_val), 2))
    else:
        division.append('Undefined')

# Compute composition of functions F o G and G o H
for x in OutputH:
    H.append(f(x))
for y in OutputF:
    F.append(h(y))

# Sort the remaining lists
add.sort()
subtract.sort()
multiply.sort()
division.sort()
H.sort()
F.sort()

# Capture inverse functions
inverse_f = [(OutputF[i], InputX[i]) for i in range(n)]
inverse_h = [(OutputH[i], InputX[i]) for i in range(n)]

# Print results
print(f'''
Input X: {InputX}
Output F: {OutputF}
Output H: {OutputH}
FH: {add}
F-H: {subtract}
FH: {multiply}
FH/: {division}
FoG: {F}
GoH: {H}
Inverse of f: {inverse_f}
Inverse of g: {inverse_h}''')
