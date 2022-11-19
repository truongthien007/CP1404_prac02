length = 10
name = input("Enter a name with at least 10 characters: ")
while len(name) < length:
    print("invalid name")
    name = input("Enter a name with at least 10 characters: ")
for i in range(len(name)):
    print("*" * len(name), end=" ")
