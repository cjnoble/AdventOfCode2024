import unittest
import day_06 as day

DAY = "06"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 41

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 6

        result = day.part_2(test_data)

        self.assertEqual(result, expected)

    def test_3(self):
        data = [
        "#######",
        "#^    #",
        "      #",
        "#######"
        ]

        expected = 6

        result = day.part_2(data)

        self.assertEqual(result, expected)

    def test_4(self):
        data = [
        "### ###",
        "#     #",
        "#  ^  #",
        "#######"
        ]

        expected = 2

        result = day.part_2(data)

        self.assertEqual(result, expected)

    def test_5(self):
        data = [
        "# #####",
        "#     #",
        "#  ^  #",
        "#######"
        ]

        expected = 5

        result = day.part_2(data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()