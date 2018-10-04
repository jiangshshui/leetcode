# class StockSpanner:
#     def __init__(self):
#         self.stock_price=[]
#         self.span=[]
#
#     def next(self, price):
#         """
#         :type price: int
#         :rtype: int
#         """
#         if len(self.stock_price)==0 or price<self.stock_price[-1]:
#             self.span.append(1)
#             self.stock_price.append(price)
#
#         else:
#             j=len(self.span)-1
#             while j>=0 and self.stock_price[j]<=price:
#                 j-=self.span[j]
#             self.span.append(len(self.span)-j)
#             self.stock_price.append(price)
#         return self.span[-1]


class StockSpanner:
    def __init__(self):
        self.stock_price_span=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span=1
        while len(self.stock_price_span)!=0:
            if price>self.stock_price_span[-1][0]:
                span+=self.stock_price_span[-1][1]
                self.stock_price_span.pop()
            else:
                break
        self.stock_price_span.append((price,span))
        return self.stock_price_span[-1][1]






if __name__=="__main__":
    s=StockSpanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))

    s = StockSpanner()
    print(s.next(29))
    print(s.next(91))
    print(s.next(62))
    print(s.next(76))
    print(s.next(51))


