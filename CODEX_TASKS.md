# Codex Tasks

## Task 1 - Create Basic App Skeleton

Create a Python PySide6 desktop application.

Requirements:

- Entry point: app/main.py
- Main window class: app/ui/main_window.py
- Window title: Mie Trak BOM Importer
- Include a drag-and-drop area for .xlsx files
- Include a table for BOM preview
- Include buttons:
  - Load File
  - Validate
  - Export Preview
  - Import BOM
- Disable Import BOM button for now
- Add basic logging

Do not implement SQL yet.

## Task 2 - Add BOM Line Model

Create a dataclass named BOMLine in app/models/bom_line.py.

Fields:

- source_file: str
- source_sheet: str
- source_row: int
- component_part_number: str
- description: str
- quantity: float
- unit_of_measure: str
- notes: str
- status: str
- message: str

## Task 3 - Build Excel Parser

Create app/parsers/packing_list_excel_parser.py.

Requirements:

- Accept path to .xlsx file
- Read workbook using openpyxl
- Detect likely header row
- Detect columns for:
  - part number
  - description
  - quantity
  - unit of measure
- Return a list of BOMLine objects
- Ignore blank rows
- Ignore rows where quantity is missing and part number is missing

Do not use hardcoded row numbers yet.

## Task 4 - Build Validation Service

Create app/services/validation_service.py.

Requirements:

- Accept list of BOMLine objects
- Validate:
  - part number is not blank
  - quantity exists
  - quantity is numeric
  - quantity > 0
- Set status to OK, WARNING, or ERROR
- Set message explaining result

## Task 5 - Connect Parser to UI

When user drops or loads an Excel file:

- Parse the file
- Validate results
- Display lines in preview table
- Show count of:
  - total lines
  - OK
  - WARNING
  - ERROR

## Task 6 - Export Preview to CSV

Add ability to export current preview table to CSV.

Fields:

- source_row
- component_part_number
- description
- quantity
- unit_of_measure
- status
- message

## Task 7 - Add Mock Work Order Search

Before SQL connection, add a fake Work Order search box.

Mock results:

- WO1001 - Test Parent Part A
- WO1002 - Test Parent Part B

User should be able to select one.

## Task 8 - Add SQL Connection Layer Placeholder

Create app/services/database.py.

Requirements:

- Read config.ini
- Prepare pyodbc connection string
- Do not connect automatically on app startup
- Add function test_connection()

Do not add insert logic yet.