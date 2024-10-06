

x = 100
def func():
    global x 
    print(x)
    x += 1

    return [10, x]


func()
func()
print(f"glob: {func()}")
a, b = func()

print('_____')
print(a, '-- ', b)