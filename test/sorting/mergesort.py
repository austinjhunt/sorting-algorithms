import unittest
from src.sorting.mergesort import merge_sort
from src.sample import nums, words


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = merge_sort(n_copy)
                self.assertEqual(result, n_sorted)

    def test_merge_sort_strings(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = merge_sort(n_copy)
                self.assertEqual(result, n_sorted)


if __name__ == "__main__":
    unittest.main()
