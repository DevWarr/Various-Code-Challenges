import unittest

def contains_duplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
    return False

class ContainsDuplicateTest(unittest.TestCase):
    
    def test_1(self):
        arr = [1, 2, 3]
        response = contains_duplicate(arr)
        self.assertFalse(response)

    def test_2(self):
        arr = [1, 2, 3, 1]
        response = contains_duplicate(arr)
        self.assertTrue(response)

    def test_3(self):
        arr = []
        response = contains_duplicate(arr)
        self.assertFalse(response)

if __name__ == "__main__":
    unittest.main()