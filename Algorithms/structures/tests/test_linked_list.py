from unittest import TestCase, main

from structures.lists import LinkedList


class TestLinkedList(TestCase):
    def test_init_without_elements(self):
        values = LinkedList[int]()

        self.assertIsNone(values.head)

    def test_string_empty_list(self):
        values = LinkedList[int]()

        self.assertEqual(str(values), '[]')

    def test_string_one_element_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9)

        self.assertEqual(str(values), '[9]')

    def test_string_many_elements_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertEqual(str(values), '[9, 5, 1]')

    def test_length_empty_list(self):
        values = LinkedList[int]()
        self.assertEqual(len(values), 0)

    def test_length_one_element_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9)

        self.assertEqual(len(values), 1)

    def test_length_many_elements_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertEqual(len(values), 3)

    def test_clear(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        values.clear()
        self.assertEqual(values.head, None)
        self.assertEqual(len(values), 0)

    def test_append_one_element(self):
        values = LinkedList[int]()
        values.append(9)

        self.assertEqual(len(values), 1)
        self.assertEqual(str(values), '[9]')

    def test_append_many_elements(self):
        values = LinkedList[int]()
        values.append(9)
        values.append(5)
        values.append(1)

        self.assertEqual(len(values), 3)
        self.assertEqual(str(values), '[9, 5, 1]')

    def test_init_with_elements(self):
        values = LinkedList[int](9, 5, 1)

        self.assertEqual(str(values), '[9, 5, 1]')
        self.assertEqual(len(values), 3)

    def test_get_item_first_element(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        self.assertEqual(values[0], 9)

    def test_get_item_last_element(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        self.assertEqual(values[4], 8)

    def test_get_item_out_of_range(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        self.assertRaises(IndexError, values.__getitem__, 20)

    def test_set_item_first_element(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        values[0] = 90
        self.assertEqual(values[0], 90)

    def test_set_item_last_element(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        values[4] = 80
        self.assertEqual(values[4], 80)

    def test_set_item_out_of_range(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        self.assertRaises(IndexError, values.__setitem__, 20, 999)

    def test_iterate(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        new_values = LinkedList[int]()

        for value in values:
            new_values.append(value)

        self.assertEqual(values, new_values)

    def test_equal_empty_lists(self):
        first_values = LinkedList[int]()
        second_values = LinkedList[int]()

        self.assertTrue(first_values == second_values)

    def test_equal_many_elements_lists(self):
        first_values = LinkedList[int](9, 5, 1, 4, 8)
        second_values = LinkedList[int](9, 5, 1, 4, 8)

        self.assertTrue(first_values == second_values)

    def test_not_equals_many_elements_lists(self):
        first_values = LinkedList[int](9, 5, 1, 4, 8)
        second_values = LinkedList[int](9, 5, 1, 4)

        self.assertFalse(first_values == second_values)

    def test_not_equals_one_empty_list(self):
        first_values = LinkedList[int]()
        second_values = LinkedList[int](9, 5, 1, 4)

        self.assertFalse(first_values == second_values)

    def test_index_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertEqual(values.index(9), 0)
        self.assertEqual(values.index(5), 1)
        self.assertEqual(values.index(1), 2)

    def test_index_element_not_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertRaises(ValueError, values.index, 7)
        self.assertRaises(ValueError, values.index, 3)
        self.assertRaises(ValueError, values.index, 4)

    def test_contains_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertTrue(9 in values)
        self.assertTrue(5 in values)
        self.assertTrue(1 in values)

    def test_contains_element_not_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node(9, LinkedList.Node(5, LinkedList.Node(1)))

        self.assertFalse(7 in values)
        self.assertFalse(3 in values)
        self.assertFalse(4 in values)

    def test_pop_element_from_first_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.pop(0)

        self.assertEqual(deleted_value, 9)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[5, 1, 4, 8]')

        values = LinkedList[int](9)
        deleted_value = values.pop(0)

        self.assertEqual(deleted_value, 9)
        self.assertEqual(len(values), 0)
        self.assertEqual(str(values), '[]')

    def test_pop_element_from_middle_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.pop(2)

        self.assertEqual(deleted_value, 1)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[9, 5, 4, 8]')

    def test_pop_element_from_last_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.pop(4)

        self.assertEqual(deleted_value, 8)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[9, 5, 1, 4]')

    def test_pop_element_from_index_out_of_range(self):
        values = LinkedList[int](9, 5, 1, 4, 8)

        self.assertRaises(IndexError, values.pop, 20)
        self.assertRaises(IndexError, values.pop, 5)
        self.assertRaises(IndexError, values.pop, 10)

    def test_remove_element_from_first_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.remove(9)

        self.assertEqual(deleted_value, 9)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[5, 1, 4, 8]')

        values = LinkedList[int](9)
        deleted_value = values.remove(9)

        self.assertEqual(deleted_value, 9)
        self.assertEqual(len(values), 0)
        self.assertEqual(str(values), '[]')

    def test_remove_element_from_middle_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.remove(1)

        self.assertEqual(deleted_value, 1)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[9, 5, 4, 8]')

    def test_remove_element_from_last_place(self):
        values = LinkedList[int](9, 5, 1, 4, 8)
        deleted_value = values.remove(8)

        self.assertEqual(deleted_value, 8)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[9, 5, 1, 4]')

    def test_remove_element_which_not_in_list(self):
        values = LinkedList[int](9, 5, 1, 4, 8)

        self.assertRaises(ValueError, values.remove, 20)
        self.assertRaises(ValueError, values.remove, 30)
        self.assertRaises(ValueError, values.remove, 10)


if __name__ == '__main__':
    main()
