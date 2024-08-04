import test2

print('hello world')
testData = ['q', 'w']
del testData[0]
print(testData)
print(type(testData))
print(type(testData[0]))

x = str(10)  # x will be '10'
y = int(10)  # y will be 10
z = float(10)  # z will be 10.0

print("x =", x)
print("y =", y)
print("z =", z)


def sum(x, y):
    sum = x + y
    return sum


print(sum(5, 10))

test2.SayHello("BigHui", 'Chlenov')