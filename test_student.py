import unittest
from typing import Optional, Union
from proj2 import (
    Row,
    Node,
    read_csv_lines,
    listlen,
    filter_rows,
    parse_row
)

class Test_GHG_csv(unittest.TestCase):
    def test_return_node(self):
        data = read_csv_lines("gtv_test.csv")
        self.assertIsInstance(data, Node)
    
    def test_parse_row(self):
        row = parse_row(["United States",
                         "2020",
                         "1764.85",
                         "5.253436",
                         "4279.84",
                         "12.739817",
                         "4320.53",
                         "12.860939"])
        self.assertEqual(row.country, "United States")
        self.assertEqual(row.year, 2020)
        self.assertEqual(row.electricity_and_heat_co2_emissions, 1764.85)
        self.assertEqual(row.total_co2_emissions_excluding_lucf, 4320.53)

    def test_listlen_none(self):
        self.assertEqual(listlen(None), 0)

    def test_listlen_gtv(self):
        data = read_csv_lines("gtv_test.csv")
        self.assertEqual(listlen(data), 8)







if __name__ == "__main__":
    unittest.main()
        
