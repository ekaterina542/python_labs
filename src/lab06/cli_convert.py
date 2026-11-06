import argparse
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()
    
    if not Path(args.input).exists():
        raise FileNotFoundError(f"Файл {args.input} не найден")

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
        print("JSON успешно преобразован в CSV")

    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
        print("CSV успешно преобразован в JSON")

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print("CSV успешно преобразован в XLSX")


if __name__ == "__main__":
    main()
