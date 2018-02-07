# https://projecteuler.net/problem=5

largest_pal = 0


for i in range(1000):
    for j in range(1000):
        mul = i * j
        str_mul = str(mul)
        if str_mul == str_mul[::-1]:
            if mul > largest_pal:
                largest_pal = mul


print(largest_pal)



