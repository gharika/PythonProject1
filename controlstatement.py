for i in range(0, 100, 7):
    print(i)

quote = "We Need To Be There In Time"
for i in quote:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(i, end='')
print("")


# lists
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11]

numbers = even + odd
numbers.sort()
numbers.append(12)
print(numbers)
print(sorted(numbers, reverse=True))

list_1 = []
list_2 = list()

print(list("There are hidden things"))

# lists are reference type
new_even = even
another_even = list(even)
new_even.sort(reverse=True)
print(even)
print(new_even)
print(another_even)

# iterator
val = "1234567890"
my_iterator = iter(val)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))

my_list = list(range(100))
print(my_list)

print(val.index('0'))
print(val[3:7])
