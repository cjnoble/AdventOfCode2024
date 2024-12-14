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

    def test_2_single_region(self):
        expected = 36  # Area = 9, sides =  4 -> 9 * 4 = 36

        data = [
            "AAA",
            "AAA",
            "AAA"
        ]

        result = day.part_2(data)
        self.assertEqual(result, expected)

    def test_diagonal_regions(self):
        expected = 80  # 2*(4 * 4) + 2*(6*4)

        data = [
            "AABBB",
            "AABBB",
            "CCDDD",
            "CCDDD"
        ]

        result = day.part_2(data)
        self.assertEqual(result, expected)

    def test_diagonal_regions_2(self):
        expected = 86  # 4*4 + 6*4 + 3*6 + 3*4 + 1*4 + 2*4+ 1*4

        data = [
            "AABBB",
            "AABBB",
            "CCAAA",
            "CADDB"
        ]

        result = day.part_2(data)
        self.assertEqual(result, expected)

    def test_2_simple_1(self):

        expected = 368

        data = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]

        result = day.part_2(data)

        self.assertEqual(result, expected)

    def test_2_simple_2(self):

        expected = 236

        data = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]

        result = day.part_2(data)

        self.assertEqual(result, expected)

    def test_2_hollow_region(self):
        expected = 136  # 6*4 + 14*8

        data = [
            "AAAAA",
            "AEEEA",
            "AEEEA",
            "AAAAA"
        ]

        result = day.part_2(data)
        self.assertEqual(result, expected)

    def test_2(self):

        expected = 1206

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
