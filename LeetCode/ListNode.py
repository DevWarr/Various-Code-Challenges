import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createSLLFromNumbers(number):
    curr = ListNode()
    track = curr

    num_str = str(number)
    for i in range(len(num_str) -1, -1, -1):
        track.next = ListNode(val=int(num_str[i]))
        track = track.next
    return curr.next


class CreateSLLFromNumbersTest(unittest.TestCase):

    def test_1(self):
        sll = createSLLFromNumbers(0)
        self.assertEqual(sll.val, 0)

    def test_2(self):
        sll = createSLLFromNumbers(125)
        self.assertEqual(sll.val, 5)
        self.assertEqual(sll.next.val, 2)
        self.assertEqual(sll.next.next.val, 1)

    def test_3(self):
        sll = createSLLFromNumbers(9876543210)
        track = sll

        for i in range(10):
            self.assertEqual(track.val, i)
            track = track.next