import unittest

def two_sum(nums, target):
        
    already_seen = {}
    
    for i in range(len(nums)):
        if target - nums[i] in already_seen:
            return [already_seen[target-nums[i]], i]
        else:
            already_seen[nums[i]] = i

class TwoSumTest(unittest.TestCase):

    def test_1(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7]
        target = 11
        expected = [5, 6]

        result = two_sum(nums, target)
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])

    def test_2(self):
        nums = [3, 57, 12, 7, 1000092, 35, 67, 234, 5784]
        target = 1000092 + 234
        expected = [4, 7]

        result = two_sum(nums, target)
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])

    def test_3(self):
        nums = [150000, 35, 4, 5, 54]
        target = 35 + 54
        expected = [1, 4]

        result = two_sum(nums, target)
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])


if __name__ == "__main__":
    unittest.main()