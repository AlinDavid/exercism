def multiply(sub_list):
    result = 1
    for i in sub_list:
        result *= i

    return result


def largest_product(series, size):
    series_list = [int(i) for i in series]
    current_result = multiply(series_list[:size])
    last_result = 1
    for i in range(len(series_list) - size + 1):
        best_result = max(current_result, multiply(series_list[i:i+size]))
        last_result = max(last_result, best_result)

    return last_result



