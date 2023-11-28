import unittest
import store


class CartTestCase(unittest.TestCase):

    def test_add(self):
        customer = store.Customer('vasya', 'vasehkin')
        cart = store.Cart(customer, [])
        samsung = store.Product(2, 'galaxy_s21', 599, 29)
        iphone = store.Product(1, 'iphone15', 999, 5)
        self.assertEqual(len(cart.items), 0)
        # Добавляем один товар
        cart.add(samsung, 5)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].amount, 5)
        self.assertEqual(cart.items[0].product, samsung)
        # Добавляем второй товар
        cart.add(iphone, 3)
        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[1].amount, 3)
        self.assertEqual(cart.items[1].product, iphone)
        # Добавляем существующий товар
        cart.add(samsung, 2)
        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[0].amount, 7)
        # Добавляем больше чем есть на складе товаров
        cart.add(iphone, 3)
        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[1].amount, 3)



    def test_delete(self):
        customer = store.Customer('vasya', 'vasehkin')
        cart = store.Cart(customer, [])
        samsung = store.Product(2, 'galaxy_s21', 599, 29)
        iphone = store.Product(1, 'iphone15', 999, 5)
        cart.add(iphone, 2)
        cart.add(samsung, 3)
        # Удаляем одну штуку
        cart.delete(iphone, 1)
        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[0].amount, 1)
        # Удаляем полностью один товар
        cart.delete(samsung, 3)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].product, iphone)
        self.assertEqual(cart.items[0].amount, 1)
        # Удаляем больше чем есть в корзине
        cart.delete(iphone, 15)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].product, iphone)
        self.assertEqual(cart.items[0].amount, 1)

    def test_total_price(self):
        gold_plan = store.DiscountPlan('gold', 0.15)
        samsung = store.Product(2, 'galaxy_s21', 599, 29)
        iphone = store.Product(1, 'iphone15', 999, 5)
        # Без скидок
        customer1 = store.Customer('vasya', 'vasehkin')
        cart1 = store.Cart(customer1, [])
        cart1.add(iphone, 3)
        cart1.add(samsung, 8)
        self.assertEqual(cart1.total_price(), 7789)
        # Со скидкой
        customer2 = store.Customer('petya', 'petyachkin', gold_plan)
        cart2 = store.Cart(customer2, [])
        cart2.add(iphone, 3)
        cart2.add(samsung, 8)
        self.assertEqual(cart2.total_price(), 6620.65)

    def test_sufficient_amount_in_stock(self):
        samsung = store.Product(2, 'galaxy_s21', 599, 29)
        iphone = store.Product(1, 'iphone15', 999, 5)
        customer1 = store.Customer('vasya', 'vasehkin')
        cart1 = store.Cart(customer1, [])
        cart1.add(iphone, 3)
        cart1.add(samsung, 8)
        self.assertTrue(cart1.sufficient_amount_in_stock())
        cart1.add(iphone, 2)
        customer2 = store.Customer('joe', 'fast')
        cart2 = store.Cart(customer2, [])
        cart2.add(iphone, 2)
        cart2.reserve()
        self.assertFalse(cart1.sufficient_amount_in_stock())

    def test_reserve(self):
        iphone = store.Product(1, 'iphone15', 999, 5)
        samsung = store.Product(2, 'galaxy_s21', 599, 29)
        # Резервируем товары которых хватает на складе
        customer1 = store.Customer('vasya', 'vasehkin')
        cart1 = store.Cart(customer1, [])
        cart1.add(iphone, 3)
        self.assertEqual(iphone.amount_in_stock, 5)
        self.assertEqual(cart1.status, 'New')
        cart1.reserve()
        self.assertEqual(iphone.amount_in_stock, 2)
        self.assertEqual(cart1.status, 'Reserved')
        # Резервируем пустую корзину
        customer2 = store.Customer('petya', 'petyachkin')
        cart2 = store.Cart(customer2, [])
        cart2.reserve()
        self.assertEqual(samsung.amount_in_stock, 29)
        self.assertEqual(iphone.amount_in_stock, 2)
        self.assertEqual(cart2.status, 'New')
        # Одного товара хватает на складе, а второго нет
        customer3 = store.Customer('serega', 'prosto')
        cart3 = store.Cart(customer3, [])
        cart3.add(samsung, 20)
        cart3.add(iphone, 2)
        customer4 = store.Customer('joe', 'fast')
        cart4 = store.Cart(customer4, [])
        cart4.add(iphone, 1)
        cart4.reserve()
        self.assertEqual(cart4.status, 'Reserved')
        self.assertEqual(iphone.amount_in_stock, 1)
        cart3.reserve()
        self.assertEqual(samsung.amount_in_stock, 29)
        self.assertEqual(iphone.amount_in_stock, 1)
        self.assertEqual(cart3.status, 'New')


if __name__ == '__main__':
    unittest.main()
