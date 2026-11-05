def bubble_sort(nums):
    """Сортирует список пузырьковым методом и возвращает новый список."""
    result = nums.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


def insertion_sort(nums):
    """Сортирует список методом вставок и возвращает новый список."""
    result = nums.copy()

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


def selection_sort(nums):
    """Сортирует список методом выбора и возвращает новый список."""
    result = nums.copy()
    n = len(result)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result
