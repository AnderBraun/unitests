import unittest

from utils.arrs import get
from utils.arrs import my_slice

class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEquals(get([1, 2, 3], 1, "test"),2)
        self.assertEquals(get([], 0, "test"),"test")


    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4, 5]),[1, 2, 3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=2),[3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=-3),[3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], end=3),[1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], end=-2),[1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=1, end=4),[2, 3, 4])

        self.assertEqual(my_slice([]),[])
        self.assertEqual(my_slice([], start=3, end=5),[])

        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=10),[])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], end=10),[1, 2, 3, 4, 5])

        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=-5, end=-2),[1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=-5, end=-1),[1, 2, 3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], start=-5, end=-6),[])

        self.assertEqual(my_slice("Hello, World!"),"Hello, World!")
        self.assertEqual(my_slice("Hello, World!", start=7),"World!")
        self.assertEqual(my_slice("Hello, World!", start=-6),"World!")
        self.assertEqual(my_slice("Hello, World!", end=5),"Hello")
        self.assertEqual(my_slice("Hello, World!", end=-8),"Hello")
        self.assertEqual(my_slice("Hello, World!", start=1, end=9),"ello, Wo")