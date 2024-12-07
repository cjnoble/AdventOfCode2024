import unittest
import day_07 as day

DAY = "07"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 3749

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_292(self):

        data=["292: 11 6 16 20"]
        expected = 292

        result = day.part_1(data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 11387

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()