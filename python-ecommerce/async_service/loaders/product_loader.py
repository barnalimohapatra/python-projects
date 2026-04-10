from async_service.utils.context import timed
from typing import List, Dict

'''
def load_products_from_csv(filepath: str) -> List[Dict]:
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_products() -> List[Dict]:
    import os
    dir_path = os.path.dirname(__file__)
    csv_path = os.path.join(dir_path, "../data/products.csv")
    return load_products_from_csv(csv_path)

'''

# Decorate  with @timeit to measure their execution time via the timeit decorator, which is a simpler way to measure
#  execution time without needing to use context managers explicitly. The timeit decorator will automatically
#  print the execution time of the decorated function when it is called.
'''
from async_service.utils.decorators import timeit 

@timeit
def load_products_from_csv(filepath: str) -> List[Dict]:
    import csv
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


@timeit
def load_products() -> List[Dict]:
    import os
    dir_path = os.path.dirname(__file__)
    csv_path = os.path.join(dir_path, "../data/products.csv")
    return load_products_from_csv(csv_path)
'''
# decorate with @timed to measure their execution time via the timed context manager, which provides a more flexible way to measure 
# execution time and can be used in various contexts, not just for function calls. The timed context manager will print the execution  
#  time of the code block it wraps when it is exited.
def load_products_from_csv(filepath: str) -> List[Dict]:
    from typing import List, Dict
    import csv

    with timed("load_products_from_csv"):
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)


def load_products() -> List[Dict]:
    from typing import List, Dict
    import os

    with timed("load_products"):
        dir_path = os.path.dirname(__file__)
        csv_path = os.path.join(dir_path, "../data/products.csv")
        return load_products_from_csv(csv_path)
