# ----------быстрая сортировка----------
def qicksort(s):
    if len(s)> 1:
        pivot = s[0]
        left_part = [i for i in s if i<pivot]
        centre_part = [x for x in s if x == pivot]
        right_part = [x for x in s if x>pivot]
        s = qicksort(left_part) + centre_part + qicksort(right_part)
    return s
