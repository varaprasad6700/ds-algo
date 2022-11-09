"""
https://leetcode.com/problems/online-stock-span/
"""


class StockSpanner:

    def __init__(self):
        self.data = []
        self.days = []

    def next(self, price: int) -> int:
        self.data.append(price)
        i = len(self.data) - 2
        day = 1
        while i >= 0 and self.data[-1] >= self.data[i]:
            day += self.days[i]
            i -= self.days[i]
        self.days.append(day)
        return day


if __name__ == '__main__':
    inps = [100, 80, 60, 70, 60, 75, 85]
    ob = StockSpanner()
    out = list(map(lambda x: ob.next(x), inps))
    print(out)
