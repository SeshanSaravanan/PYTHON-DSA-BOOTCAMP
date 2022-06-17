nth_term = int(input("Enter the nth term of the Fibonacci Series: "))

# where n1 and n2 are first and second number respectively
n1 = 0
n2 = 1

print(n1)
print(n2)

for number in range(2, nth_term):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
