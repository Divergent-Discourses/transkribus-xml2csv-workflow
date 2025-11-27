# Quick Reference Card

## Installation
```bash
pip install -r requirements.txt
```

## Basic Usage
```bash
python workflow.py
```

## File Locations

### INPUT
Place your PageXML files here:
```
data/to_process_xml/
```

### OUTPUT
Results are saved to:
```
data/step1_extracted_csv/      # Extracted paragraphs
data/step2_normalized_csv/     # Normalized text
data/step3_merged_csv/         # Final merged CSV
```

## Configuration Quick Edits

### Skip a Step
Edit `workflow_config.ini`:
```ini
[workflow]
enable_extraction = False    # Skip this step
enable_normalization = True
enable_merge = True
```

### Change Normalization Rules
```ini
[normalization]
flag = 0    # Change from 1 to 0
```

### Change Output Locations
```ini
[paths]
extracted_csv_dir = ./my_custom_output
normalized_csv_dir = ./another_location
```

## Command Line Options
```bash
# Use default config
python workflow.py

# Use custom config file
python workflow.py --config my_config.ini
```

## Workflow Steps

| Step | Input | Output | Action |
|------|-------|--------|--------|
| 1. Extract | XML files | CSV files | Extract paragraphs |
| 2. Normalize | Step 1 CSVs | Normalized CSVs | Apply text rules |
| 3. Merge | Step 2 CSVs | Single CSV | Combine all files |

## Output CSV Columns

1. `paragraph` - Original text
2. `normalised_paragraph` - Normalized text ⭐ NEW
3. `paragraph_idx` - Paragraph ID
4. `readingorder_idx` - Reading order
5. `region_type` - heading/paragraph/caption
6. `filename` - Image filename
7. `newspaper` - Newspaper code
8. `year` - Year
9. `month` - Month
10. `date` - Day
11. `page_num` - Page number

## Troubleshooting

| Problem | Quick Fix |
|---------|-----------|
| No XML files found | Put .xml files in `data/to_process_xml/` |
| No tables found | Ensure .tsv files are in `tables/` |
| Import error | Run `pip install -r requirements.txt` |
| Wrong filename format | Use format: `0001_QTN_1959_10_03_001_*.xml` |

## Filename Format

PageXML files must follow this pattern:
```
XXXX_NEWSPAPER_YYYY_MM_DD_PPP_[anything].xml

XXXX = Transkribus ID (4 digits)
NEWSPAPER = Newspaper code
YYYY = Year
MM = Month
DD = Day
PPP = Page number
[anything] = Optional additional info
```

Example: `0001_QTN_1959_10_03_001_SB_Zsn128163MR.xml`

## Module Usage (Python)

```python
# Import modules
from extractor import XMLParagraphExtractor
from normalizer import load_tables, normalize_csv_files
from merger import merge_csv_files

# Use individually
extractor = XMLParagraphExtractor(namespace_uri, excluded_files)
tables = load_tables(table_path, flag=1)
merge_csv_files(input_dir, output_file)
```

## Log Files

Check for detailed information:
```
logs/workflow.log
```

## Need More Help?

- Full documentation: `README.md`
- Quick start guide: `QUICKSTART.md`
- Project overview: `PROJECT_SUMMARY.md`

## Success Indicators

✓ Extraction complete: [N] CSV files created
✓ Normalization complete: [N] files normalized  
✓ Merge complete: Output file created
✓ WORKFLOW COMPLETED SUCCESSFULLY

---

**Project**: Divergent Discourses  
**Institutions**: SOAS University of London & Leipzig University  
**Funding**: AHRC (UK) & DFG (Germany)
