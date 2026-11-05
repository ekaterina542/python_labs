import random

from .search import linear_search, binary_search
from .search import two_sum_brute, two_sum_fast
from .sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    """Проверяет сортировку на случайных списках."""
    checks = 0

    for _ in range(trials):
        nums = [
            random.randint(-100, 100)
            for _ in range(random.randint(0, 50))
        ]

        original = nums.copy()

        assert fn(nums) == sorted(nums)
        checks += 1

        assert nums == original
        checks += 1

    return checks


def check_search():
    """Проверяет линейный и бинарный поиск."""
    checks = 0

    for _ in range(100):
        nums = [
            random.randint(-100, 100)
            for _ in range(random.randint(0, 50))
        ]

        x = random.randint(-100, 100)

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        assert linear_search(nums, x) == expected
        checks += 1

        sorted_nums = sorted(nums)

        if sorted_nums:
            queries = [
                x,
                sorted_nums[0],
                sorted_nums[-1],
                sorted_nums[-1] + 1
            ]
        else:
            queries = [x, 0]

        for value in queries:
            result = binary_search(sorted_nums, value)

            if value in sorted_nums:
                assert 0 <= result < len(sorted_nums)
                checks += 1

                assert sorted_nums[result] == value
                checks += 1
            else:
                assert result == -1
                checks += 1

    return checks


def check_two_sum(trials=100):
    """Проверяет оба способа решения задачи Two Sum."""
    checks = 0

    for _ in range(trials):
        nums = [
            random.randint(-100, 100)
            for _ in range(random.randint(0, 50))
        ]

        if len(nums) >= 2 and random.random() < 0.5:
            i, j = random.sample(range(len(nums)), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-200, 200)

        brute_result = two_sum_brute(nums, target)
        fast_result = two_sum_fast(nums, target)

        assert (brute_result is None) == (fast_result is None)
        checks += 1

        if brute_result is not None:
            i, j = brute_result
            assert 0 <= i < j < len(nums)
            checks += 1

            assert nums[i] + nums[j] == target
            checks += 1

        if fast_result is not None:
            i, j = fast_result
            assert 0 <= i < j < len(nums)
            checks += 1

            assert nums[i] + nums[j] == target
            checks += 1

    return checks


def main():
    checks = 0

    checks += check_sorting(bubble_sort)
    checks += check_sorting(insertion_sort)
    checks += check_sorting(selection_sort)

    checks += check_search()
    checks += check_two_sum()

    print(f"OK: {checks} проверок")


if __name__ == "__main__":
    main()
