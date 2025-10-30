from main import Item, Inventory
import unittest

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Mango", 6, 7)

    def testStr(self):
        self.assertEqual(str(self.item), "Mango - $6.00 (x7)")

    def testEq(self):
        other = Item("Mango", 6, 1)
        self.assertTrue(self.item == other)

    def testLt(self):
        other = Item("Mustard", 8, 8)
        self.assertTrue(self.item < other)


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.Apple = Item("Apple", 4, 10)
        self.Pear = Item("Pear", 3, 12)
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
        orange = Item("Orange", 2, 5)
        self.inv + orange
        self.assertIn(orange, self.inv.items)


if __name__ == "__main__":
    unittest.main()
