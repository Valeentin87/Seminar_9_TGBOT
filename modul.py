# ----------быстрая сортировка----------
def qicksort(s):
    if len(s)> 1:
        pivot = s[0]
        left_part = [i for i in s if i<pivot]
        centre_part = [x for x in s if x == pivot]
        right_part = [x for x in s if x>pivot]
        s = qicksort(left_part) + centre_part + qicksort(right_part)
    return s

# ------------------преобразование десятичного в двоичное----------------------


def decimal_binary(number):
    remains = 0
    whole = 0
    binary = ''
    while number // 2 != 0:
        remains = number % 2
        binary = binary + str(remains)
        number = number // 2

    result_binary = str(number)
    j = 0
    for i in range(len(binary)):
        result_binary = result_binary + binary[j-1]
        j = j-1
    return result_binary

