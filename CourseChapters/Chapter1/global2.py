name = "Susan"
print(name)

def print_name():
    global name
    name = "John"
    print(name)

print_name()
print(name)