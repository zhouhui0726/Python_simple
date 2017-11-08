#!/usr/bin/python3

def FuncX(x):
    def FuncY(y):
        return x * y
    return FuncY

tempFunc = FuncX(3)
result = tempFunc(5)
print(result)  # 15

result = FuncX(3)(5)
print(result)  # 15
