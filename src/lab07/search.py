def linear_search(nums, x):
    """Возвращает индекс первого вхождения x или -1, если элемента нет."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """
    Выполняет бинарный поиск элемента x.

    Возвращает индекс любого вхождения x или -1, если элемента нет.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums, target):
    """Находит пару индексов i < j, сумма элементов которых равна target."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None


def two_sum_fast(nums, target):
    """Находит пару индексов i < j за один проход с помощью словаря."""
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return (seen[needed], i)

        seen[nums[i]] = i

    return None
