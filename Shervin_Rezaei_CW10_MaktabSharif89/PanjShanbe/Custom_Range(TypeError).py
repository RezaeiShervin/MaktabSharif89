class CustomRange:

    def __init__(self, end: int, start=0, step=1) -> None:
        # if start < end
        self.start = start
        self.end = end
        self.step = step
        if start > end:
            self.start, self.end = self.end, self.start

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += self.step
        return self.start - self.step

    def __iter__(self):
        return self


numbers_obj = CustomRange(2, 36, 3)
print(numbers_obj)
numbers_iter = iter(numbers_obj)
print(next(numbers_iter))
print(*numbers_iter, sep=", ")
# print(range(2, 36, 3))
