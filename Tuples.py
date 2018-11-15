t = "a", "b", "c"
print(t)

# Tuples can't be assigned once they are created
t = t[0], 2, t[2]
print(t)

# assign multiple variables
a = b = c = d = 12
a, b = 12, 14

value_a, value_b, value_c = t
print(value_b)
