# class MyIterator:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.count = 0

class MyList:
    def __init__(self, lst):
        self.iterable = lst
        self.count = 0

    def __iter__(self):
        return self

    def func(self, n):
        return n // 2

    def __next__(self):
        if self.count < len(self.iterable):
            self.count += 1
            return self.iterable[self.count - 1]
        raise StopIteration

l = MyList([6, 7, 10, 1001, 945, 653])
print(type(l))

print(list(l))
for i in l:
    print(i)


















# class DoubleElementListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#
#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2], self.lst[self.i - 1]
#         else:
#             raise StopIteration
#
# class MyList(list):
#     def __iter__(self):
#         return DoubleElementListIterator(self)
#
# for x in MyList([1, 2, 3, 4]):
#     print(x)

# class multifilter:
#     def judge_half(pos, neg):
#         return x % 2 == 0# допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#
#     def judge_any(pos, neg):
#         return x % 3 == 0# допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#
#     def judge_all(pos, neg):
#         return x % 5 == 0# допускает элемент, если его допускают все функции (neg == 0)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#         # iterable - исходная последовательность
#         # funcs - допускающие функции
#         # judge - решающая функция
#
#     def __iter__(self):
#         pos, neg = 0, 0
#         a = [i for i in range(self.iterable)]
#         return self
#
#         # возвращает итератор по результирующей последовательности
#
# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))