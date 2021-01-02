def slices(series, length):
    if length > len(series):
        raise ValueError("Your substring is too large")
    return [series[i : i + length] for i in range(0, len(series) - length + 1)]








