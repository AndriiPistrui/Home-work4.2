def sum_even_index_multiply_last(lst):
    if not lst:
        return 0

    sum_even_index = sum(lst[i] for i in range(0, len(lst), 2))

    return sum_even_index * lst[-1]


print(sum_even_index_multiply_last([0, 1, 7, 2, 4, 8]))  # (0 + 7 + 4) * 8 = 88
print(sum_even_index_multiply_last([1, 3, 5]))  # (1 + 5) * 5 = 30
print(sum_even_index_multiply_last([6]))  # 6 * 6 = 36
print(sum_even_index_multiply_last([]))  # 0

