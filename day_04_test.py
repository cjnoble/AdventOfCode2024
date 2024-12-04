import unittest
import day_04 as day

DAY = "04"
test_data = day.read_text_file(f"{DAY}_test.txt")


class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 18

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 9

        result = day.part_2(test_data)

        self.assertEqual(result, expected)

    def test_XMAS_1(self):

        expected = 1

        result = day.part_2(["MXS", "XAX", "MXS"])

        self.assertEqual(result, expected)

    def test_XMAS_2(self):

        expected = 1

        result = day.part_2(["MXM", "XAX", "SXS"])

        self.assertEqual(result, expected)

    def test_XMAS_3(self):

        expected = 1

        result = day.part_2(["SXS", "XAX", "MXM"])

        self.assertEqual(result, expected)

    def test_XMAS_4(self):

        expected = 1

        result = day.part_2(["SXM", "XAX", "SXM"])

        self.assertEqual(result, expected)

    def test_double_XMAS_1(self):

        expected = 2

        result = day.part_2(["MXSXM", "XAXAX", "MXSXM"])

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
