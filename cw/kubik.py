# +1$ (1, 2) - 33%
# -1$ (3, 4, 5, 6) - 67%

# +3$ (1, 2) - 33%
# -1$ (3, 4, 5, 6) - 67%

# +3$ * 33% = 0,99$
# -1$ * 67% = -0,67$

# 0,99$ + -0,67$ = 0,32$ - математическое ожидание


# +1$ (1, 2) - 33%
# -3$ (3, 4, 5, 6) - 67%

# 0,33 + -2 = -1,67$


import random

cube = [1, 2, 3, 4, 5, 6]
count_repeat = 1000
balance = 0

for _ in range(count_repeat):
    random_side = random.choice(cube)
    
    if random_side in [3, 5]:
        balance += 2
    elif random_side in [1, 6]:
        balance -= 1


print(f"Ваш баланс равен {balance}$")

