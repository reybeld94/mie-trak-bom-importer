# Project Specification

## Problem

Engineering creates a Packing List when releasing a job. This Packing List represents the materials/components needed for the job, similar to a Bill of Material in Mie Trak.

Currently, Engineering does not manually enter this BOM into Mie Trak. The goal is to build a portable Windows tool that reads the Packing List and helps import it into the correct Mie Trak Work Order after validation.

## Target User

Internal company users who need to import Engineering Packing Lists into Mie Trak.

## Main Workflow

1. User opens the portable app.
2. User drags and drops a Packing List Excel file.
3. App reads the file.
4. User searches/selects the target Work Order.
5. App validates the extracted BOM lines.
6. App shows a preview table.
7. User reviews errors/warnings.
8. If no blocking errors exist, user confirms import.
9. App imports the BOM using a safe SQL process.
10. App generates a log/report.

## Initial MVP

The MVP should only support Excel files.

The MVP should:

- Open a desktop window.
- Accept drag and drop of `.xlsx` files.
- Parse the file into BOM line objects.
- Show a preview grid.
- Show validation status per line.
- Export preview to CSV.

The MVP should NOT connect to Mie Trak yet.

## Technology

- Python 3.11+
- PySide6 for UI
- openpyxl or pandas for Excel parsing
- pyodbc for future SQL Server connection
- pytest for tests
- PyInstaller for future portable EXE build

## Main Screens

### Main Window

Sections:

- File drop area
- File information
- Work Order search/selection area
- Validation summary
- BOM preview table
- Action buttons

Buttons:

- Load File
- Validate
- Export Preview
- Import BOM

In MVP, Import BOM should be disabled.

## BOM Line Fields

Each parsed BOM line should contain:

- source_file
- source_sheet
- source_row
- component_part_number
- description
- quantity
- unit_of_measure
- notes
- status
- message

## Validation Status

Valid statuses:

- OK
- WARNING
- ERROR

## Blocking Errors

Import must be blocked if:

- Component part number is blank
- Quantity is blank
- Quantity is zero or negative
- Quantity is not numeric
- Required columns cannot be detected

## Future SQL Safety

When SQL import is added:

- Use staging table first
- Use stored procedure for final import
- Use SQL transaction
- Rollback on error
- Write import log
- Never hardcode credentials