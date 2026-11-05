import random
import time
from pathlib import Path

from .search import (linear_search, binary_search, two_sum_brute, two_sum_fast)
from .sorting import (bubble_sort, insertion_sort, selection_sort)
from src.lab04.io_txt_csv import write_csv


def measure_time(fn, *args):
    """Измеряет время выполнения функции в секундах."""
    start = time.perf_counter()
    result = fn(*args)
    elapsed = time.perf_counter() - start

    return result, elapsed


def print_table(rows):
    """Выводит результаты в виде таблицы."""
    widths = [max(len(str(row[i])) for row in rows) for i in range(3)]

    for row in rows:
        print(
            f"{str(row[0]):<{widths[0]}} | "
            f"{str(row[1]):<{widths[1]}} | "
            f"{str(row[2]):>{widths[2]}}"
        )


def run_benchmarks():
    """Запускает измерения времени работы алгоритмов."""
    random.seed(42)

    results = [
        ["Алгоритм", "Размер", "Время (сек)"]
    ]

    # Сортировки
    sorting_functions = [bubble_sort, insertion_sort, selection_sort]

    for n in [1000, 10000, 100000]:
        nums = [
            random.randint(-100000, 100000)
            for _ in range(n)
        ]

        for fn in sorting_functions:
            if n == 100000 and fn != bubble_sort and fn != insertion_sort:
                continue

            if n == 100000:
                results.append([fn.__name__, n, "> 60"])
                continue

            _, elapsed = measure_time(fn, nums)
            results.append([fn.__name__, n, f"{elapsed:.6f}"])

    # Поиск
    nums = [
        random.randint(-100000, 100000)
        for _ in range(100000)
    ]

    queries = [
        random.choice(nums)
        for _ in range(10000)
    ]

    _, linear_time = measure_time(
        lambda: [linear_search(nums, x) for x in queries]
    )

    results.append(["linear_search", 10000, f"{linear_time:.6f}"])

    sorted_nums, sort_time = measure_time(sorted, nums)

    results.append(["sort for binary", 100000, f"{sort_time:.6f}"])

    _, binary_time = measure_time(
        lambda: [binary_search(sorted_nums, x) for x in queries]
    )

    results.append(["binary_search", 10000, f"{binary_time:.6f}"])

    # Two Sum
    for n in [1000, 10000]:
        nums = list(range(n))
        target = nums[-1] + nums[-2]

        _, brute_time = measure_time(two_sum_brute, nums, target)
        _, fast_time = measure_time(two_sum_fast, nums, target)

        results.append(["two_sum_brute", n, f"{brute_time:.6f}"])
        results.append(["two_sum_fast", n, f"{fast_time:.6f}"])

    # Вывод таблицы
    print_table(results)

    # Сохранение в CSV
    output_path = Path("data/lab07/bench.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    write_csv(results, output_path)

    print(f"\nРезультаты сохранены в {output_path}")


if __name__ == "__main__":
    run_benchmarks()
