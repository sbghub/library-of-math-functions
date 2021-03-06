from functools import reduce


def choose(total, choosing):
    if not is_integer(total) or not is_integer(choosing) or total <= 0 or choosing <= 0:
        return "please enter positive integers"

    return factorial(total) / (factorial(choosing) * factorial(total - choosing))


def circular_prime(number):
    if not is_prime(number):
        return False

    permutations = len(str(number)) - 1
    if permutations == 0:
        return True

    for i in range(1, permutations + 1):
        last_digit = number % 10
        rest_of_num = int(number / 10)
        number = (last_digit * 10 ** permutations) + rest_of_num
        if not is_prime(number):
            return False

    return True


def collatz_sequence(number):
    error_message = "please enter a positive integer"
    if is_integer(number):
        number = int(number)
        if number < 1:
            return error_message
    else:
        return error_message

    result = [number]
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            result.append(number)
        else:
            number = 3 * number + 1
            result.append(number)
    return result


def consecutive_prime_sum(number):
    incr = 1
    orig_incr, orig_num = incr, number
    prime = nth_prime(incr)
    while nth_prime(orig_incr) < (number / 2):
        tally = 0
        while number > prime:
            number -= prime
            incr += 1
            prime = nth_prime(incr)
            tally += 1
        if number == prime:
            return tally + 1
        else:
            orig_incr += 1
            incr = orig_incr
            prime = nth_prime(incr)
            number = orig_num
    return False


def digit_sum(number):
    if is_integer(number):
        number = int(number)
        if number < 0:
            number *= -1
    else:
        return "Please enter an integer."

    return sum(int(digit) for digit in list(str(number)))


def distinct_prime_factors(number):
    return list(filter(lambda x: is_prime(x), factor_list(number)))


def factorial(number):
    error_message = "Please enter a non-negative integer"
    try:
        check = float(number)
        number = int(number)
    except:
        return error_message

    if check != number or number < 0:
        return error_message

    return 1 if number == 0 else number * factorial(number - 1)


def factor_list(number):
    error_message = "Please enter a positive integer"
    if is_integer(number):
        number = int(number)
        if number < 0:
            return error_message
    else:
        return error_message

    result = set()
    root = int(number ** .5)

    for divisor in range(1, root + 1):
        if number % divisor == 0:
            result.add(divisor)
            result.add(int(number / divisor))

    result = list(result)
    result.sort()
    return result


def fibonacci(index):
    error_message = 'Please enter a positive integer'
    if is_integer(index):
        index = int(index)
        if index < 0:
            return error_message
    else:
        return error_message

    num_1, num_2 = 0, 1
    while index > 0:
        num_1, num_2 = num_2, num_1 + num_2
        index -= 1

    return num_1


def goldbach_pair(number):
    error_message = "please enter an odd composite number"
    if not is_integer(number) or number % 2 == 0 or is_prime(number):
        return error_message
    else:
        number = int(number)

    max_root = int((number / 2) ** .5)
    for i in range(1, max_root + 1):
        second = 2 * i ** 2
        first = number - second
        if is_prime(first):
            return first, second

    return False


def is_integer(number):
    try:
        adj_number = int(float(number))
        return float(number) == adj_number
    except:
        return False


def is_prime(number):
    error_message = 'Please enter a positive integer greater than 1'

    if not is_integer(number) or number < 0:
        return error_message
    elif number < 3:
        return number == 2
    elif number % 2 == 0:
        return False
    else:
        root = number**.5
        divisor = 3
        while divisor <= root:
            if number % divisor == 0:
                return False
            divisor += 2
        return True


def largest_prime_factor(number):
    error_message = 'Please enter a non-prime integer greater than 1'
    if not is_integer(number) or number <= 1 or is_prime(number):
        return error_message

    divisor = int(number**.5)
    while divisor > 1:
        if number % divisor == 0:
            factor_1, factor_2 = divisor, number / divisor
            if is_prime(factor_2):
                return factor_2
            elif is_prime(factor_1):
                return factor_1
        divisor -= 1
    return 2


def least_common_multiple(factors):
    error_message = "Please return a list of numbers"
    if not isinstance(factors, list):
        return error_message
    if any(not is_integer(factor) for factor in factors):
        return error_message

    factors.sort()
    for index, factor in enumerate(factors):
        for subindex, future_factor in enumerate(factors[index + 1:]):
            if future_factor % factor == 0:
                factors[index + subindex + 1] = int(future_factor / factor)

    return reduce((lambda x, y: x * y), factors)


def lexicographic_permutation(base, index):
    base = str(base)
    if index == 1:
        return base
    if len(base) == 2:
        if index == 2:
            return base[1] + base[0]

    perms_per_substr = factorial(len(base) - 1)

    letter_index = 0
    while index > perms_per_substr:
        index -= perms_per_substr
        letter_index += 1

    base = list(base)
    first_letter = base.pop(letter_index)
    adj_base = reduce((lambda x, y: x + y), base)
    return first_letter + lexicographic_permutation(adj_base, index)


def multiple_of(number, factor_list):
    error_message = 'Please enter an integer and a list of factors'
    if not is_integer(number):
        return error_message

    if isinstance(factor_list, int):
        factor_list = [factor_list]

    return any(number % factor == 0 for factor in factor_list)


def nth_prime(index):
    error_message = 'Please enter an integer greater than 1'
    if not is_integer(index) or index < 1:
        return error_message

    if index == 1:
        return 2

    base = 1
    while index > 1:
        base += 2
        if is_prime(base):
            index -= 1

    return base


def palindrome(text):
    text = str(text)
    length = len(text)

    for index in range(int(length / 2)):
        if text[index] != text[-(index + 1)]:
            return False

    return True


def triangular_number(index):
    error_message = "Please enter a positive integer greater than 0"
    if not is_integer(index) or index < 1:
        return error_message

    return sum(range(index + 1))


def truncatable_prime(number):
    if not is_prime(number) or number < 10:
        return False
    else:
        left, right = number, number

        while left >= 10:
            left = int(left / 10)
            if not is_prime(left):
                return False

        while right >= 10:
            right = int(str(right)[1:])
            if not is_prime(right):
                return False

    return True
