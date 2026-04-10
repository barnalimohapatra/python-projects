from contextlib import contextmanager, asynccontextmanager
import time


@contextmanager
def timed(name: str):
    start = time.time()
    try:
        yield
    finally:
        print(f"{name} took {time.time() - start:.3f}s")


@asynccontextmanager
async def async_timed(name: str):
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"{name} took {time.time() - start:.3f}s")
