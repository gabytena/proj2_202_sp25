import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)


# Put your data definitions first!

@dataclass(frozen = True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: float
    electricity_and_heat_co2_emissions_per_capita: float
    energy_co2_emissions: float
    energy_co2_emissions_per_capita: float
    total_co2_emissions_excluding_lucf: float
    total_co2_emissions_excluding_lucf_per_capita: float

@dataclass(frozen = True)
class Node:
    value: Row
    next: "Node | None"


# Then your functions.
def parse_row(fields: list[str]) -> Row:
    return Row(country = fields[0],
                year = int(fields[1]),
                electricity_and_heat_co2_emissions = float(fields[2]),
                electricity_and_heat_co2_emissions_per_capita = float(fields[3]),
                energy_co2_emissions = float(fields[4]),
                energy_co2_emissions_per_capita = float(fields[5]),
                total_co2_emissions_excluding_lucf = float(fields[6]),
                total_co2_emissions_excluding_lucf_per_capita = float(fields[7]))


def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename, newline = "") as file:
        csvFile = csv.reader(filename)
        rows = list(csvFile)

    head = ["country",
            "year",
            "electricity_and_heat_co2_emissions",
            "electricity_and_heat_co2_emissions_per_capita",
            "energy_co2_emissions",
            "energy_co2_emissions_per_capita",
            "total_co2_emissions_excluding_lucf",
            "total_co2_emissions_excluding_lucf_per_capita"]


    if row[0] or rows != head:
        return None
    
    def linked_list(idx: int) ->Optional(Node):
        if idx >= len(rows):
            return None
        
        row_object = parse_row(rows[idx])
        return Node(row_object, linked_list(idx +1))
    
    return linked_list(1)

def listlen(data: Optional[Node]) -> int:
    if data is None:
        return 0
    return 1 + listlen(data.next)


def filter_rows(data: Optional[Node],
                field_name: str,
                comparison: str,
                value: Union[str, float, int]) -> Optional[Node]:
    pass