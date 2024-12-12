import unittest
import day_12 as day

DAY = "12"
test_data = day.read_text_file(f"{DAY}_test.txt")


class TestMethods(unittest.TestCase):

    def test_1_simple(self):

        expected = 140

        data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]

        result = day.part_1(data)

        self.assertEqual(result, expected)

    def test_1(self):

        expected = 1930

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 1206

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
