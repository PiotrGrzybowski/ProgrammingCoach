from unittest import TestCase, main

from structures.queues import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.head.value, 3)
        self.assertEqual(stack.head.next.value, 2)
        self.assertEqual(stack.head.next.next.value, 1)

    def test_push_init_elements(self):
        stack = Stack[int](1, 2, 3)

        self.assertEqual(stack.head.value, 3)
        self.assertEqual(stack.head.next.value, 2)
        self.assertEqual(stack.head.next.next.value, 1)

    def test_front(self):
        stack = Stack[int](1, 2, 3)

        self.assertEqual(stack.front(), 3)

    def test_pop_stack_with_elements(self):
        stack = Stack[int](1, 2, 3)

        popped = stack.pop()

        self.assertEqual(popped, 3)
        self.assertEqual(stack.head.value, 2)
        self.assertEqual(stack.head.next.value, 1)

    def test_pop_empty_stack(self):
        stack = Stack[int]()

        self.assertRaises(Stack.EmptyStackError, stack.pop)


if __name__ == '__main__':
    main()
