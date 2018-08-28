import numpy as np
# print(np.sqrt(38912))

x = np.arange(252)
y = np.arange(152)

for x_ in x:
    for y_ in y:
        if x_ * y_ == 38912:
            print(x_)
print('fda;')