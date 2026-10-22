from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл и возвращает его содержимое одной строкой.

    Если файл не найден, возникает FileNotFoundError.
    Если кодировка не подходит, возникает UnicodeDecodeError.
    Для другой кодировки можно передать параметр encoding,
    например encoding="cp1251".
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

