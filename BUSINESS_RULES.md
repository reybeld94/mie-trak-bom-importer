# Business Rules

## General

The app imports Engineering Packing Lists into Mie Trak BOMs.

The user must always review the parsed BOM before import.

## Import Target

The user must select one specific Work Order.

Do not import based only on Sales Order because one Sales Order can have multiple Work Orders.

## Parsing

The Packing List may have a custom Engineering format.

The parser should not assume the first row contains headers.

The parser should try to detect columns such as:

- Part Number
- Part #
- Item
- Component
- Description
- Qty
- Quantity
- UOM
- Unit

Rows should be ignored if they are blank or contain summary/note-only information.

## Validation

Each BOM line must have:

- Component part number
- Quantity
- Valid positive numeric quantity

Warnings should be used for suspicious but not blocking conditions.

Errors should block import.

## Existing BOM Handling

First production version should only support:

- Add missing components only

Do not replace existing BOM automatically.

Do not update existing component quantities automatically.

## Import Safety

All imports must be:

- Previewed
- Confirmed by the user
- Logged
- Executed in a SQL transaction

## Security

No passwords in source code.

No credentials committed to GitHub.

Use config.ini or Windows authentication.