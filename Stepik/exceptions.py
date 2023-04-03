class multifilter:
    def judge_half(pos, neg):
        return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.pos = 0
        self.neg = 0
        if self.count < len(self.iterable):
            self.count += 1
            for i in self.funcs:
                if i(self.iterable[self.count - 1]):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos, self.neg):
                return self.iterable[self.count - 1]
            else:
                return self.__next__()
        raise StopIteration

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0



a = [i for i in range(31)] # [0, 1, 2, ... , 30]



print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]