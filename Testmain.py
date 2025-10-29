from main import Item, Inventory

import unittest

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = ("Mango", 6, 7)

    def testStr(self):
        self.assertEqual(str(self.item), "Item: Apple, Price: 2.5, Quantity: 10")

    def testEq(self):
        other = Item('Mango', 6, 1)
        self.assertTrue(self.item.name == other.name and self.item.price == other.price)

    def testLt(self):
        other = Item("Mustard", 4, 8)
        self.assertTrue(self.item.price < other.price)

class testInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.Apple = Item('Apple', 4, 10)
        self.Pear = Item('Pear', 3, 12)
        self.inv + self.Apple
        self.inv + self.Pear

    def testLen(self):
        self.assertEqual(len(self.inv), 2)

    def testGetItem(self):
        self.assertEqual(self.inv[0], self.Apple)
    
    def testSetItem(self):
        cookie = Item("Cookie", 2, 25)
        self.inv[1] = cookie
        self.assertEqual(self.inv[1], cookie)

    def testAddItem(self):
        pass

if __name__ == '__main__':
    unittest.main()