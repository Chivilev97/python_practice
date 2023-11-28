class Customer(object):
    def __init__(self, first_name, last_name, discount_plan=None):
        self.first_name = first_name
        self.last_name = last_name
        self.discount_plan = discount_plan


class Product(object):
    def __init__(self, id, name, price, amount_in_stock):
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock
        self.id = id


class CartItem(object):
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount


class Cart(object):
    def __init__(self, customer, items, status='New'):
        self.customer = customer
        self.items = items
        self.status = status

    def add(self, product, amount):
        existing_item = None
        for i in self.items:
            if i.product == product:
                existing_item = i
                break
        total_amount = amount
        if existing_item:
            total_amount += existing_item.amount

        if total_amount > product.amount_in_stock:
            return False
        else:
            if existing_item:
                existing_item.amount = total_amount
            else:
                self.items.append(CartItem(product, amount))

    def delete(self, product, amount):
        for i in self.items:
            if i.product == product:
                if i.amount - amount == 0:
                    self.items.remove(i)
                elif i.amount - amount < 0:
                    return False
                else:
                    i.amount -= amount

    def total_price(self):
        prices = []
        for i in self.items:
            prices.append(i.product.price * i.amount)
        if self.customer.discount_plan:
            discount = sum(prices) * self.customer.discount_plan.discount_percent
            return sum(prices) - discount
        return sum(prices)
        
    def sufficient_amount_in_stock(self):
        for i in self.items:
            if i.amount > i.product.amount_in_stock:
                return False
        return True

    def reserve(self):
        if self.sufficient_amount_in_stock() and len(self.items) != 0:
            for i in self.items:
                i.product.amount_in_stock -= i.amount
            self.status = 'Reserved'
        else:
            return False


class DiscountPlan(object):
    def __init__(self, name, discount_percent):
        self.name = name
        self.discount_percent = discount_percent
