# 1
f1 = lambda x: x**2 if x % 2 == 0 else x**3
print(f1(3))

# 2
f2 = lambda a, b: a if a > b else b
print(f2(10, 7))

# 3
f3 = lambda s: s[::-1]
print(f3("python"))

# 4
f4 = lambda x: "musbat" if x > 0 else "manfiy" if x < 0 else "nol"
print(f4(-5))

# 5
f5 = lambda x: abs(x)
print(f5(-12))

# 6
f6 = lambda x: x % 10
print(f6(987))

# 7
f7 = lambda x: "juft" if x % 2 == 0 else "toq"
print(f7(9))

# 8
f8 = lambda a, b, c: max(a, b, c)
print(f8(4, 9, 2))

# 9
f9 = lambda s: s.isupper()
print(f9("HELLO"))

# 10
f10 = lambda x: 10 <= x <= 99
print(f10(45))
