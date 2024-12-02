import unittest
import day_02 as day

DAY = "02"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 2

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 4

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()