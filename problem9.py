'''
Project Euler:
Problem #9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Date: May 7, 2019
'''

a, b, c, m = 1, 1, 1, 2
while (1000 % (a+b+c)) != 0:
    for n in range(1, m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        print(str(a+b+c))
        if 1000 % (a+b+c) == 0:
            print(a*b*c*25*25*25)
            break
    m += 1
print(a*b*c)

25*(15+8+17)
1000/40
375
200
425
200*375*425

1000/180

genPrimitiveTriples(50)
