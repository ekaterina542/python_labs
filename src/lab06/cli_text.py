
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        path = Path(args.input)

        with path.open("r", encoding="utf-8") as file:
            for number, line in enumerate(file, start=1):
                if args.n:
                    print(f"{number}: {line}", end="")
                else:
                    print(line, end="")

    elif args.command == "stats":
        path = Path(args.input)

        text = path.read_text(encoding="utf-8")

        text = normalize(text)
        tokens = tokenize(text)
        freq = count_freq(tokens)
        result = top_n(freq, args.top)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print(f"Топ-{args.top} слов:")

        for word, count in result:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
