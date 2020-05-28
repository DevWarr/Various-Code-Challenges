import unittest
from ListNode import ListNode, createSLLFromNumbers

def merge_two_lists(l1, l2):

    # Potential edge cases
    if not l1:
        return l2
    if not l2:
        return l1

    result = None
    l1_curr = l1
    l2_curr = l2

    # Initialize result as the first lowest node
    if l1.val < l2.val:
        result = l1
        l1_curr = l1.next
    else:
        result = l2
        l2_curr = l2.next

    curr = result

    while l1_curr or l2_curr:

        # If one list is leftover at the end,
        # simply connect it and break
        if not l1_curr:
            curr.next = l2_curr
            break
        if not l2_curr:
            curr.next = l1_curr
            break

        if l1_curr.val < l2_curr.val:
            curr.next = l1_curr
            l1_curr = l1_curr.next
        else:
            curr.next = l2_curr
            l2_curr = l2_curr.next

        curr = curr.next

    return result


class MergeTwoListsTest(unittest.TestCase):

    def test_1(self):
        l1 = createSLLFromNumbers(54321)
        l2 = createSLLFromNumbers(643)

        expected_values = [1, 2, 3, 3, 4, 4, 5, 6]

        result = merge_two_lists(l1, l2)
        
        for i in range(len(expected_values)):
            self.assertEqual(result.val, expected_values[i])
            result = result.next

    def test_2(self):
        l1 = createSLLFromNumbers(111)
        l2 = createSLLFromNumbers(87642)

        expected_values = [1, 1, 1, 2, 4, 6, 7, 8]

        result = merge_two_lists(l1, l2)
        
        for i in range(len(expected_values)):
            self.assertEqual(result.val, expected_values[i])
            result = result.next

    def test_3(self):
        l1 = createSLLFromNumbers(88866642)
        l2 = createSLLFromNumbers(98765421)

        expected_values = [1, 2, 2, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8, 8, 9]

        result = merge_two_lists(l1, l2)
        
        for i in range(len(expected_values)):
            self.assertEqual(result.val, expected_values[i])
            result = result.next

if __name__ == "__main__":
    unittest.main()