Libraries and tool dependencies:
Prototyping:
- Python
- Pandas
- DuckDB
- GeoParquet
Production:
- Rust
- Polars
Steps to process GPX files:
- Grab gpx files. Either specified (for testing) or recursively for an entire folder.
- Import to Dataframe
- Remove null columns: https://stackoverflow.com/questions/76338261/polars-and-the-lazy-api-how-to-drop-columns-that-contain-only-null-values
- Insure columns are typed
- Calculate metadata