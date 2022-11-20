import random
import numpy as np
x = np.zeros(10)
y = 0
z = 1
c = 0
a = 0
while c < 10:
    n = random.randrange(100,999)
    x[c] = n
    if (x[y:z:]) % 3 == 0:
        print(f"{x[y:z:]} está no índice {a} e é divisível por 3")
        y += 1; z += 1; c += 1; a += 1
    else:
        y += 1; z += 1; c += 1; a += 1
print(x)
