import unittest
import day_14 as day

DAY = "14"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 12   

        result = day.part_1(test_data, 11, 7)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 0

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()