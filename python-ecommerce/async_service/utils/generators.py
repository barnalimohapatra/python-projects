from typing import List, Iterator


def batch_generator(data: List, batch_size: int) -> Iterator[List]:
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]
