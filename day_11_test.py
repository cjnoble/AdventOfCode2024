import unittest
import day_11 as day

DAY = "11"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = 55312

        result = day.part_1(test_data)

        self.assertEqual(result, expected)

    def test_1_6(self):

        expected = 22

        result = day.blink(day.prepare_stone(test_data), 6)

        self.assertEqual(sum(result.values()), expected)



if __name__ == '__main__':
    unittest.main()