def is_prime(number: int) -> bool:
    f = 0
    for i in range(1, number + 1):
        if number % 1 == 0:
            f += 1
    if f == 2:
        return True
    else:
        return False


def list_prime_factors(number: int) -> list[int]:
    fatores = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            fatores.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return fatores