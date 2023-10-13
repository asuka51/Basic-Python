#確認問題　問1(1)

import math

# 2次方程式の係数
a = 1
b = -6
c = 9

# 判別式を計算
discriminant = b**2 - 4*a*c

# 判別式が正の場合
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("2つの実数解があります:")
    print("x1 =", x1)
    print("x2 =", x2)

# 判別式がゼロの場合
elif discriminant == 0:
    x1 = -b / (2*a)
    print("重解があります:")
    print("x1 =", x1)

# 判別式が負の場合
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print("2つの複素数解があります:")
    print("x1 =", realPart, "+", imaginaryPart, "i")
    print("x2 =", realPart, "-", imaginaryPart, "i")

