c=50
h=30

import math

x = []
y = [i for i in input('Give me a number: ').split('.')]
for d in y:
    x.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
print(','.join(x))
