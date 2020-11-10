# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 让x变化确定y， z
    count = 1
    x, y, z = 1, 1, 1

    print("\t\t\t Men, Women, Children")
    print("........................................")

    while x <= 9:
        y = 20 - 2 * x  # 根据x求y
        z = 30 - x - y  # 根据x, y 求z

        if 3 * x + 2 * y + z == 50:
            print(f"solution 1: {x:-4d} {y:-4d} {z:-8d}")

        x += 1

    n = 1

    while not (n % 2 == 1 and n % 3 == 2
               and n % 5 == 4 and n % 6 == 5
               and n % 7 == 0):
        n += 1

    print("Count the stairs: ", n)

    n = 7

    while not (n % 2 == 1 and n % 3 == 2
               and n % 5 == 4 and n % 6 == 5
               and n % 7 == 0):
        n += 7

    print("Count the stairs: ", n)



