from dataclasses import dataclass


@dataclass
class BOMLine:
    source_file: str
    source_sheet: str
    source_row: int
    component_part_number: str
    description: str
    quantity: float | None
    unit_of_measure: str
    notes: str = ""
    status: str = ""
    message: str = ""