import unittest
import day_17 as day

DAY = "17"
test_data_1 = day.read_text_file(f"{DAY}_test_1.txt")
test_data_2 = day.read_text_file(f"{DAY}_test_2.txt")

class TestMethods(unittest.TestCase):

    def test_1(self):

        expected = "4,6,3,5,6,3,5,2,1,0"

        result = day.part_1(test_data_1)

        self.assertEqual(result, expected)

    def test_2(self):

        out = day.test(test_data_2, 3)
        
        expected = 117440

        out = day.test(test_data_2, expected)
        print(out)

        result = day.part_2(test_data_2)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()