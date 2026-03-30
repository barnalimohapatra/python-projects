import csv
from typing import List, Dict


def load_products_from_csv(filepath: str) -> List[Dict]:
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_products() -> List[Dict]:
    import os
    dir_path = os.path.dirname(__file__)
    csv_path = os.path.join(dir_path, "../data/products.csv")
    return load_products_from_csv(csv_path)

