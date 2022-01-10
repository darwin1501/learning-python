

# difference between is and ==
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
# b = a             # Point b at what a is pointing to
# print(b is a)            # => True, a and b refer to the same object
# print(b == a)            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
print(b is a )           # => False, a and b do not refer to the same object
print(b == a)

