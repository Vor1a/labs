# TODO решите задачу
import json


def task() -> float:
    file_path = "input.json"
    with open(file_path) as f:
        data = json.load(f)
    sum_of_products = 0.0
    for item in data:
        score = item['score']
        weight = item['weight']
        product = score * weight
        sum_of_products += product

    return round(sum_of_products, 3)


print(task())
