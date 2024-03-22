import random
from itertools import permutations, combinations

# For PIN code
pin = input("Enter Your 4 Digit PIN: ")
if not pin.isdigit() or len(pin) != 4 or len(set(pin)) != 4:
    print("Invalid PIN code.")
    exit()

codes = list(permutations(range(10), 4))
random.shuffle(codes)

pinPosition = codes.index(tuple(map(int, pin))) + 1

if tuple(map(int, pin)) in codes:
    print("OPEN!", f"\nPosition [{pinPosition}] out of [{len(codes)}] Permutations.")
else:
    print("PIN DOES NOT EXIST.")

# For lucky numbers
luckyNumbers = list(combinations(range(45), 6))
random.shuffle(luckyNumbers)

print(f"TAYA-I NI: {random.choice(luckyNumbers)}")
