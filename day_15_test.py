import unittest
import day_15 as day

DAY = "15"
test_data = day.read_text_file(f"{DAY}_test.txt")

class TestMethods(unittest.TestCase):


    def test_1_small(self):

        data = [
            "########",
            "#..O.O.#",
            "##@.O..#",
            "#...O..#",
            "#.#.O..#",
            "#...O..#",
            "#......#",
            "########",
            "",
            "<^^>>>vv<v>>v<<"
        ]

        expected = 2028

        result = day.part_1(data)

        self.assertEqual(result, expected)



    def test_1(self):

        expected = 10092

        result = day.part_1(test_data)

        self.assertEqual(result, expected)


    def test_2_small(self):

        expected = 105 + 207 + 306

        data = [

        "#######",
        "#...#.#",
        "#.....#",
        "#..OO@#",
        "#..O..#",
        "#.....#",
        "#######",
        "",
        "<vv<<^^<<^^"
                ]
        
        result = day.part_2(data)

        self.assertEqual(result, expected)

    def test_2(self):

        expected = 9021  

        result = day.part_2(test_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()