def is_prime_dec(func):
    def wrapper(a, b, c):
        dec_res = func(a, b, c)
        for i in range(2, dec_res):
            if dec_res % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return dec_res
    return wrapper

@is_prime_dec
def sum_three(a, b, c):
    return a + b + c

res = sum_three(2, 4, 6)
print(res)
