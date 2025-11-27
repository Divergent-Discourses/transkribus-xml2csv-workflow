# Quick Start Guide

## Installation (5 minutes)

1. **Extract the workflow files** to your desired location

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Workflow (3 steps)

### Step 1: Prepare Your Data

Place your Transkribus PageXML files in:
```
data/to_process_xml/
```

Your normalization tables should already be in:
```
tables/
├── abbreviations.tsv
├── table1.tsv
├── table2.tsv
└── table3.tsv
```

### Step 2: Configure (Optional)

Edit `workflow_config.ini` if you need to change:
- Input/output directories
- Enable/disable specific steps
- Normalization flag parameter
- Logging options

Default settings work for most cases!

### Step 3: Run

```bash
python workflow.py
```

## What Happens?

The workflow will automatically:

1. **Extract** paragraphs from all XML files
   - Output: `data/step1_extracted_csv/*.csv`

2. **Normalize** Tibetan text in each CSV
   - Output: `data/step2_normalized_csv/*.csv`

3. **Merge** all normalized CSVs into one file
   - Output: `data/step3_merged_csv/merged_pages.csv`

## Checking Results

Each step creates its own output directory, so you can:
- Review extracted paragraphs in `step1_extracted_csv/`
- Check normalization results in `step2_normalized_csv/`
- Use the final merged file from `step3_merged_csv/`

## Common Scenarios

### Run Only Extraction
```ini
[workflow]
enable_extraction = True
enable_normalization = False
enable_merge = False
```

### Skip Normalization
```ini
[workflow]
enable_extraction = True
enable_normalization = False
enable_merge = True
```

### Re-run Normalization Only
1. Disable extraction: `enable_extraction = False`
2. Keep normalization enabled
3. Run workflow again

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "No XML files found" | Check files are in `data/to_process_xml/` |
| "No normalization tables" | Verify `.tsv` files are in `tables/` |
| "No 'paragraph' column" | Input CSVs must have a 'paragraph' column |
| Import errors | Run `pip install -r requirements.txt` |

## Example Output

After running, your directory will look like:

```
transkribus-workflow/
├── data/
│   ├── to_process_xml/          # Your input XML files
│   ├── step1_extracted_csv/     # 100 CSV files extracted
│   ├── step2_normalized_csv/    # 100 CSV files normalized
│   └── step3_merged_csv/        # 1 merged CSV file
│       └── merged_pages.csv     # ← Your final output!
├── logs/
│   └── workflow.log             # Detailed processing log
└── ...
```

## Next Steps

- Open `merged_pages.csv` in your preferred tool
- Compare `paragraph` and `normalised_paragraph` columns
- Use the data for your analysis

## Need Help?

Check the full `README.md` for:
- Detailed configuration options
- Advanced usage examples
- Module-level API documentation
- Troubleshooting guide
