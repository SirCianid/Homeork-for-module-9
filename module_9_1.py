def apply_all_func(int_list, *functions):
    results = dict()
    for res in functions:
        results[res.__name__] = res(int_list)
    return results


print(apply_all_func([1, 39, 5, 73], max, min))
print(apply_all_func([1, 39, 5, 73], len, sum, sorted))
