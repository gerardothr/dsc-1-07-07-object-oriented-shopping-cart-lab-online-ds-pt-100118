class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None, total=0, items=[]):
        self.employee_discount = employee_discount
        self.items = items
        self.total = total
        
    def add_item(self, name, price, quantity=1):
       self.total += quantity * price
       for i in range(quantity):
            self.items.append({'name' : name, 'price' : price})
       return self.total

    def mean_item_price(self):
        mean = self.total / len(self.items)
        return round(mean, 2)

    def median_item_price(self):
        prices = []
        for i in self.items:
            prices.append(i['price'])
        sorted_prices = sorted(prices)
        if len(sorted_prices) % 2 != 0:
            median = sorted_prices[int(len(sorted_prices)/2)]
        elif len(sorted_prices) % 2 == 0:
            median = (sorted_prices[int(len(sorted_prices)/2)] + sorted_prices[int(len(sorted_prices)/2) + 1])/2
        return round(median, 2)

    def apply_discount(self):
       if self.employee_discount == None:
           return "Sorry, there is no discount to apply to your cart :("
       elif self.employee_discount == 0:
           return "Sorry, there is no discount to apply to your cart :("
       else:
            self.total = self.total - self.total * (self.employee_discount / 100)
            return self.total

    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        else:
            last_item = self.items.pop(-1)
            self.total = self.total - last_item['price']
            return self.total