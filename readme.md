# Mie Trak BOM Importer

Portable Windows tool for importing Engineering Packing Lists into Mie Trak BOMs.

## Goal

This tool allows a user to:

1. Drag and drop an Engineering Packing List file.
2. Select a target Work Order from Mie Trak.
3. Parse the packing list into BOM lines.
4. Validate all components before import.
5. Preview exactly what will be imported.
6. Import only after user confirmation.
7. Keep logs and validation reports.

## First Version Scope

Version 1 will NOT insert into Mie Trak yet.

Version 1 will only:

- Load Excel packing list files.
- Parse BOM-like rows.
- Display a preview table.
- Validate basic data.
- Export parsed BOM preview as CSV.

## Later Versions

Version 2:

- Connect to SQL Server.
- Search/select Work Orders.
- Validate part numbers against Mie Trak.

Version 3:

- Write to BOM import staging table.
- Call SQL stored procedure to import BOM safely.

Version 4:

- Compare existing BOM vs packing list.
- Skip duplicates.
- Support controlled quantity updates.

## Safety Rules

- Never import directly without preview.
- Never replace an existing BOM in Version 1.
- Never hardcode database credentials.
- All imports must be logged.
- Any SQL write must be inside a transaction.