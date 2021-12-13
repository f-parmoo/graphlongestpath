import unittest
import graphpath


class GraphPathtest(unittest.TestCase):
    def test_calculate_longest_path(self):
        graph_list = [('a', 'b'), ('b', 'e'), ('e', 'f'), ('b', 'c'), ('c', 'd')]
        result = graphpath.calculate_longest_path(graph_list)
        self.assertEqual(result[0], ['f-e-b-c-d', 'd-c-b-e-f'])
        self.assertEqual(result[1], 4)


if __name__ == '__main__':
    unittest.main()
