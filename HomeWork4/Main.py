from math import sqrt


def correlation(num_1, num_2):
    n = len(num_1)

    mean_1 = sum(num_1) / n
    mean_2 = sum(num_2) / n

    covariance = sum((num_1[i] - mean_1) * (num_2[i] - mean_2) for i in range(n))
    variance_num_1 = sum((x - mean_1) ** 2 for x in num_1)
    variance_num_2 = sum((y - mean_2) ** 2 for y in num_2)

    correlation = covariance / (sqrt(variance_num_1) * sqrt(variance_num_2))

    return round(correlation)

num_1 = [1, 2, 3]
num_2 = [3, 2, 1]

correlation = correlation(num_1, num_2)
print(f"Корреляция Пирсона: {correlation}")