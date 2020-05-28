import unittest
from ListNode import ListNode, createSLLFromNumbers


def addTwoNumbers(l1, l2):

    result = ListNode()
    carry = 0

    l1_curr = l1
    l2_curr = l2
    result_curr = result

    while l1_curr or l2_curr or carry:
        result_curr.next = ListNode()
        result_curr = result_curr.next

        num1 = 0
        num2 = 0

        if l1_curr and l1_curr.val is not None:
            num1 = l1_curr.val
            l1_curr = l1_curr.next

        if l2_curr and l2_curr.val is not None:
            num2 = l2_curr.val
            l2_curr = l2_curr.next

        result_curr.val = (num1 + num2 + carry) % 10
        carry = (num1 + num2 + carry) // 10

    return result.next


class AddTwoNumbersTest(unittest.TestCase):

    def test_1(self):
        l1 = createSLLFromNumbers(125)
        l2 = createSLLFromNumbers(125)
        result = addTwoNumbers(l1, l2)

        # 125 + 125 = 250
        self.assertEqual(result.val, 0)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 2)

    def test_2(self):
        l1 = createSLLFromNumbers(342)
        l2 = createSLLFromNumbers(465)
        result = addTwoNumbers(l1, l2)

        # 342 + 465 = 807
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_3(self):
        l1 = createSLLFromNumbers(5678)
        l2 = createSLLFromNumbers(9932)
        result = addTwoNumbers(l1, l2)

        # 5678 + 9932 = 15610
        self.assertEqual(result.val, 0)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 6)
        self.assertEqual(result.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.val, 1)


if __name__ == "__main__":
    unittest.main()
