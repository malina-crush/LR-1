values = [3, 1, 3, 2, 1, 5, 2]
uniqe_values = set(values)
print(uniqe_values, len(uniqe_values))
other = {2, 4, 5}
print(uniqe_values & other)
print(uniqe_values | other)
print(uniqe_values - other)
print(other - uniqe_values)
