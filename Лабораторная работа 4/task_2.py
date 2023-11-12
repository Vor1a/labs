import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        lines = [line for line in csv.DictReader(csv_file)]

    json_data = json.dumps(lines, indent=4)

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json_file.write(json_data)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")